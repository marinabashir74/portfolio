# QA report — prototype checks (24 October 2026)

## Inspected

- Desktop 1440 × 900, mobile 390 × 844: rendered and visually inspected in headless Chromium using a Playwright inline-content harness.
- Responsive horizontal overflow check at widths: 320, 360, 375, 390, 768, 1024, 1280, 1440 and 1920 px — no horizontal document overflow was observed.
- Mobile navigation opens and closes, and sets appropriate `aria-expanded` state.
- Portfolio filters: 'AI motion' reduces three project cards to one; 'All' restores three.
- Case study 'Gloria Cup' renders with its correct primary heading.
- No JavaScript page errors in the tested homepage view.
- `prefers-reduced-motion` used in screenshot testing, covering the static fallback.
- Local SVG artworks render in the browser after forcing below-fold images to eager for full-page capture.

## Not yet tested or not assertable

- Netlify server-side form submission and notification delivery, which need a real Netlify deploy.
- Real production image/video loading and video accessibility, as real campaign media was not provided.
- Remote Google Fonts availability across browsers; fallbacks are supplied.
- Lighthouse, WebPageTest, keyboard-only full audit and screen-reader end-to-end audit on a deployed HTTPS instance.
- Publishing permissions, claims accuracy, consent and up-to-date contacts.

## Design QA changes made

- Reduced the hero display font scale and aligned copy nearer the top so the primary CTA appears in the initial desktop viewport.
- Confirmed artwork/typography/layout at mobile and desktop sizes.
- Identified that a naive CSS `@import` removal routine broke CSS custom properties in the *test harness*; corrected test harness so production CSS was actually evaluated. The production stylesheet itself did not have that issue.
