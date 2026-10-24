from pathlib import Path
from html import escape

ROOT = Path(__file__).parent
SITE_DIR = ROOT.parent / 'site'

CASES = [
    dict(
        slug='gloria-cup',
        title='Gloria Cup',
        sub='Turning an everyday beverage brand into a 20K+ organic community and daily lifestyle ritual.',
        kind='Social Growth · Community Architecture',
        index='01',
        image='gloria-cover.svg',
        theme='gloria',
        role='Lead Social Media Strategist & Content Director',
        scope='Instagram Growth · Short-Form Reels · Community',
        year='20K+ Organic Community Scaled',
        brand='Gloria Cup (Beverage & Lifestyle)',
        challenge='Crowded beverage feeds fail when brands post static product shots with no human ritual attached. The opportunity for Gloria Cup was to become a familiar, craveable part of the audience’s daily routine—turning passive scrollers into an active, returning community.',
        direction='I architected a lifestyle-first social growth engine built around relatable daily occasions, high-retention short-form Reels, and conversational caption frameworks—pairing visual feed cohesion with repeatable organic discovery hooks.',
        ideas=[
            'Mapped core daily moments and emotional triggers where the beverage naturally belongs in a customer’s day.',
            'Engineered repeatable short-form Reel formats (recipe rituals, sensory pours, lifestyle transitions) built for watch-time, saves, and shares.',
            'Established a warm, participatory caption voice and comment-to-DM loop to accelerate early-hour algorithmic reach.',
            'Used weekly Meta Business Suite retention and engagement signals to double down on winning creative pillars.'
        ],
        result='Scaled the brand’s organic Instagram community past 20,000+ engaged followers, establishing a recognizable lifestyle identity, higher save-to-impression ratios, and consistent inbound customer inquiries.',
        deliverables=[
            'End-to-End Instagram Strategy, Content Calendar & Grid Direction',
            'High-Retention Short-Form Reel Production & Hook Scripting (CapCut Pro, Canva, Figma)',
            'Active Community Nurturing & Micro-Influencer Collaboration Playbook',
            'Meta Business Suite Performance Tracking & Monthly Iteration'
        ],
        next='furniture-corner',
        next_title='Furniture Corner'
    ),
    dict(
        slug='furniture-corner',
        title='Furniture Corner',
        sub='Transforming static furniture listings into high-converting visual stories and +40% year-over-year commercial growth.',
        kind='Commercial Content · Meta Campaigns',
        index='02',
        image='furniture-cover.svg',
        theme='furniture',
        role='Performance Content Strategist & Meta Campaign Lead',
        scope='Visual Catalogs · Meta Ads · Conversion Copy',
        year='+40% YoY Revenue Expansion',
        brand='Furniture Corner (Retail & E-Commerce)',
        challenge='High-consideration home furniture never sells on specifications alone. Showing a chair or sofa in isolation is one thing; helping a buyer immediately picture how it transforms their living space—and giving them the confidence to inquire—is what drives revenue.',
        direction='I bridged the gap between editorial interior inspiration and direct-response commerce—rebuilding Furniture Corner’s visual catalog system and pairing it with targeted Meta Business Suite campaigns engineered to convert high-intent home buyers.',
        ideas=[
            'Redesigned product creative around real buyer decisions—room styling, dimensions, material texture, and spatial flow.',
            'Built scroll-stopping multi-slide carousels and staged video features that work seamlessly across organic feeds and paid placements.',
            'Structured full-funnel Meta Business Suite ad campaigns targeting active homeowners, movers, and interior shoppers.',
            'Optimized direct-response copy and WhatsApp/DM inquiry handoffs to shorten the path from first click to closed sale.'
        ],
        result='Drove a +40% year-over-year commercial revenue expansion through stronger catalog conversion rates, lower cost-per-inquiry on Meta placements, and higher-intent showroom and online orders.',
        deliverables=[
            'Conversion-Engineered Visual Product Catalogs & Carousel Systems',
            'Meta Business Suite Campaign Setup, Targeting & Creative A/B Testing',
            'Direct-Response Sales Copywriting & WhatsApp/DM Inquiry Funnel',
            'Monthly Commercial Attribution & Merchandising Optimization'
        ],
        next='alphabet-jungle',
        next_title='Alphabet Jungle Safari'
    ),
    dict(
        slug='alphabet-jungle',
        title='Alphabet Jungle Safari',
        sub='Studio-grade 3D character consistency and generative AI motion—proving what is possible with a disciplined multi-tool AI video pipeline.',
        kind='AI Video Studio · 3D Character Pipeline',
        index='03',
        image='alphabet-cover.svg',
        theme='alphabet',
        role='AI Video Director & Generative Pipeline Architect',
        scope='Midjourney · Kling AI · Runway Gen-3 · ElevenLabs',
        year='100% Generative AI Studio Pipeline',
        brand='3D Animated Series & AI Production Showcase',
        challenge='Most AI-generated video fails commercially because characters morph from shot to shot, motion feels random, and audio lacks emotional timing. Whether producing a children’s edutainment series or a branded 3D mascot campaign for an international agency, commercial work requires strict visual continuity and narrative control.',
        direction='I engineered an end-to-end 3D generative production pipeline for Alphabet Jungle Safari—combining locked character model sheets with controlled camera kinematics, expressive vocal synthesis, and retention-driven editorial pacing.',
        ideas=[
            'Built multi-angle 3D character model sheets and locked color/lighting bibles in Midjourney so characters remain 100% recognizable across every scene.',
            'Directed purposeful character kinematics and smooth camera motion using Kling AI and Runway Gen-3, eliminating temporal distortion.',
            'Engineered expressive voiceovers, rhythmic phonics hooks, and layered foley sound design using ElevenLabs and CapCut Pro.',
            'Structured scene pacing and visual hooks around YouTube Studio retention curves to capture attention in the first 5 seconds and hold viewers to completion.'
        ],
        result='A repeatable, studio-grade AI animation workflow that delivers the warmth and character consistency of traditional 3D production at a fraction of conventional timelines—ready for branded mascots, AI commercials, and scalable YouTube IP channels.',
        deliverables=[
            '3D Character Bible & Multi-Scene Prompt Architecture (Midjourney)',
            'Generative Motion Direction & Camera Kinematics (Kling AI & Runway Gen-3)',
            'Vocal Synthesis, Lip-Sync & Foley Sound Design (ElevenLabs & CapCut Pro)',
            'High-CTR Thumbnail Design & YouTube Studio SEO Architecture'
        ],
        next='gloria-cup',
        next_title='Gloria Cup'
    )
]

