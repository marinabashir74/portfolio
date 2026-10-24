from pathlib import Path
from html import escape

ROOT = Path(__file__).parent
SITE_DIR = ROOT.parent / 'site'

GLORIA_SHOWCASE_HTML = '''
<div class="brand-bar">
  <div class="brand-bar-info">
    <img class="brand-bar-logo" src="../assets/gloria/gloria-logo.jpg" alt="Gloria Cup Cafe official logo" width="64" height="64">
    <div>
      <h2>Gloria Cup Café · <span style="color:var(--lime)">@gloriacupcafe</span></h2>
      <p>271-Block H-2 Top Roof, Johar Town (Opposite Emporium Mall), Lahore · Rooftop Dining, Coffee &amp; Live Match Screenings</p>
    </div>
  </div>
  <div class="brand-bar-actions">
    <a class="brand-bar-btn" href="https://www.instagram.com/gloriacupcafe/?hl=en" target="_blank" rel="noopener noreferrer">Visit @gloriacupcafe on Instagram ↗</a>
    <a class="brand-bar-btn brand-bar-btn--ghost" href="https://www.facebook.com/Gloriacupcafe/" target="_blank" rel="noopener noreferrer">Official Facebook ↗</a>
  </div>
</div>

<section class="media-showcase" aria-label="Gloria Cup Cafe Live Reels and Visual Content">
  <div class="media-showcase-head">
    <div>
      <div class="section-kicker" style="color:var(--lime)">LIVE CAMPAIGN REELS &amp; MEDIA</div>
      <h2>From the <span class="serif" style="color:var(--lime)">rooftop feed.</span></h2>
    </div>
    <a class="underline-link" style="color:var(--lime)" href="https://www.instagram.com/gloriacupcafe/?hl=en" target="_blank" rel="noopener noreferrer">Explore all 146+ posts &amp; reels on @gloriacupcafe ↗</a>
  </div>

  <div class="media-grid">
    <article class="media-card">
      <a class="media-card-thumb media-card-thumb--reel" href="https://www.facebook.com/reel/3239960226277686/" target="_blank" rel="noopener noreferrer" aria-label="Watch Gloria Cup Cafe vertical rooftop reel">
        <span class="media-pill">9:16 VERTICAL REEL · JOHAR TOWN ROOFTOP</span>
        <img src="../assets/gloria/gloria-reel-rooftop.jpg" alt="Gloria Cup Cafe rooftop food reel opposite Emporium Mall Lahore" loading="lazy">
        <div class="media-play-badge"><div class="media-play-circle">▶</div></div>
      </a>
      <div class="media-card-body">
        <h3>Rooftop Platter &amp; Ambiance Reel</h3>
        <p>Short-form vertical reel filmed on the Block H-2 rooftop overlooking Emporium Mall—showcasing loaded burgers, specialty pan pizza, and baked pasta to drive weekend foot traffic and DM bookings.</p>
        <div style="display:flex;gap:16px;flex-wrap:wrap">
          <a class="underline-link" style="color:var(--lime)" href="https://www.facebook.com/reel/3239960226277686/" target="_blank" rel="noopener noreferrer">Watch Full Reel ↗</a>
          <a class="underline-link" style="color:#fff" href="https://www.instagram.com/gloriacupcafe/?hl=en" target="_blank" rel="noopener noreferrer">View on @gloriacupcafe ↗</a>
        </div>
      </div>
    </article>

    <div class="media-stack-right">
      <article class="media-card">
        <a class="media-card-thumb media-card-thumb--video" href="https://www.instagram.com/gloriacupcafe/?hl=en" target="_blank" rel="noopener noreferrer">
          <span class="media-pill">SIGNATURE PLATTERS &amp; DEALS</span>
          <img src="../assets/gloria/gloria-deals-feature.jpg" alt="Gloria Cup Cafe amazing deals campaign cover" loading="lazy">
        </a>
        <div class="media-card-body">
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px">
            <img src="../assets/gloria/gloria-logo.jpg" alt="Gloria Cup Cafe logo" width="38" height="38" style="border-radius:50%;border:1.5px solid var(--lime)">
            <h3 style="margin:0">Signature Platter &amp; Creator Reels (@gloriacupcafe)</h3>
          </div>
          <p>High-retention short-form Reels and creator collaborations built around four repeatable pillars: <strong>Cappuccino &amp; Coffee Rituals</strong>, <strong>Desperado Steak &amp; Platter Deals</strong>, <strong>Live Cricket Match Rooftop Screenings</strong>, and <strong>Customer Story Reposts</strong>.</p>
          <a class="underline-link" style="color:var(--lime)" href="https://www.instagram.com/gloriacupcafe/?hl=en" target="_blank" rel="noopener noreferrer">Open @gloriacupcafe Instagram Feed ↗</a>
        </div>
      </article>
    </div>
  </div>
</section>
'''

