# What changed from the previous server-based LIFEFARM package

The previous Vercel platform required PostgreSQL, private/public Blob stores, GitHub OAuth, SMTP and server environment variables. This edition removes those service dependencies and is a static website.

| Previous component | Simple replacement |
|---|---|
| PostgreSQL and migrations | Static JSON content files in the GitHub repository |
| GitHub OAuth admin login | GitHub repository collaborator permissions |
| CMS backend | Browser Content Studio that exports JSON files for commit |
| Public Blob media | Images stored in `assets/uploads/` in the repository |
| Private Blob member storage | Removed; no private member storage in static edition |
| Email verification/password reset | Removed; no member login in static edition |
| Member Key and secure account | Local participation card with clearly non-credential local reference |
| Social feed, likes, comments, private posts | Removed; public editorial content is managed as Field Notes |
| Server audit and consent records | Git commit history and local-only policy acknowledgement |
| Database backup | Git repository history and downloaded repository ZIP |

The replacements are intentionally honest about their scope. A static site cannot provide central member authentication, private user data, secure account recovery or a multi-user social feed. Reintroducing those functions later requires a backend and a proper security design.