HEAD = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#f7f6f0"><meta name="description" content="{desc}"><meta property="og:title" content="{title} — Marina Bashir"><meta property="og:description" content="{desc}"><meta property="og:image" content="https://marinabashir.netlify.app/assets/og-cover.png"><link rel="icon" href="../assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="../styles.css"><script defer src="../main.js"></script><title>{title} — Case Study | Marina Bashir</title></head>'''

NAV = '''<a class="skip-link" href="#main">Skip to content</a><header class="site-header"><div class="header-inner container"><a href="../index.html" class="brand"><span class="brand-mark" aria-hidden="true">mb.</span><span>marina bashir<em> / studio</em></span></a><nav class="header-links" aria-label="Main navigation"><a href="../index.html#work">Selected work</a><a href="../index.html#expertise">Expertise</a><a href="../index.html#packages">Packages</a><a href="../index.html#about">About</a><a href="../index.html#contact">Contact</a></nav><div class="header-action"><span class="availability">Available for global retainers</span><a class="header-cta" href="../contact.html">Book a project ↗</a><button type="button" class="menu-button" data-menu-button aria-expanded="false" aria-controls="mobile-nav">Menu ☰</button></div></div><nav id="mobile-nav" class="mobile-panel" data-mobile-panel aria-label="Mobile navigation"><a href="../index.html#work">Selected work ↗</a><a href="../index.html#expertise">Expertise ↗</a><a href="../index.html#packages">Packages ↗</a><a href="../index.html#about">About ↗</a><a href="../index.html#contact">Contact ↗</a></nav></header>'''

