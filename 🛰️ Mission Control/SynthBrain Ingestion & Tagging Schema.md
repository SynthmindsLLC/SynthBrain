---
created: 2026-05-24
updated: 2026-05-24
tags:
  - infrastructure
  - ingestion
  - mem-ai
  - tagging
  - automation
type: Documentation
subtype: Schema
---

# SynthBrain Ingestion & Tagging Schema

## Overview

All documents flow into **Mem.ai** as the single source of truth. Claude reads documents from connected sources (Gmail, Google Drive, local filesystem), auto-classifies them, applies the tagging schema, and pushes them to Mem.ai with the correct collection and inline tags. The SynthBrain git repo serves as a versioned backup.

---

## Collections

Collections in Mem.ai mirror the SynthBrain vault structure. Create these once, then reference by ID when ingesting.

| Collection | Maps To | What Goes Here |
|-----------|---------|---------------|
| **Work** | `00 - ⚙ Work/` | Client projects, deliverables, proposals, SOWs |
| **Commercial Hub** | `01 - 🎥 Commercial Hub/` | YouTube content, Synaptic Labs, content workflows |
| **Learning Lab** | `02 - 🧙 Learning Lab/` | Courses, tutorials, walkthroughs, certifications |
| **R&D** | `03 - 🔬 R&D/` | AI research, papers, tech explorations, experiments |
| **Prompts** | `04 - 🤖 Prompts/` | Prompt templates, prompt engineering, GPTs |
| **Organization** | `05 - 🌐 Organization/` | Team coordination, partnerships, hiring, admin |
| **Workshop** | `🛠 The Workshop/` | Tools docs, programming references, technical guides |
| **Mission Control** | `🛰️ Mission Control/` | Strategic projects, roadmaps, templates, session logs |
| **PBTV** | `00 - ⚙ Work/Clients/PBTV/` | All Plants by the Village project docs |
| **Inbox** | _(no vault equivalent)_ | Unsorted items pending classification |

---

## Tagging Taxonomy

Tags are applied as inline `#tags` in Mem.ai note content. Use the **first line** of the note as the title.

### Document Type Tags

| Tag | When to Use |
|-----|------------|
| `#meeting-notes` | Meeting transcripts, summaries, action items |
| `#documentation` | Reference docs, guides, how-tos, READMEs |
| `#decision` | Decision records, architecture decisions, strategy choices |
| `#research` | Papers, analysis, explorations, deep dives |
| `#proposal` | Proposals, pitches, SOWs, project scopes |
| `#email` | Ingested emails, email threads |
| `#reference` | Quick reference cards, cheat sheets, lookups |
| `#template` | Reusable templates and frameworks |
| `#log` | Session logs, changelogs, activity logs |
| `#financial` | Invoices, budgets, expenses, tax docs |
| `#creative` | Content drafts, scripts, storyboards, copy |
| `#code` | Code snippets, configs, technical implementations |

### Source Tags

| Tag | Source |
|-----|-------|
| `#from-gmail` | Ingested from Gmail |
| `#from-gdrive` | Ingested from Google Drive |
| `#from-local` | Ingested from local filesystem |
| `#from-slack` | Ingested from Slack |
| `#from-notion` | Ingested from Notion |
| `#from-granola` | Ingested from Granola meeting notes |
| `#from-web` | Ingested from web page / Exa search |
| `#from-manual` | Manually created or dictated |

### Project Tags

| Tag | Project |
|-----|---------|
| `#pbtv` | Plants by the Village |
| `#synthminds` | Synthminds internal |
| `#synaptic-labs` | Synaptic Labs / YouTube |
| `#verizon` | Verizon AI Literacy |
| `#yu` | Yeshiva University |
| `#anvl` | ANVL project |
| `#synthsidian` | Synthsidian product |

### Status Tags

| Tag | Meaning |
|-----|---------|
| `#active` | Currently being worked on |
| `#draft` | Work in progress, not finalized |
| `#review` | Needs review or approval |
| `#archived` | Completed, kept for reference |
| `#action-required` | Has pending action items |

### Priority Tags

| Tag | When |
|-----|------|
| `#urgent` | Needs attention today |
| `#high-priority` | This week |
| `#low-priority` | When time permits |

---

## Classification Rules

When ingesting a document, Claude applies these rules in order:

### 1. Determine Collection

| If the document... | Collection |
|---|---|
| Is about a specific client project | **Work** (or client sub-collection like **PBTV**) |
| Is a YouTube script, video plan, or content workflow | **Commercial Hub** |
| Is course material, learning notes, or a tutorial | **Learning Lab** |
| Is a research paper, AI concept, or technical exploration | **R&D** |
| Is a prompt template or GPT configuration | **Prompts** |
| Is about team ops, hiring, partnerships, admin | **Organization** |
| Is tool documentation or a programming reference | **Workshop** |
| Is a project plan, roadmap, template, or session log | **Mission Control** |
| Cannot be classified confidently | **Inbox** |

