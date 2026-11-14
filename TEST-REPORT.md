# Build and static verification report

This report describes checks run on the generated source package. It does not claim a live deployment or browser/device certification.

Checks to run:
- `python3 scripts/check_site.py` — required files, JSON validity, relative links, GitHub workflow and static-only checks.
- Test the GitHub Actions deployment after import.
- Test Content Studio import/export and a publication update on the deployed site.
- Test participation card generation, SVG download, print and local backup/restore on Android and desktop.

Not performed by this package generator:
- A live GitHub Pages deployment under the user's account.
- A live Vercel deployment.
- Device testing on the user's exact browser/device.
- Legal review or confirmation of operator placeholders.

No source package can guarantee zero issues in every hosting account or browser. The package avoids server-side dependencies and includes automated static checks to make setup straightforward.