FURNITURE_SHOWCASE_HTML = '''
<div class="brand-bar">
  <div class="brand-bar-info">
    <img class="brand-bar-logo" src="../assets/furniture/furniture-logo.jpg" alt="Furniture Corner official logo" width="64" height="64" style="background:#fff">
    <div>
      <h2>Furniture Corner · <span style="color:var(--lime)">@furniturecorner.pk</span></h2>
      <p>6 Block B1, PIA Road, Hakim Chowk, Lahore · Bespoke Luxury Dining, Bedroom, Sofa &amp; Interior Collections</p>
    </div>
  </div>
  <div class="brand-bar-actions">
    <a class="brand-bar-btn" href="https://www.instagram.com/furniturecorner.pk/?hl=en" target="_blank" rel="noopener noreferrer">Visit @furniturecorner.pk on Instagram ↗</a>
    <a class="brand-bar-btn brand-bar-btn--ghost" href="https://furniturecorner.pk/" target="_blank" rel="noopener noreferrer">furniturecorner.pk ↗</a>
  </div>
</div>

<section class="media-showcase" aria-label="Furniture Corner Live Reels and Luxury Catalog">
  <div class="media-showcase-head">
    <div>
      <div class="section-kicker" style="color:var(--lime)">SHORT-FORM REELS &amp; LAVISH CATALOG</div>
      <h2>Luxury in <span class="serif" style="color:var(--lime)">every frame.</span></h2>
    </div>
    <a class="underline-link" style="color:var(--lime)" href="https://www.instagram.com/furniturecorner.pk/?hl=en" target="_blank" rel="noopener noreferrer">Explore all 290+ posts &amp; reels on @furniturecorner.pk ↗</a>
  </div>

  <div class="media-grid">
    <article class="media-card">
      <a class="media-card-thumb media-card-thumb--reel" href="https://www.facebook.com/reel/1771560293769205/" target="_blank" rel="noopener noreferrer" aria-label="Watch Furniture Corner Fancy Bubble Bed Set Reel">
        <span class="media-pill">9:16 VERTICAL REEL · BOUCLÉ BED SET</span>
        <img src="../assets/furniture/fb_post1.jpg" alt="Furniture Corner Fancy Bubble Bed Set in Shiny Boucle Fabric Reel" loading="lazy">
        <div class="media-play-badge"><div class="media-play-circle">▶</div></div>
      </a>
      <div class="media-card-body">
        <h3>Fancy Bubble Bed Set · Bouclé Fabric Reel</h3>
        <p>Short-form vertical showroom reel highlighting the plush channel-tufted bouclé silhouette, matching vanity console, and warm ambient lighting—driving direct WhatsApp price inquiries.</p>
        <div style="display:flex;gap:16px;flex-wrap:wrap">
          <a class="underline-link" style="color:var(--lime)" href="https://www.facebook.com/reel/1771560293769205/" target="_blank" rel="noopener noreferrer">Watch Bed Set Reel ↗</a>
          <a class="underline-link" style="color:#fff" href="https://www.instagram.com/furniturecorner.pk/?hl=en" target="_blank" rel="noopener noreferrer">View on @furniturecorner.pk ↗</a>
        </div>
      </div>
    </article>

    <div class="media-stack-right">
      <article class="media-card">
        <a class="media-card-thumb media-card-thumb--video" href="https://www.facebook.com/reel/9033300306705962/" target="_blank" rel="noopener noreferrer" aria-label="Watch Furniture Corner 10-Chair Royal Dining Set Reel">
          <span class="media-pill">SHOWROOM REEL · 10-SEATER ROYAL DINING</span>
          <img src="../assets/furniture/fb_post2.jpg" alt="Furniture Corner 10 Chairs Royal Gold Dining Table Reel" loading="lazy">
          <div class="media-play-badge"><div class="media-play-circle">▶</div></div>
        </a>
        <div class="media-card-body">
          <h3>10-Seater Hand-Carved Royal Dining Reel</h3>
          <p>Close-up motion reel showcasing hand-carved gold leaf detailing, pleated velvet chair backs, and inlaid marble tabletop craftsmanship for luxury home buyers.</p>
          <a class="underline-link" style="color:var(--lime)" href="https://www.facebook.com/reel/9033300306705962/" target="_blank" rel="noopener noreferrer">Watch Dining Reel ↗</a>
        </div>
      </article>

      <article class="media-card">
        <a class="media-card-thumb media-card-thumb--video" href="https://www.instagram.com/p/C0gzFfburrp/" target="_blank" rel="noopener noreferrer">
          <span class="media-pill">BRANDED CATALOG · VELVET &amp; GOLD LOUNGE</span>
          <img src="../assets/furniture/ig_info.jpg" alt="Furniture Corner turquoise velvet and gold accent chairs post" loading="lazy">
        </a>
        <div class="media-card-body">
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px">
            <img src="../assets/furniture/furniture-logo.jpg" alt="Furniture Corner logo" width="38" height="38" style="border-radius:50%;border:1.5px solid var(--lime);background:#fff">
            <h3 style="margin:0">Statement Velvet &amp; Live-Edge Collection</h3>
          </div>
          <p>Branded Instagram catalog showcase pairing scalloped turquoise velvet accent chairs with a live-edge solid wood coffee table to inspire high-ticket living room makeovers.</p>
          <a class="underline-link" style="color:var(--lime)" href="https://www.instagram.com/p/C0gzFfburrp/" target="_blank" rel="noopener noreferrer">View Post on Instagram ↗</a>
        </div>
      </article>
    </div>
  </div>

  <div class="lavish-gallery" aria-label="Lavish Furniture Catalog Highlights">
    <article class="lavish-item">
      <a class="lavish-thumb" href="https://www.instagram.com/p/DdHPX1EjS6N/" target="_blank" rel="noopener noreferrer">
        <span class="media-pill">ROYAL DINING · 8 CHAIRS</span>
        <img src="../assets/furniture/ig_dining.jpg" alt="Elegant 8 Chairs Dining Table Featuring Premium Wooden Craftsmanship" loading="lazy">
      </a>
      <div class="lavish-caption">
        <h4>Royal Gold &amp; Inlaid Marble 8-Chair Dining Set</h4>
        <p>Staged luxury dining room photography highlighting ornate gold-carved crowns, tufted upholstery, and warm architectural shelving.</p>
        <a class="underline-link" style="color:var(--lime)" href="https://www.instagram.com/p/DdHPX1EjS6N/" target="_blank" rel="noopener noreferrer">View on @furniturecorner.pk ↗</a>
      </div>
    </article>

    <article class="lavish-item">
      <a class="lavish-thumb" href="https://www.instagram.com/p/Ddi7nptDVZD/" target="_blank" rel="noopener noreferrer">
        <span class="media-pill">MODERN LUXE · MEDIA WALL</span>
        <img src="../assets/furniture/ig_led.jpg" alt="Furniture Corner Modern Luxe LED Rack" loading="lazy">
      </a>
      <div class="lavish-caption">
        <h4>Modern Luxe Architectural LED Media Console</h4>
        <p>Minimalist walnut and smoked-glass LED console staged with warm indirect lighting and editorial decor for contemporary lounges.</p>
        <a class="underline-link" style="color:var(--lime)" href="https://www.instagram.com/p/Ddi7nptDVZD/" target="_blank" rel="noopener noreferrer">View on @furniturecorner.pk ↗</a>
      </div>
    </article>

    <article class="lavish-item">
      <a class="lavish-thumb" href="https://www.instagram.com/p/DeEKPYvDbgv/" target="_blank" rel="noopener noreferrer">
        <span class="media-pill">BESPOKE COMFORT · LOUNGE</span>
        <img src="../assets/furniture/ig_rocking.jpg" alt="Furniture Corner Luxury Wooden Rocking Chair" loading="lazy">
      </a>
      <div class="lavish-caption">
        <h4>Luxury Tufted &amp; Solid Wood Rocking Chair</h4>
        <p>Close-up texture and craftsmanship shot combining deep charcoal biscuit tufting with polished mahogany-toned solid wood arms.</p>
        <a class="underline-link" style="color:var(--lime)" href="https://www.instagram.com/p/DeEKPYvDbgv/" target="_blank" rel="noopener noreferrer">View on @furniturecorner.pk ↗</a>
      </div>
    </article>
  </div>
</section>
'''

