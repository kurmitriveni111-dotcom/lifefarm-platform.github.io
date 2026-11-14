# Android publishing guide

## Upload the site
1. Extract the ZIP using My Files.
2. In GitHub app or Chrome, create `lifefarm-platform`.
3. For a reliable first upload, use GitHub in Chrome desktop-site mode or a computer. Upload all files and folders at the repository root. Preserve `.github/workflows/pages.yml`.
4. Choose Settings → Pages → GitHub Actions.
5. In Actions, open the latest workflow and wait for both build and deploy jobs to pass.
6. Use the `github-pages` environment URL to open the website.

## Publish an article
1. Open the deployed `editor.html`.
2. Load `content/articles.json` from your repository onto the phone.
3. Add/edit articles and export the updated file.
4. In GitHub, open `content/articles.json`, replace its contents with the downloaded JSON, and commit to `main`.
5. Wait for the automatic deployment and refresh the public site.

## Upload a cover image
1. Upload the image to `assets/uploads/` in GitHub (create the folder if needed).
2. In the Content Studio, set cover path to `./assets/uploads/filename.webp`.
3. Export and publish `articles.json`.

## Important
The Content Studio is not a secure login dashboard. It only creates content files in the browser. GitHub permissions control publishing. Do not publish private member data, passwords or secret keys.

## Publish gallery images
1. Upload each image to `assets/uploads/` in GitHub.
2. Open `editor.html`, load `content/gallery.json`, and add an entry with a path such as `./assets/uploads/field-work.webp`.
3. Export `gallery.json`, replace `content/gallery.json` in GitHub and commit.
4. Wait for deployment and check the Gallery section.
