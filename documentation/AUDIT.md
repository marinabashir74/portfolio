# Marina Bashir — Current Site Audit & Redesign Rationale

Reference reviewed on 24 October 2026: https://marinabashir.netlify.app/

## Executive verdict

The existing portfolio has useful substance (a defined combination of social media management and AI-assisted video production; three named projects; direct contacts), but its design follows a generic dark, glass-card SaaS template. The gap is *proof*. The site says more about tools and ambitions than it shows of Marina's actual output, decision-making and outcomes.

The replacement is an original editorial-style creative portfolio. Its goal is differentiation, trust and inquiry conversion, not decoration alone. It deliberately does **not** clone the Behance portfolio that inspired the initial direction.

## Important findings

| Category | Existing implementation | Consequence | Redesign decision |
|---|---|---|---|
| Positioning | 'Engineering High-Retention AI Content & Organic Brand Growth' and numerous technical buzzwords | Feels like product copy instead of a person with judgment and taste | Human-first framing: what she makes, why people care, and the kinds of work she does |
| Visual identity | Dark indigo/cyan/purple glows, glass cards, icon grids | Common AI-generated site pattern; difficult to remember | Original ink/paper/coral/lime/cobalt editorial identity |
| Portfolio | Three mock-poster cards opening small text-only modals | Visitors cannot inspect live work, decisions, role or evidence | Dedicated, navigable case-study pages with evidence slots |
| Real media | No actual image or playable video URLs found in HTML; avatar img has empty `src` | Weakest possible proof for a video/content specialist | Original concept artwork used transparently until approved media arrives |
| Metrics | 20K+ community and +40% YoY revenue are claimed without shown measurement sources | Causal and evidentiary ambiguity | Keep as previously reported, clearly flag verification and attribution |
| Form | Submitting announces inquiry captured then opens a generic WhatsApp link without encoding entered fields | Misleading user feedback; inquiry may never be sent | Real Netlify HTML form + direct email/WhatsApp contact paths |
| Admin | Public browser UI edits and profile photo saved in `localStorage` | Only the visitor's browser is changed, not the website served to everyone | Remove misleading admin; use site files for prototype and recommend proper CMS later |
| Tech | Single HTML document, Tailwind browser CDN, Font Awesome CDN and inline JavaScript | Unstructured, difficult to maintain and tune | Clean, small, static HTML/CSS/JS files; local vector assets; no app framework |
| Accessibility | Showcase uses click handlers attached to divs | Keyboard users cannot predictably open work | Semantic anchors, accessible menu and filter buttons, reduced-motion support |
| Navigation | One-page site with section jumps only | No dedicated pages for search or prospect sharing | Individual URL per case study and a direct project inquiry page |
| Proof hierarchy | Tool stack and claims placed before substantial work | Credibility relies on assertions | Work up front; clear role/scope, selected outcomes and evidence needs |

## Design system

- Visual direction: 'The Social Studio' — bold, optimistic, human, editorial and digitally native.
- Colors: paper #F7F6F0, ink #1C2521, coral #FF6148, acid lime #E5FF70, blue #424BD6.
- Type: DM Sans for clarity; Instrument Serif for expressive emphasis. Both are served from Google Fonts with local font fallbacks; no font files are redistributed.
- Rhythm: fluid typographic scales, generous whitespace, strong section contrast and asymmetrical grids.
- Motion: one subtle infinite marquee, hover transforms and scroll reveals, all respecting reduced-motion preferences.
- Navigation: selected work → services → process → evidence → about → contact.
- Editorial principle: distinguish real media, conceptual artwork and unverified results.

## What cannot honestly be claimed yet

No external analytics, client briefs, original raw videos, campaign visuals, ad accounts or source permissions have been shared. This prototype cannot prove the original growth numbers or replace those source materials. Its illustrations are created for presentation only, **not genuine outputs from the featured client campaigns**.

## Why this is a better base

The new architecture allows rich proof and genuine stories to be inserted without rebuilding the layout. Case studies have their own URLs, each page has a working next-project navigation, and the site can deploy as plain static files. It is ready to mature into a portfolio that could compete visually, but awards and business outcomes depend on genuine creative artifacts and thoughtful execution beyond this prototype.
