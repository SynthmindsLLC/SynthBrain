[![](https://publish-01.obsidian.md/access/caa27d6312fe5c26ebc657cc609543be/Assets/obsidian-lockup-docs.svg)](https://docs.obsidian.md/Home)[Developer Documentation](https://docs.obsidian.md/Home)

Release your theme with GitHub Actions

Manually releasing your theme can be time-consuming and error-prone. In this guide, you'll configure your theme to use [GitHub Actions](https://github.com/features/actions) to automatically create a release when you create a new tag.

1.  In the root directory of your theme, create a file called `release.yml` under `.github/workflows` with the following content:
    
        name: Release Obsidian theme
        
        on:
          push:
            tags:
              - "*"
        
        jobs:
          build:
            runs-on: ubuntu-latest
        
            steps:
              - uses: actions/checkout@v3
        
              - name: Create release
                env:
                  GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
                run: |
                  tag="${GITHUB_REF#refs/tags/}"
        
                  gh release create "$tag" \
                    --title="$tag" \
                    --generate-notes \
                    --draft \
                    manifest.json theme.css
        
    
2.  In your terminal, commit the workflow.
    
        git add .github/workflows/release.yml
        git commit -m "Add release workflow"
        git push origin main
        
    
3.  Create a tag that matches the version in the `manifest.json` file.
    
        git tag -a 1.0.1 -m "1.0.1"
        git push origin 1.0.1
        
    
    *   `-a` creates an [annotated tag](https://git-scm.com/book/en/v2/Git-Basics-Tagging#_creating_tags).
    *   `-m` specifies the name of your release. For Obsidian plugins, this must be the same as the version.
4.  Browse to your repository on GitHub and select the **Actions** tab. Your workflow might still be running, or it might have finished already.
    
5.  When the workflow finishes, go back to the main page for your repository and select **Releases** in the sidebar on the right side. The workflow has created a draft GitHub release and uploaded the required assets as binary attachments.
    
6.  Select **Edit** (pencil icon) on the right side of the release name.
    
7.  Add release notes to let users know what happened in this release, and then select **Publish release**.
    

You've successfully set up your theme to automatically create a GitHub release whenever you create a new tag.

*   If this is the first release for this theme, you're now ready to [Submit your theme](https://docs.obsidian.md/Themes/App+themes/Submit+your+theme).
*   If this is an update to an already published theme, your users can now update to the latest version.

Release your theme with GitHub Actions

Not found

This page does not exist

Interactive graph

On this page

[Powered by Obsidian Publish](https://publish.obsidian.md)