ALPHABET_SHOWCASE_HTML = '''
<div class="brand-bar">
  <div class="brand-bar-info">
    <div class="brand-bar-logo" style="display:grid;place-items:center;background:var(--lime);color:var(--ink);font-weight:900;font-size:22px">3D</div>
    <div>
      <h2>Alphabet Adventure Land · <span style="color:var(--lime)">3D AI Animated Series</span></h2>
      <p>Multi-Episode 3D Character Continuity · Google Flow · Picsart AI · Midjourney (--cref) · Kling AI &amp; Runway Gen-3 · ElevenLabs Lip-Sync</p>
    </div>
  </div>
  <div class="brand-bar-actions">
    <a class="brand-bar-btn" href="../contact.html?service=AI%20video%20and%20animation">Commission 3D AI Video ↗</a>
  </div>
</div>

<section class="media-showcase" aria-label="Alphabet Adventure Land Playable 3D AI Episodes">
  <div class="media-showcase-head">
    <div>
      <div class="section-kicker" style="color:var(--lime)">PLAYABLE STUDIO REELS · TURN SOUND ON</div>
      <h2>Same characters.<br><span class="serif" style="color:var(--lime)">Every episode.</span></h2>
    </div>
    <p style="max-width:410px;color:#bec7bd;font-size:14px;line-height:1.65;margin:0">Notice how both protagonists—the boy in the blue hoodie and the girl in the rainbow-hem pink dress—stay 100% consistent in facial structure, wardrobe, and Pixar-grade lighting across separate episodes.</p>
  </div>

  <div class="media-grid--two-videos">
    <article class="media-card">
      <div class="media-card-thumb media-card-thumb--video">
        <span class="media-pill">EPISODE D · DOG &amp; DRUM (WITH AUDIO)</span>
        <video src="../assets/alphabet/animator-reel.mp4#t=0.1" controls playsinline preload="metadata" aria-label="Alphabet Adventure Land Episode D: D is for Dog and Drum"></video>
      </div>
      <div class="media-card-body">
        <h3>Episode D — “D is for Dog, D is for Drum”</h3>
        <p>Full 3D character kinematics and audio sync: the boy plays a patterned drum with drumsticks while the golden puppy barks on beat and the girl claps along beneath magical particle typography.</p>
      </div>
    </article>

    <article class="media-card">
      <div class="media-card-thumb media-card-thumb--video">
        <span class="media-pill">EPISODE C · CAT &amp; CUP (WITH AUDIO)</span>
        <video src="../assets/alphabet/alphabet-adventure-ep-c.mp4#t=0.1" controls playsinline preload="metadata" aria-label="Alphabet Adventure Land Episode C: C is for Cat and Cup"></video>
      </div>
      <div class="media-card-body">
        <h3>Episode C — “C is for Cat, C is for Cup”</h3>
        <p>Multi-episode character continuity in action: the exact same two 3D protagonists return in a sunlit garden scene alongside an animated orange tabby cat (with synced meow foley) and a smiling teacup.</p>
      </div>
    </article>
  </div>
</section>
'''