### 2. Apply Tags

Always apply exactly:
- **1 document type tag** (the primary type)
- **1 source tag** (where it came from)
- **0-2 project tags** (if project-specific)
- **0-1 status tags** (if status is clear)
- **0-1 priority tags** (only if urgency is explicit)

### 3. Format the Note

```markdown
# [Document Title]

#[type-tag] #[source-tag] #[project-tag] #[status-tag]

[Document content in markdown...]

---
*Ingested: [ISO 8601 timestamp] | Source: [source path or URL]*
```

---

## Ingestion Pipelines

### Pipeline 1: Gmail → Mem.ai

**Trigger:** Manual or scheduled scan
**MCP Tools:** Gmail (`gmail_search_messages`, `gmail_read_thread`) → Mem.ai (`create_note`)

1. Search Gmail for unread or starred messages matching filter criteria
2. Read the full thread
3. Classify: type = `#email`, source = `#from-gmail`
4. Determine collection and project tags from subject/sender/content
5. Create note in Mem.ai with extracted content, applied tags, and collection ID
6. Format: subject as title, thread content as body, participants listed

### Pipeline 2: Google Drive → Mem.ai

**Trigger:** Manual or scheduled scan
**MCP Tools:** Google Drive (`search`, `readGoogleDoc`, `getGoogleSheetContent`) → Mem.ai (`create_note`)

1. Search Drive for recently modified files (last 24h or since last scan)
2. Read content as markdown (Docs auto-convert)
3. Classify based on file location, name, and content
4. Apply tags and determine collection
5. Create note in Mem.ai
6. Track ingested file IDs to avoid duplicates

### Pipeline 3: Local Filesystem → Mem.ai

**Trigger:** Manual scan of specified directories
**MCP Tools:** Filesystem (`read_text_file`, `list_directory`) → Mem.ai (`create_note`)

1. Scan designated local directories for new/modified `.md`, `.txt`, `.pdf` files
2. Read content
3. If file has YAML frontmatter, extract existing tags and metadata
4. Classify and apply schema tags
5. Create note in Mem.ai
6. Log ingested files to avoid re-processing

### Pipeline 4: Meeting Notes → Mem.ai

**Trigger:** After meetings
**MCP Tools:** Granola (`get_meeting_transcript`) → Mem.ai (`create_note`)

1. Pull latest meeting transcript from Granola
2. Extract: attendees, agenda, decisions, action items
3. Tag: `#meeting-notes`, `#from-granola`, project tag from context
4. Create structured note with sections: Summary, Decisions, Action Items, Raw Transcript
5. Collection: determined by meeting context (client = Work, internal = Organization)

---

## Duplicate Prevention

Track ingested documents using the Memory MCP knowledge graph:

```
Entity: "ingested-doc"
Observations:
  - "gmail:thread-id-abc123 → mem:note-id-xyz | 2026-05-24T10:00:00Z"
  - "gdrive:file-id-def456 → mem:note-id-uvw | 2026-05-24T11:00:00Z"
```

Before ingesting, check if the source ID already exists in the knowledge graph.

---

## Connected Sources

### Active Now

| Source | MCP Server | Status |
|--------|-----------|--------|
| Gmail | Web UI (OAuth) | Connected |
| Google Drive | CLI (`@piotr-agier/google-drive-mcp`) | Needs OAuth setup |
| Local Filesystem | CLI (`@modelcontextprotocol/server-filesystem`) | Ready |
| Granola | Web UI (OAuth) | Connected |
| Notion | Web UI (OAuth) | Connected |
| Slack | Web UI (OAuth) | Connected |

### Future Expansion

| Source | MCP Server | When |
|--------|-----------|------|
| Microsoft 365 | `@softeria/ms-365-mcp-server` (200+ tools) | When M365 access is needed |
| Box | `box-mcp-server` | When Box integration is needed |
| Google Shared Drives | Same as Google Drive MCP | Included in current setup |

---

## Google Drive OAuth Setup

One-time setup to connect the Google Drive MCP:

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create or select a project
3. Enable APIs: Drive, Docs, Sheets, Slides, Calendar
4. Create OAuth 2.0 credentials (Desktop app type)
5. Download the JSON key file
6. Save to `~/.config/google-drive-mcp/gcp-oauth.keys.json`
7. Set env var: `export GOOGLE_DRIVE_OAUTH_CREDENTIALS="~/.config/google-drive-mcp/gcp-oauth.keys.json"`
8. On first run, the MCP server opens a browser for OAuth consent