FOOT = '''<footer class="footer"><div class="container"><div class="footer-inner"><a href="../index.html" class="brand"><span class="brand-mark" aria-hidden="true">mb.</span><span>marina bashir</span></a><span>AI-Powered Social Growth &amp; Creative Video Studio. © 2026 Marina Bashir.</span><div class="footer-links"><a href="mailto:marinabashir74@gmail.com">Email ↗</a><a href="https://wa.me/923024292224" target="_blank" rel="noopener noreferrer">WhatsApp ↗</a><a href="https://linkedin.com/in/marina-bashir-a356641b5" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a></div></div><p class="footer-bottom">Lahore, Pakistan · Serving brands, founders &amp; agencies worldwide.</p></div></footer>'''

out_dir = SITE_DIR / 'work'
out_dir.mkdir(parents=True, exist_ok=True)

for c in CASES:
    desc = escape(c['sub'], quote=True)
    head = HEAD.format(desc=desc, title=escape(c['title']))
    bullets = ''.join('<li>' + escape(b) + '</li>' for b in c['ideas'])
    deliverables = ''.join('<li>' + escape(b) + '</li>' for b in c['deliverables'])
    html = (
        head
        + f'''<body class="case-page--{c['theme']}">{NAV}<main id="main"><section class="case-header"><div class="container"><div class="case-breadcrumb"><a href="../index.html">Home</a><span> / </span><a href="../index.html#work">Selected work</a><span> / </span>{escape(c['title'])}</div><div class="case-kicker">{escape(c['index'])} / {escape(c['kind'])}</div><h1 class="display case-title">{escape(c['title'])}<span style="color:var(--coral)">.</span></h1><p class="case-subtitle">{escape(c['sub'])}</p></div></section><div class="container"><img class="case-art" src="../assets/{c['image']}" alt="{escape(c['title'])} case study visual cover" width="1200" height="1020"><div class="case-details"><div class="case-detail"><small>Client / Showcase</small><strong>{escape(c['brand'])}</strong></div><div class="case-detail"><small>Role</small><strong>{escape(c['role'])}</strong></div><div class="case-detail"><small>Core Stack &amp; Scope</small><strong>{escape(c['scope'])}</strong></div><div class="case-detail"><small>Key Highlight</small><strong>{escape(c['year'])}</strong></div></div></div><div class="container case-content"><section class="case-story"><h2>The challenge.</h2><div><p>{escape(c['challenge'])}</p></div></section><section class="case-story"><h2>Strategic direction.</h2><div><p>{escape(c['direction'])}</p></div></section><section class="case-story"><h2>Execution in motion.</h2><div><ul>{bullets}</ul></div></section><section class="case-story"><h2>Commercial impact.</h2><div><p>{escape(c['result'])}</p></div></section><section class="case-story"><h2>Deliverables &amp; stack.</h2><div><p>Core production capabilities and deliverables executed in this workflow:</p><ul>{deliverables}</ul></div></section><div class="case-follow"><div><div class="eyebrow">KEEP EXPLORING</div><h3>Up next: <span class="serif">{escape(c['next_title'])}</span></h3></div><a href="{c['next']}.html">View next story ↗</a></div></div><section class="contact-section"><div class="container"><div class="section-kicker">WANT RESULTS LIKE THIS?</div><h2 class="display" style="font-size:clamp(67px,10vw,145px)">Let's <span class="serif">build it.</span></h2><div class="contact-buttons" style="margin-top:28px"><a class="button" href="../contact.html">Book a project or retainer ↗</a><a class="button button--outline" href="https://wa.me/923024292224?text=Hi%20Marina%2C%20I%20saw%20your%20{escape(c['title'])}%20case%20study%20and%20would%20love%20to%20chat." target="_blank" rel="noopener noreferrer">Chat on WhatsApp ↗</a></div></div></section></main>{FOOT}</body></html>'''
    )
    (out_dir / f"{c['slug']}.html").write_text(html, encoding='utf-8')

print('Generated', len(CASES), 'case study pages in', out_dir)