CASES = [
    dict(
        slug='gloria-cup',
        title='Gloria Cup Café',
        sub='Turning a Johar Town rooftop café into a 20K+ organic community, live-screening hub, and daily food & coffee ritual.',
        kind='Social Growth · Reels · Community Architecture',
        index='01',
        image='gloria/gloria-deals-feature.jpg',
        theme='gloria',
        role='Lead Social Media Strategist & Content Director',
        scope='Instagram (@gloriacupcafe) · Reels · Influencer Collabs',
        year='20K+ Cross-Channel Community Scaled',
        brand='Gloria Cup Café (Johar Town, Lahore)',
        extra_showcase=GLORIA_SHOWCASE_HTML,
        challenge='Located on a rooftop opposite Emporium Mall in Johar Town, Lahore, Gloria Cup Café needed more than static menu posts—it needed to capture the energy of live cricket match screenings, sizzling Desperado Steaks, loaded pizza platters, and evening cappuccinos so local foodies would choose it as their go-to hangout.',
        direction='I architected a lifestyle- and food-first social engine for @gloriacupcafe built around high-retention rooftop Reels, food creator collaborations, deal-driven carousels, and match-day screening promos that turned online views into packed rooftop tables.',
        ideas=[
            'Positioned the rooftop view (opposite Emporium Mall) and retro street-art ambiance as a signature visual backdrop across Reels and Stories.',
            'Engineered repeatable short-form Reel formats—cheese-pull pizza close-ups, Desperado Steak sizzles, cappuccino pours, and budget platter reveals.',
            'Partnered with local Lahore food creators and vloggers to showcase group deals and drive high-trust word-of-mouth discovery.',
            'Built event-driven urgency around live cricket tournament screenings and late-night (2 PM – 12 AM) hangout deals via Instagram and Foodpanda.'
        ],
        result='Scaled the brand’s organic social footprint past 20,000+ engaged local foodies across platforms, driving consistent daily DM/WhatsApp reservations, viral platter Reels, and packed rooftop match screenings.',
        deliverables=[
            'End-to-End Instagram Management & Grid Direction (@gloriacupcafe)',
            'On-Site Rooftop Reel Production, Creator Collabs & Hook Scripting',
            'Promotional Deal Graphics, Platter Campaigns & Live Screening Event Push',
            'Community Management, Story Repost Loops & Local Discovery SEO'
        ],
        next='furniture-corner',
        next_title='Furniture Corner'
    ),
    dict(
        slug='furniture-corner',
        title='Furniture Corner',
        sub='Transforming luxury furniture collections into lavish visual stories, showroom Reels, and +40% year-over-year commercial growth.',
        kind='Luxury Catalog · Reels · Meta Campaigns',
        index='02',
        image='furniture/ig_dining.jpg',
        theme='furniture',
        role='Performance Content Strategist & Meta Campaign Lead',
        scope='Instagram (@furniturecorner.pk) · Showroom Reels · Meta Ads',
        year='+40% YoY Revenue Expansion',
        brand='Furniture Corner (PIA Road, Lahore · furniturecorner.pk)',
        extra_showcase=FURNITURE_SHOWCASE_HTML,
        challenge='High-ticket luxury furniture—from hand-carved 8- and 10-seater royal dining sets to bouclé bedroom suites—never sells on specifications alone. Buyers need to feel the craftsmanship, texture, and room presence before they ever message on WhatsApp or visit the PIA Road showroom.',
        direction='I elevated @furniturecorner.pk into a lavish digital showroom—combining editorial interior staging, close-up texture Reels, and full-funnel Meta Business Suite catalog campaigns engineered to convert high-intent homeowners and interior buyers.',
        ideas=[
            'Directed lavish, warm-lit room staging for flagship collections: Royal Gold & Marble Dining Sets, Bouclé Bubble Bed Sets, and Modern Luxe LED Consoles.',
            'Produced short-form vertical Showroom Reels that pan across wood carving details, velvet/bouclé textures, and full bedroom/dining setups.',
            'Structured targeted Meta Business Suite ad campaigns reaching active homeowners, bridal/dowry shoppers, and interior design enthusiasts.',
            'Streamlined the Instagram-to-WhatsApp (0309-9566665) inquiry funnel to turn Reel views and post saves into showroom visits and nationwide orders.'
        ],
        result='Drove a +40% year-over-year commercial revenue expansion across 290+ curated Instagram posts and Reels, significantly lowering cost-per-inquiry on Meta placements and increasing high-ticket dining and bedroom set orders.',
        deliverables=[
            'Lavish Digital Catalog & Instagram Grid Curation (@furniturecorner.pk)',
            'Short-Form Showroom Reels (Bouclé Bed Sets, Royal Dining & Lounge Collections)',
            'Meta Business Suite Ad Architecture, Retargeting & Audience Segmentation',
            'Direct-Response Copywriting & WhatsApp/Showroom Conversion Funnel'
        ],
        next='alphabet-jungle',
        next_title='Alphabet Adventure Land'
    ),
    dict(
        slug='alphabet-jungle',
        title='Alphabet Adventure Land',
        sub='Studio-grade 3D character consistency and generative AI motion across episodes—proving what is possible with a disciplined multi-tool AI video pipeline.',
        kind='AI Video Studio · 3D Character Pipeline',
        index='03',
        image='alphabet-cover.svg',
        video_hero='alphabet/animator-reel.mp4',
        theme='alphabet',
        role='AI Video Director & Generative Pipeline Architect',
        scope='Google Flow · Picsart AI · Midjourney · Kling AI · Runway Gen-3 · ElevenLabs',
        year='Multi-Episode 3D Character Continuity',
        brand='Alphabet Adventure Land (Episodes C & D)',
        extra_showcase=ALPHABET_SHOWCASE_HTML,
        challenge='Most AI-generated video fails commercially because characters morph from shot to shot, outfits change randomly, and audio lacks emotional timing. Whether producing a children’s edutainment series or a branded 3D mascot campaign for an international agency, commercial work requires strict frame-to-frame character continuity.',
        direction='I engineered an end-to-end 3D generative production pipeline for Alphabet Adventure Land—locking character identity across episodes (Episode C: Cat & Cup and Episode D: Dog & Drum) while directing expressive kinematics, lip-synced voiceovers, and layered foley sound design.',
        ideas=[
            'Locked 3D character model sheets and visual assets using Midjourney and Picsart AI (the boy in the blue zip hoodie & yellow tee, and the girl in pigtails & rainbow-hem pink dress) so they remain 100% identical across separate episodes.',
            'Directed purposeful prop interaction, cinematic scene transitions, and motion kinematics using Google Flow, Kling AI, and Runway Gen-3—from rhythmic drumstick beats to waving, clapping, and pet reactions.',
            'Engineered expressive child voiceovers, lip-sync, and layered sound effects (drum hits, cat meows, magical chimes, forest ambiance) using ElevenLabs and CapCut Pro.',
            'Structured visual pacing and glowing 3D particle typography around YouTube retention curves to hold viewer attention from the first second.'
        ],
        result='A repeatable, broadcast-ready 3D AI animation pipeline that achieves Pixar-style character warmth and multi-episode continuity at a fraction of traditional 3D studio timelines—ideal for branded mascots, commercial storytelling, and scalable YouTube IP channels.',
        deliverables=[
            'Multi-Episode 3D Character Bible & Visual Asset Refinement (Midjourney & Picsart AI)',
            'Cinematic AI Video Generation, Character Kinematics & Camera Motion (Google Flow, Kling AI & Runway Gen-3)',
            'Expressive Voice Synthesis, Lip-Sync & Foley Audio Engineering (ElevenLabs & CapCut Pro)',
            'Turnkey YouTube Series Production & Retention Optimization'
        ],
        next='marina-fits',
        next_title='Marina Fits (Marinafits.pk)'
    ),
    dict(
        slug='marina-fits',
        title='Marina Fits (Marinafits.pk)',
        sub='Launching an original women’s clothing brand in Lahore—using generative AI to design every dress collection, direct virtual model lookbooks, and manage full-funnel social pages.',
        kind='Brand Founder · AI Fashion Design · Social Management',
        index='04',
        image='clothing/dress-magenta-organza.jpg',
        theme='clothing',
        role='Founder, AI Fashion Designer & Social Media Manager',
        scope='Picsart AI · Google Flow · AI Dress Design · Facebook (Marinafits.pk) · Instagram (@marina_fits_)',
        year='1.8K+ FB Community & 10+ AI Dress Lines',
        brand='Marina Fits · Marinafits.pk (“Elegance Woven For You”)',
        extra_showcase='''
<div class="brand-bar">
  <div class="brand-bar-info">
    <img class="brand-bar-logo" src="../assets/clothing/marinafits-logo.jpg" alt="Marina Fits official logo" width="64" height="64">
    <div>
      <h2>Marina Fits · <span style="color:var(--lime)">Marinafits.pk · @marina_fits_</span></h2>
      <p>Lahore, Pakistan · “Elegance Woven For You” — AI-Designed Modern &amp; Traditional Women’s Pret, 2-Piece &amp; 3-Piece Ensembles</p>
    </div>
  </div>
  <div class="brand-bar-actions">
    <a class="brand-bar-btn" href="https://www.facebook.com/profile.php?id=61575990746354" target="_blank" rel="noopener noreferrer">Visit Marinafits.pk on Facebook ↗</a>
    <a class="brand-bar-btn brand-bar-btn--ghost" href="https://www.instagram.com/marina_fits_/" target="_blank" rel="noopener noreferrer">Instagram @marina_fits_ ↗</a>
  </div>
</div>

<section class="media-showcase" aria-label="Marina Fits AI-Designed Dress Lookbook and Social Showcase">
  <div class="media-showcase-head">
    <div>
      <div class="section-kicker" style="color:var(--lime)">AI-DESIGNED DRESS COLLECTIONS &amp; BRAND PAGES</div>
      <h2>Elegance woven <span class="serif" style="color:var(--lime)">with AI.</span></h2>
    </div>
    <a class="underline-link" style="color:var(--lime)" href="https://www.facebook.com/profile.php?id=61575990746354" target="_blank" rel="noopener noreferrer">Explore all collections on Marinafits.pk Facebook Page ↗</a>
  </div>

  <div class="media-grid">
    <article class="media-card">
      <a class="media-card-thumb media-card-thumb--reel" href="https://www.facebook.com/61575990746354/posts/-grace-in-every-thread-get-ready-to-redefine-elegance-with-marina-fitswhere-time/122105174450866358/" target="_blank" rel="noopener noreferrer" aria-label="View Marina Fits Deep Teal Two-Piece Ensemble Post on Facebook">
        <span class="media-pill">FEATURED LAUNCH POST · DEEP TEAL 2-PIECE</span>
        <img src="../assets/clothing/dress-teal-fringe.jpg" alt="Marina Fits Launching Soon deep teal fringe two-piece ensemble" loading="lazy">
      </a>
      <div class="media-card-body">
        <h3>“Grace in Every Thread” — Deep Teal Fringe 2-Piece</h3>
        <p>Flagship launch campaign post on <strong>Marinafits.pk</strong> showcasing an AI-designed deep teal minimalist two-piece ensemble with delicate fringe-trimmed cuffs and asymmetrical hemline.</p>
        <div style="display:flex;gap:16px;flex-wrap:wrap">
          <a class="underline-link" style="color:var(--lime)" href="https://www.facebook.com/61575990746354/posts/-grace-in-every-thread-get-ready-to-redefine-elegance-with-marina-fitswhere-time/122105174450866358/" target="_blank" rel="noopener noreferrer">View Live Facebook Post ↗</a>
          <a class="underline-link" style="color:#fff" href="https://www.facebook.com/profile.php?id=61575990746354" target="_blank" rel="noopener noreferrer">Open Facebook Page ↗</a>
        </div>
      </div>
    </article>

    <div class="media-stack-right">
      <article class="media-card">
        <a class="media-card-thumb media-card-thumb--video" href="https://www.facebook.com/photo/?fbid=122135577464866358" target="_blank" rel="noopener noreferrer">
          <span class="media-pill">AI COUTURE · CRIMSON ORGANZA 3-PIECE</span>
          <img src="../assets/clothing/dress-magenta-organza.jpg" alt="Marina Fits crimson keyhole 3-piece suit with embroidered organza dupatta" loading="lazy">
        </a>
        <div class="media-card-body">
          <h3>Crimson Keyhole 3-Piece with Floral Organza Dupatta</h3>
          <p>AI-concepted festive 3-piece silhouette combining a jewel-neck keyhole kameez, floral-embroidered sheer organza dupatta, and wide-leg lace-trimmed trousers.</p>
          <a class="underline-link" style="color:var(--lime)" href="https://www.facebook.com/photo/?fbid=122135577464866358" target="_blank" rel="noopener noreferrer">View Post on Marinafits.pk ↗</a>
        </div>
      </article>

      <article class="media-card">
        <a class="media-card-thumb media-card-thumb--video" href="https://www.facebook.com/profile.php?id=61575990746354" target="_blank" rel="noopener noreferrer">
          <span class="media-pill">BRAND IDENTITY · ELEGANCE WOVEN FOR YOU</span>
          <img src="../assets/clothing/marinafits-banner.jpg" alt="Marina Fits Elegance Woven For You official brand cover banner" loading="lazy">
        </a>
        <div class="media-card-body">
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px">
            <img src="../assets/clothing/marinafits-logo.jpg" alt="Marina Fits logo" width="38" height="38" style="border-radius:50%;border:1.5px solid var(--lime)">
            <h3 style="margin:0">End-to-End Brand Identity &amp; Page Management</h3>
          </div>
          <p>Created the complete visual identity, minimalist line-art emblem, catalog typography, and social media strategy across Facebook (1,880+ followers) and Instagram (<code>@marina_fits_</code>).</p>
          <div style="display:flex;gap:16px;flex-wrap:wrap">
            <a class="underline-link" style="color:var(--lime)" href="https://www.facebook.com/profile.php?id=61575990746354" target="_blank" rel="noopener noreferrer">Facebook Page ↗</a>
            <a class="underline-link" style="color:#fff" href="https://www.instagram.com/marina_fits_/" target="_blank" rel="noopener noreferrer">Instagram @marina_fits_ ↗</a>
          </div>
        </div>
      </article>
    </div>
  </div>

  <div class="lavish-gallery" aria-label="Marina Fits AI-Designed Dress Lookbook Gallery">
    <article class="lavish-item">
      <a class="lavish-thumb" href="https://www.facebook.com/photo/?fbid=122135557838866358" target="_blank" rel="noopener noreferrer">
        <span class="media-pill">FRONT &amp; BACK · LACE CO-ORD</span>
        <img src="../assets/clothing/dress-rose-lace.jpg" alt="Dusty rose two-piece co-ord set with white Chantilly lace sleeves and hem" loading="lazy">
      </a>
      <div class="lavish-caption">
        <h4>Dusty Rose Chantilly Lace 2-Piece Co-Ord Set</h4>
        <p>Dual-angle AI lookbook showing front and back tailoring of a collared dusty pink tunic and trousers with intricate white lace cuffs.</p>
        <a class="underline-link" style="color:var(--lime)" href="https://www.facebook.com/photo/?fbid=122135557838866358" target="_blank" rel="noopener noreferrer">View Post on Marinafits.pk ↗</a>
      </div>
    </article>

    <article class="lavish-item">
      <a class="lavish-thumb" href="https://www.facebook.com/photo/?fbid=122110692074866358" target="_blank" rel="noopener noreferrer">
        <span class="media-pill">PASTEL LUXE · MINT 3-PIECE</span>
        <img src="../assets/clothing/dress-mint-organza.jpg" alt="Marina Fits mint pastel 3-piece suit with scalloped organza dupatta" loading="lazy">
      </a>
      <div class="lavish-caption">
        <h4>Mint Pastel Silk &amp; Scalloped Organza 3-Piece</h4>
        <p>Daytime luxury pret design featuring a luminous mint-blue straight shirt paired with a white lace-bordered sheer organza dupatta.</p>
        <a class="underline-link" style="color:var(--lime)" href="https://www.facebook.com/photo/?fbid=122110692074866358" target="_blank" rel="noopener noreferrer">View Post on Marinafits.pk ↗</a>
      </div>
    </article>

    <article class="lavish-item">
      <a class="lavish-thumb" href="https://www.facebook.com/photo/?fbid=122129609276866358" target="_blank" rel="noopener noreferrer">
        <span class="media-pill">SILK DRAPE · ICE BLUE</span>
        <img src="../assets/clothing/dress-iceblue-silk.jpg" alt="Marina Fits ice-blue silk puff-sleeve 3-piece ensemble" loading="lazy">
      </a>
      <div class="lavish-caption">
        <h4>Ice-Blue Shimmer Silk Puff-Sleeve Ensemble</h4>
        <p>Softly structured puff-sleeve silk tunic with wide-leg palazzo trousers and a flowing tonal dupatta.</p>
        <a class="underline-link" style="color:var(--lime)" href="https://www.facebook.com/photo/?fbid=122129609276866358" target="_blank" rel="noopener noreferrer">View Post on Marinafits.pk ↗</a>
      </div>
    </article>

    <article class="lavish-item">
      <a class="lavish-thumb" href="https://www.facebook.com/photo/?fbid=122110297796866358" target="_blank" rel="noopener noreferrer">
        <span class="media-pill">RESORT PRET · SKY BLUE</span>
        <img src="../assets/clothing/dress-skyblue-kurta.jpg" alt="Marina Fits sky-blue kurta with coral and gold neckline embroidery" loading="lazy">
      </a>
      <div class="lavish-caption">
        <h4>Sky-Blue A-Line Kurta with Coral Embroidery</h4>
        <p>Breezy everyday pret silhouette accented with vibrant coral-pink and gold geometric neckline embroidery.</p>
        <a class="underline-link" style="color:var(--lime)" href="https://www.facebook.com/photo/?fbid=122110297796866358" target="_blank" rel="noopener noreferrer">View Post on Marinafits.pk ↗</a>
      </div>
    </article>

    <article class="lavish-item">
      <a class="lavish-thumb" href="https://www.facebook.com/photo/?fbid=122109949682866358" target="_blank" rel="noopener noreferrer">
        <span class="media-pill">MODERN MAXI · ESPRESSO</span>
        <img src="../assets/clothing/dress-brown-tiered.jpg" alt="Marina Fits espresso brown tiered smocked maxi dress" loading="lazy">
      </a>
      <div class="lavish-caption">
        <h4>Espresso Brown Smocked Bodice Tiered Maxi</h4>
        <p>Contemporary fusion wear combining a square-neck smocked bodice, voluminous bishop sleeves, and floor-sweeping tiered skirt.</p>
        <a class="underline-link" style="color:var(--lime)" href="https://www.facebook.com/photo/?fbid=122109949682866358" target="_blank" rel="noopener noreferrer">View Post on Marinafits.pk ↗</a>
      </div>
    </article>

    <article class="lavish-item">
      <a class="lavish-thumb" href="https://www.facebook.com/photo/?fbid=122109559202866358" target="_blank" rel="noopener noreferrer">
        <span class="media-pill">MINIMALIST · CAMEL CO-ORD</span>
        <img src="../assets/clothing/dress-camel-coord.jpg" alt="Marina Fits warm camel and black contrast-cuff modern tunic co-ord" loading="lazy">
      </a>
      <div class="lavish-caption">
        <h4>Warm Camel &amp; Black Contrast-Cuff Co-Ord</h4>
        <p>Executive-ready minimalist 2-piece featuring a relaxed V-neck camel tunic with bold black split cuffs and cropped tailored trousers.</p>
        <a class="underline-link" style="color:var(--lime)" href="https://www.facebook.com/photo/?fbid=122109559202866358" target="_blank" rel="noopener noreferrer">View Post on Marinafits.pk ↗</a>
      </div>
    </article>

    <article class="lavish-item">
      <a class="lavish-thumb" href="https://www.facebook.com/photo/?fbid=122109554846866358" target="_blank" rel="noopener noreferrer">
        <span class="media-pill">STREET PRET · CHARTREUSE</span>
        <img src="../assets/clothing/dress-olive-street.jpg" alt="Marina Fits chartreuse olive street-style 2-piece co-ord set" loading="lazy">
      </a>
      <div class="lavish-caption">
        <h4>Chartreuse Olive Street-Style 2-Piece Set</h4>
        <p>Modern urban pret lookbook staging a structured olive-lime tunic and cigarette pants in natural outdoor lighting.</p>
        <a class="underline-link" style="color:var(--lime)" href="https://www.facebook.com/photo/?fbid=122109554846866358" target="_blank" rel="noopener noreferrer">View Post on Marinafits.pk ↗</a>
      </div>
    </article>

    <article class="lavish-item">
      <a class="lavish-thumb" href="https://www.facebook.com/photo/?fbid=122109948968866358" target="_blank" rel="noopener noreferrer">
        <span class="media-pill">FESTIVE · EMERALD &amp; PINK</span>
        <img src="../assets/clothing/dress-emerald-pink.jpg" alt="Marina Fits emerald embroidered kurta with vibrant pink zari dupatta" loading="lazy">
      </a>
      <div class="lavish-caption">
        <h4>Emerald Zari Kurta &amp; Hot Pink Dupatta</h4>
        <p>Traditional Pakistani festive color-blocking pairing a teal-emerald embroidered kameez with a contrasting magenta-pink zari dupatta.</p>
        <a class="underline-link" style="color:var(--lime)" href="https://www.facebook.com/photo/?fbid=122109948968866358" target="_blank" rel="noopener noreferrer">View Post on Marinafits.pk ↗</a>
      </div>
    </article>

    <article class="lavish-item">
      <a class="lavish-thumb" href="https://www.facebook.com/profile.php?id=61575990746354" target="_blank" rel="noopener noreferrer">
        <span class="media-pill">BRAND EMBLEM · MARINA FITS</span>
        <img src="../assets/clothing/marinafits-logo.jpg" alt="Marina Fits official circular plum brand emblem" loading="lazy">
      </a>
      <div class="lavish-caption">
        <h4>Marina Fits Official Brand Identity</h4>
        <p>Minimalist continuous-line couture silhouette emblem on deep plum—designed for social avatars, hangtags, and lookbook watermarks.</p>
        <a class="underline-link" style="color:var(--lime)" href="https://www.facebook.com/profile.php?id=61575990746354" target="_blank" rel="noopener noreferrer">Visit Marinafits.pk ↗</a>
      </div>
    </article>
  </div>
</section>
''',
        challenge='Launching an independent women’s clothing brand in Pakistan traditionally demands massive upfront capital for sample stitching, studio photography, model bookings, and location shoots before testing which silhouettes customers actually want to buy.',
        direction='I founded and launched Marina Fits (Marinafits.pk — “Elegance Woven For You”), using Picsart AI, Google Flow, and generative AI design workflows to create original 2-piece and 3-piece women’s dress collections, visualize realistic fabric drapes (organza, silk, chantilly lace, khaddar, and lawn) on virtual models, and manage the brand’s entire Facebook and Instagram presence.',
        ideas=[
            'Designed 10+ original women’s wear silhouettes using Picsart AI, Google Flow, and generative AI—ranging from fringed deep-teal minimalist co-ords and dusty-rose lace sets to festive embroidered organza 3-piece suits.',
            'Used multi-angle AI fashion prototyping and Picsart AI studio editing (including front-and-back tailoring sheets) to validate cuts, sleeve detailing, and color palettes before physical production.',
            'Created the complete Marina Fits visual identity (“Elegance Woven For You”), plum continuous-line couture logo, and editorial typography.',
            'Built and manage the official Facebook page (Marinafits.pk, 1,880+ followers) and Instagram (@marina_fits_), handling catalog copywriting, community engagement, and WhatsApp/DM order inquiries.'
        ],
        result='Successfully launched Marinafits.pk from concept to a 1,880+ follower Facebook community and multi-collection digital storefront—eliminating traditional photoshoot overhead while proving how generative AI can power end-to-end fashion design and e-commerce merchandising.',
        deliverables=[
            'Founder & Creative Direction — Marina Fits (Marinafits.pk)',
            'AI-Assisted Apparel & Dress Design with Picsart AI & Google Flow (2-Piece Co-Ords, 3-Piece Organza/Silk Suits & Tiered Maxis)',
            'Virtual Model Editorial Lookbooks & Front/Back Tailoring Visualization',
            'End-to-End Facebook & Instagram (@marina_fits_) Page Management & Social Merchandising'
        ],
        next='gloria-cup',
        next_title='Gloria Cup Café'
    )
]

