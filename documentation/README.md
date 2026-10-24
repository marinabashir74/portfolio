# Marina Bashir — The Social Studio

An original responsive portfolio redesign prototype for **Marina Bashir**, based on the public content of https://marinabashir.netlify.app/ and inspired by expressive editorial portfolio design.

**Status:** Finished functional prototype — **not a final client-approved or evidence-verified publication**.

## Explore

Open `index.html` to preview the landing page. Internal pages:

- `work/gloria-cup.html` — social management and community growth
- `work/furniture-corner.html` — campaigns and commerce
- `work/alphabet-jungle.html` — AI-assisted children's video
- `contact.html` — Netlify-compatible project inquiry + direct contact links
- `success.html` — contact form confirmation page
- `404.html` — not found page

The `site/` folder in the downloadable package contains a **deployment-ready copy**. The package also includes `documentation/` and `previews/`.

## Production deployment — Netlify

1. Deploy the `site/` folder to an existing or new Netlify site via Netlify's deploy UI (or your usual Git workflow). It's pure static HTML/CSS/JS with no build command.
2. If retaining Marina's existing domain, deploy to the current site only after keeping a backup of the old version.
3. In Netlify's dashboard, confirm the `project-inquiry` form is detected. Enable form submissions/notifications according to the account settings.
4. Submit a real test message on the deployed URL, confirm success page and confirm the notification/submission actually arrived. This form **does not send email in a local file preview**.
5. Validate the contact destinations, page links, SEO previews, privacy and mobile experience.

### How to replace artwork and text

- Brand tokens are in `styles.css`, under `:root`.
- Hero, portfolio and contact copy are in `index.html`.
- Case-study content is in `generate_cases.py`: update the `CASES` data and run `python generate_cases.py` to regenerate `/work/` pages.
- Assets are in `assets/`; see `ASSET-SPEC.md` for replacement export sizes.
- Direct email and WhatsApp links are visible in HTML. Replace if Marina's preferred contacts have changed.
- No public 'admin' panel is included; the prior localStorage-only mechanism did not change the shared live site. For ongoing client self-service editing, add a proper authenticated CMS as a separate phase.

## Technical choices

- Static semantic HTML, hand-authored CSS with fluid typography and responsive layout, lightweight vanilla JavaScript.
- No Tailwind browser CDN, unnecessary application framework or simulated CMS.
- Real links, project filters and mobile navigation; keyboard-visible focus and reduced-motion support.
- Netlify Forms using a standard HTML POST, Netlify honeypot, hidden form-name field and a real post-submit page.
- Local original SVG artwork, 1200x630 OG social preview PNG, sitemap/robots, 404 and security headers.
- Google Fonts CSS for DM Sans and Instrument Serif; system fonts provide a fallback if the font CDN isn't available.

## Honesty about client work

The three client/project names and the reported 20K+/40% figures originate from Marina's existing portfolio. **They have not been verified independently.** The beautiful images included in this package are **concept illustrations made for this prototype**, not actual Gloria Cup, Furniture Corner or Alphabet Safari client assets. No third-party Behance panels were redistributed or embedded.

See `CONTENT-VALIDATION.md` and `AUDIT.md` before public use.
