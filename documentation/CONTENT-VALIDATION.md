# Content verification, client approvals & launch blockers

This is a design and content structure prototype. It preserves project names and previously reported figures from Marina's existing publicly accessible site, but it has not independently confirmed the underlying work or outcomes.

## Priority 0 — needed before professional public launch

- [ ] Obtain Marina's own portrait and a short, personally written introduction.
- [ ] Verify that the project names, client affiliations, roles and confidentiality allowances are accurate.
- [ ] Replace editorial case-study artwork with approved examples of her actual campaigns, posts, video and final output. Keep artwork only as clearly marked decorative material.
- [ ] Confirm reported **20K+ community scaled**: which platform/account, initial audience, final audience, period, organic/paid split and Marina's contribution.
- [ ] Confirm reported **+40% year-over-year revenue**: source, dates, baseline and whether marketing contribution can be established. Revenue movement alone does not prove campaign causation.
- [ ] Review case-study narrative with Marina. Sections titled 'The opportunity' and 'Ideas in motion' are plausible editorial reconstructions based on the prior site—not independently established historical project records.
- [ ] Add the actual playable Alphabet Safari video (or other strongest approved AI video) plus credits, music/voice permissions and accessibility captions.
- [ ] Check Marina's current availability and preferred contact email/number and whether WhatsApp inquiries are wanted.
- [ ] Configure Netlify Forms notifications and test one real inquiry on deployment; also test direct email and WhatsApp links.

## Priority 1 — strongly recommended

- [ ] Add 2–3 detailed approved project outcome snapshots (date, baseline, approach, results, what was learned).
- [ ] Obtain permission for brand logos, client screenshots and social posts.
- [ ] Add concise testimonials only if written permission and verbatim wording are available.
- [ ] Make a short original reel/showreel with real work; include clickable play and full video controls.
- [ ] Customize page-specific SEO/social previews.
- [ ] Add privacy/consent disclosure appropriate to the geographic audience and any analytics/contact integrations.
- [ ] Run Lighthouse and manual browser tests on the deployed Netlify URL after adding actual media.

## Editorial tone

Prefer concrete actions and thoughtful language over speculative language like 'viral guarantees', 'algorithmic trend-hijacking', '10x brand presence' or 'engineered for retention' unless justified by verified evidence.

## Adding authentic work

The source is intentionally simple: replace `assets/*-cover.svg` with allowed visuals and change the three homepage `<img>` paths; update the project content in `generate_cases.py`, then run `python generate_cases.py` to regenerate each case page. If the old drawings are not used, remove the illustration disclosures from their corresponding pages and the homepage only after genuine media replaces them.