HEAD = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#f7f6f0"><meta name="description" content="{desc}"><meta property="og:title" content="{title} — Marina Bashir"><meta property="og:description" content="{desc}"><meta property="og:image" content="https://marinabashir.netlify.app/assets/og-cover.png"><link rel="icon" href="../assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="../styles.css"><script defer src="../main.js"></script><title>{title} — Case Study | Marina Bashir</title></head>'''

NAV = '''<a class="skip-link" href="#main">Skip to content</a><header class="site-header"><div class="header-inner container"><a href="../index.html" class="brand"><span class="brand-mark" aria-hidden="true">mb.</span><span>marina bashir<em> / studio</em></span></a><nav class="header-links" aria-label="Main navigation"><a href="../index.html#work">Selected work</a><a href="../index.html#experience">Experience</a><a href="../index.html#expertise">Expertise</a><a href="../index.html#packages">Packages</a><a href="../index.html#about">About</a><a href="../index.html#contact">Contact</a></nav><div class="header-action"><span class="availability">Available for global retainers</span><a class="header-cta" href="../contact.html">Book a project ↗</a><button type="button" class="menu-button" data-menu-button aria-expanded="false" aria-controls="mobile-nav">Menu ☰</button></div></div><nav id="mobile-nav" class="mobile-panel" data-mobile-panel aria-label="Mobile navigation"><a href="../index.html#work">Selected work ↗</a><a href="../index.html#experience">Experience ↗</a><a href="../index.html#expertise">Expertise ↗</a><a href="../index.html#packages">Packages ↗</a><a href="../index.html#about">About ↗</a><a href="../index.html#contact">Contact ↗</a></nav></header>'''

