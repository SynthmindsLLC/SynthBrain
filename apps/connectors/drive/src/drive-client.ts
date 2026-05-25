import { google, type drive_v3 } from 'googleapis';

/**
 * Move-capable Google Drive v3 wrapper. Unlike the read+copy-only MCP, this
 * uses files.update(addParents/removeParents) for true moves, files.update(name)
 * for renames, and files.update(trashed) for reversible deletes.
 *
 * Auth: OAuth2 refresh token (GOOGLE_OAUTH_CLIENT_ID / _SECRET / _REFRESH_TOKEN).
 * Scope required: https://www.googleapis.com/auth/drive
 *
 * Every mutating method honors `commit`. When false (default), it logs the
 * intended action and performs no write.
 */

const FOLDER_MIME = 'application/vnd.google-apps.folder';

export interface DriveFile {
  id: string;
  name: string;
  mimeType: string;
  parents?: string[];
  size?: string;
  modifiedTime?: string;
  md5Checksum?: string;
}

export class DriveClient {
  private readonly drive: drive_v3.Drive;
  private readonly folderCache = new Map<string, string>();

  constructor(private readonly commit: boolean) {
    const clientId = required('GOOGLE_OAUTH_CLIENT_ID');
    const clientSecret = required('GOOGLE_OAUTH_CLIENT_SECRET');
    const refreshToken = required('GOOGLE_OAUTH_REFRESH_TOKEN');
    const auth = new google.auth.OAuth2(clientId, clientSecret);
    auth.setCredentials({ refresh_token: refreshToken });
    this.drive = google.drive({ version: 'v3', auth });
  }

  /** List direct children of a folder ('root' for My Drive). */
  async listChildren(parentId: string): Promise<DriveFile[]> {
    const out: DriveFile[] = [];
    let pageToken: string | undefined;
    do {
      const res = await this.drive.files.list({
        q: `'${parentId}' in parents and trashed = false`,
        fields: 'nextPageToken, files(id,name,mimeType,parents,size,modifiedTime,md5Checksum)',
        pageSize: 1000,
        pageToken,
      });
      out.push(...((res.data.files ?? []) as DriveFile[]));
      pageToken = res.data.nextPageToken ?? undefined;
    } while (pageToken);
    return out;
  }

  /**
   * Ensure a nested folder path exists under `rootId` (e.g. ["Projects","PBTV"]).
   * Returns the leaf folder id. Cached. In dry-run, returns a synthetic id.
   */
  async ensureFolderPath(segments: string[], rootId = 'root'): Promise<string> {
    let parent = rootId;
    let cacheKey = rootId;
    for (const name of segments) {
      cacheKey = `${cacheKey}/${name}`;
      const cached = this.folderCache.get(cacheKey);
      if (cached) {
        parent = cached;
        continue;
      }
      const existing = await this.findFolder(name, parent);
      if (existing) {
        this.folderCache.set(cacheKey, existing);
        parent = existing;
        continue;
      }
      if (!this.commit) {
        console.log(`[dry-run] create folder ${cacheKey}`);
        parent = `dryrun:${cacheKey}`;
        this.folderCache.set(cacheKey, parent);
        continue;
      }
      const res = await this.drive.files.create({
        requestBody: { name, mimeType: FOLDER_MIME, parents: [parent] },
        fields: 'id',
      });
      const id = res.data.id!;
      this.folderCache.set(cacheKey, id);
      parent = id;
    }
    return parent;
  }

  /** True move: detach from current parents, attach to target. */
  async moveFile(file: DriveFile, toFolderId: string, toPathLabel: string): Promise<void> {
    if (file.parents?.includes(toFolderId)) return; // already there
    if (!this.commit || toFolderId.startsWith('dryrun:')) {
      console.log(`[dry-run] move "${file.name}" → ${toPathLabel}`);
      return;
    }
    await this.drive.files.update({
      fileId: file.id,
      addParents: toFolderId,
      removeParents: (file.parents ?? []).join(','),
      fields: 'id, parents',
    });
    console.log(`[move] "${file.name}" → ${toPathLabel}`);
  }

  async renameFile(file: DriveFile, newName: string): Promise<void> {
    if (file.name === newName) return;
    if (!this.commit) {
      console.log(`[dry-run] rename "${file.name}" → "${newName}"`);
      return;
    }
    await this.drive.files.update({ fileId: file.id, requestBody: { name: newName } });
    console.log(`[rename] "${file.name}" → "${newName}"`);
  }

  /** Reversible delete (Drive trash). */
  async trashFile(file: DriveFile, reason: string): Promise<void> {
    if (!this.commit) {
      console.log(`[dry-run] trash "${file.name}" (${reason})`);
      return;
    }
    await this.drive.files.update({ fileId: file.id, requestBody: { trashed: true } });
    console.log(`[trash] "${file.name}" (${reason})`);
  }

  private async findFolder(name: string, parentId: string): Promise<string | undefined> {
    const res = await this.drive.files.list({
      q:
        `'${parentId}' in parents and mimeType = '${FOLDER_MIME}' and ` +
        `name = '${name.replace(/'/g, "\\'")}' and trashed = false`,
      fields: 'files(id)',
      pageSize: 1,
    });
    return res.data.files?.[0]?.id ?? undefined;
  }
}

function required(name: string): string {
  const v = process.env[name];
  if (!v) throw new Error(`Missing env ${name} (Google OAuth). Set it in .env.local.`);
  return v;
}
