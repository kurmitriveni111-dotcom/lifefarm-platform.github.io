# LIFEFARM 3.0 — Simple Static Edition

A ready-to-import, static LIFEFARM website for GitHub Pages, with optional Vercel preview deployment. It has no database, no backend server, no OAuth, no SMTP, no Blob store and no external API requirement.

## Included and working

- LIFEFARM institutional homepage and ARENA organization overview.
- ARENA hierarchy, five foundation levels, seven seals and eleven branches.
- Responsive mobile-first layout.
- Public Field Notes / publications loaded from `content/articles.json`.
- Public image gallery loaded from `content/gallery.json`.
- Browser-based Content Studio (`editor.html`) to create, edit, delete and export publication JSON and gallery JSON.
- Participation Card generator with random local reference ID, SVG download and print.
- Local policy acknowledgement, language metadata selector, command navigator and knowledge quiz.
- Local browser data export and restore.
- Terms, Privacy, Community, Copyright and operator-information policy page.
- PWA manifest, offline shell and service worker.
- GitHub Actions deployment workflow for GitHub Pages.
- Optional Vercel static preview configuration.

## Important design boundary

This edition is intentionally static. It does **not** claim to provide centrally verified member accounts, secure login, globally unique Member Keys, private cloud storage, multi-user Social likes/comments, private member records or server-verified consent. The participation card is a local display card only. Local browser data does not synchronize across devices. The Content Studio exports files; publishing still requires a GitHub repository collaborator to commit those files.

These boundaries are deliberate: secure shared accounts and private multi-user data require a backend service. A static website cannot safely provide those functions by hiding passwords in browser code or local storage.

## Publish on GitHub Pages (Android or PC)

1. Download and extract this ZIP.
2. Open GitHub and create a repository named `lifefarm-platform`.
3. Upload the **contents** of this folder to the repository root. The `.github/workflows/pages.yml` file must be included. If Android file picker hides dot-folders, use GitHub's web upload or GitHub Desktop on a computer so the workflow folder is preserved.
4. In repository **Settings → Pages**, set the source to **GitHub Actions**.
5. Open **Actions** and wait for `Deploy LIFEFARM to GitHub Pages` to finish successfully.
6. Open the Pages URL shown in the workflow. It will usually look like `https://YOUR-USERNAME.github.io/lifefarm-platform/`.
7. Make future changes by editing files in GitHub and committing them to `main`. The workflow deploys automatically.

Do not put passwords, private identity documents, API tokens or private member data in a public repository.

## Optional Vercel preview

1. Sign in to Vercel with GitHub.
2. Import the same repository as a static project.
3. Do not add environment variables, databases, OAuth credentials or storage tokens. There is no backend in this edition.
4. Keep Vercel use within the plan's applicable terms. The public GitHub Pages site remains the primary deployment.

## Publish a Field Note

1. Open `editor.html` on the deployed site or locally.
2. Load the current `content/articles.json` file.
3. Create or edit the article. Use plain text with line breaks.
4. Click **Download updated articles.json**.
5. In GitHub, replace `content/articles.json` with the downloaded file and commit.
6. If using a cover image, upload the image to `assets/uploads/` in GitHub and use a relative path such as `./assets/uploads/soil-restoration.webp` in the article.
7. Wait for GitHub Pages deployment. The article appears in Field Notes.

The Content Studio is a file generator, not a private admin panel. GitHub repository permissions control who can publish.

## Manage the public image gallery

1. Upload images to `assets/uploads/` in GitHub.
2. Open `editor.html` and load the current `content/gallery.json`.
3. Add the image title, relative image path, alternative text and caption.
4. Export `gallery.json`, replace `content/gallery.json` in GitHub and commit.
5. The gallery appears on the public homepage after deployment.

## Backup and restore

- The entire website is backed up by its GitHub repository and commit history.
- Periodically download a ZIP of the repository using GitHub's **Code → Download ZIP**.
- To back up locally saved participation-card and preference data, use **Tools → Local Backup → Export** on the device where it was created.
- Restore local data with the **Restore** button. This only restores browser-local settings, not the website's articles.
- To restore the website, upload a known-good repository version or revert the relevant Git commit.

## Folder structure

```
index.html                 Main public website
editor.html                Local publication file editor
legal.html                 Terms, Privacy and Community policies
content/articles.json      Public articles collection
content/gallery.json       Reserved public gallery manifest
assets/js/site.js          Website functionality
assets/js/editor.js        Content Studio functionality
assets/css/editor.css      Content Studio styles
assets/icons/icon.svg      Website icon
sw.js                      Offline service worker
manifest.webmanifest       PWA settings
.github/workflows/pages.yml GitHub Pages deployment
vercel.json                Optional static Vercel settings
```

## Before public launch

- Review and complete all operator placeholders in `legal.html`.
- Confirm the real legal identity and registration status; do not claim an unregistered legal structure.
- Review privacy and copyright terms with a qualified professional for the actual activity.
- Review all content and images for rights and personal information.
- Keep repository write access limited to trusted people.
- Test the published site on Android and desktop.
- Test article publishing, local card generation, SVG download, print, backup and restore.

## Verification

Run `python3 scripts/check_site.py` from this folder. The script validates required files, JSON, internal relative links, deployment workflow presence and basic static-site restrictions. This package has no npm dependencies or build step. Actual GitHub/Vercel account deployment must still be completed by the repository owner.