FOOT = '''<footer class="footer"><div class="container"><div class="footer-inner"><a href="../index.html" class="brand"><span class="brand-mark" aria-hidden="true">mb.</span><span>marina bashir</span></a><span>AI-Powered Social Growth &amp; Creative Video Studio. © 2026 Marina Bashir.</span><div class="footer-links"><a href="mailto:marinabashir74@gmail.com">Email ↗</a><a href="https://wa.me/923024292224" target="_blank" rel="noopener noreferrer">WhatsApp ↗</a><a href="https://linkedin.com/in/marina-bashir-a356641b5" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a></div></div><p class="footer-bottom">Lahore, Pakistan · Serving brands, founders &amp; agencies worldwide.</p></div></footer>'''

out_dir = SITE_DIR / 'work'
out_dir.mkdir(parents=True, exist_ok=True)

for c in CASES:
    desc = escape(c['sub'], quote=True)
    head = HEAD.format(desc=desc, title=escape(c['title']))
    bullets = ''.join('<li>' + escape(b) + '</li>' for b in c['ideas'])
    deliverables = ''.join('<li>' + escape(b) + '</li>' for b in c['deliverables'])
    extra_html = c.get('extra_showcase', '')
    if c.get('video_hero'):
        hero_media_html = f'<video class="case-art" src="../assets/{c["video_hero"]}" autoplay muted loop playsinline preload="metadata"></video>'
    else:
        hero_media_html = f'<img class="case-art" src="../assets/{c["image"]}" alt="{escape(c["title"])} case study visual cover" width="1200" height="1020">'
    html = (
        head
        + f'''<body class="case-page--{c['theme']}">{NAV}<main id="main"><section class="case-header"><div class="container"><div class="case-breadcrumb"><a href="../index.html">Home</a><span> / </span><a href="../index.html#work">Selected work</a><span> / </span>{escape(c['title'])}</div><div class="case-kicker">{escape(c['index'])} / {escape(c['kind'])}</div><h1 class="display case-title">{escape(c['title'])}<span style="color:var(--coral)">.</span></h1><p class="case-subtitle">{escape(c['sub'])}</p></div></section><div class="container">{extra_html}{hero_media_html}<div class="case-details"><div class="case-detail"><small>Client / Showcase</small><strong>{escape(c['brand'])}</strong></div><div class="case-detail"><small>Role</small><strong>{escape(c['role'])}</strong></div><div class="case-detail"><small>Core Stack &amp; Scope</small><strong>{escape(c['scope'])}</strong></div><div class="case-detail"><small>Key Highlight</small><strong>{escape(c['year'])}</strong></div></div></div><div class="container case-content"><section class="case-story"><h2>The challenge.</h2><div><p>{escape(c['challenge'])}</p></div></section><section class="case-story"><h2>Strategic direction.</h2><div><p>{escape(c['direction'])}</p></div></section><section class="case-story"><h2>Execution in motion.</h2><div><ul>{bullets}</ul></div></section><section class="case-story"><h2>Commercial impact.</h2><div><p>{escape(c['result'])}</p></div></section><section class="case-story"><h2>Deliverables &amp; stack.</h2><div><p>Core production capabilities and deliverables executed in this workflow:</p><ul>{deliverables}</ul></div></section><div class="case-follow"><div><div class="eyebrow">KEEP EXPLORING</div><h3>Up next: <span class="serif">{escape(c['next_title'])}</span></h3></div><a href="{c['next']}.html">View next story ↗</a></div></div><section class="contact-section"><div class="container"><div class="section-kicker">WANT RESULTS LIKE THIS?</div><h2 class="display" style="font-size:clamp(67px,10vw,145px)">Let's <span class="serif">build it.</span></h2><div class="contact-buttons" style="margin-top:28px"><a class="button" href="../contact.html">Book a project or retainer ↗</a><a class="button button--outline" href="https://wa.me/923024292224?text=Hi%20Marina%2C%20I%20saw%20your%20{escape(c['title'])}%20case%20study%20and%20would%20love%20to%20chat." target="_blank" rel="noopener noreferrer">Chat on WhatsApp ↗</a></div></div></section></main>{FOOT}</body></html>'''
    )
    (out_dir / f"{c['slug']}.html").write_text(html, encoding='utf-8')

print('Generated', len(CASES), 'case study pages in', out_dir)
