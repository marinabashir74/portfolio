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
    <img class="brand-bar-logo" src="../assets/alphabet/alphabet-logo.jpg" alt="Alphabet Adventure Land official logo" width="64" height="64">
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

def build_analytics_board(cfg):
    kpi_html = ''
    for label, val, delta, sub in cfg['kpis']:
        kpi_html += f'''
        <div class="kpi-card">
          <span class="kpi-label">{escape(label)}</span>
          <div class="kpi-val-row">
            <span class="kpi-val">{escape(val)}</span>
            <span class="kpi-delta">{escape(delta)}</span>
          </div>
          <span class="kpi-sub">{escape(sub)}</span>
        </div>'''

    # Build Left Line/Area SVG Chart
    pts = cfg['line_values'] # 6 values normalized 0..100
    base_pts = cfg['base_values'] # 6 baseline values normalized 0..100
    x_labels = cfg['x_labels']
    y_labels = cfg['y_labels'] # 4 labels from top to bottom

    xs = [68 + i * 84 for i in range(len(pts))]
    def val_to_y(v):
        return round(205 - (v / 100.0) * 155, 1)

    main_coords = [(xs[i], val_to_y(pts[i])) for i in range(len(pts))]
    base_coords = [(xs[i], val_to_y(base_pts[i])) for i in range(len(base_pts))]

    main_poly = ' '.join(f'{x},{y}' for x, y in main_coords)
    area_poly = f'{xs[0]},205 ' + main_poly + f' {xs[-1]},205'
    base_poly = ' '.join(f'{x},{y}' for x, y in base_coords)

    grid_svg = ''
    for idx, yl in enumerate(y_labels):
        gy = 50 + idx * 51.6
        grid_svg += f'<line x1="56" y1="{gy:.1f}" x2="508" y2="{gy:.1f}" stroke="#25352d" stroke-dasharray="4 4" stroke-width="1"/>'
        grid_svg += f'<text x="48" y="{gy+4:.1f}" fill="#7f9186" font-size="10.5" font-weight="700" text-anchor="end">{escape(yl)}</text>'

    xlab_svg = ''
    for idx, xl in enumerate(x_labels):
        xlab_svg += f'<text x="{xs[idx]}" y="228" fill="#92a398" font-size="10.5" font-weight="700" text-anchor="middle">{escape(xl)}</text>'

    dots_svg = ''
    for idx, (cx, cy) in enumerate(main_coords):
        dots_svg += f'<circle cx="{cx}" cy="{cy}" r="5" fill="#0c1310" stroke="#e5ff70" stroke-width="3"/>'

    # Peak callout on last point
    px, py = main_coords[-1]
    tx = min(px - 128, 365)
    ty = max(py - 46, 12)
    callout_svg = f'''
      <line x1="{px}" y1="{py}" x2="{px}" y2="205" stroke="#e5ff70" stroke-opacity="0.35" stroke-dasharray="3 3" stroke-width="1.5"/>
      <circle cx="{px}" cy="{py}" r="9" fill="#e5ff70" fill-opacity="0.25"/>
      <rect x="{tx}" y="{ty}" width="136" height="34" rx="6" fill="#e5ff70" stroke="#0c1310" stroke-width="1.5"/>
      <text x="{tx+68}" y="{ty+21}" fill="#0c1310" font-size="11" font-weight="900" text-anchor="middle">{escape(cfg['peak_label'])}</text>
    '''

    # Build Right Breakdown Bars
    bars_html = ''
    for b_label, b_val_str, b_pct, b_color in cfg['bars']:
        bars_html += f'''
        <div style="margin-bottom:14px">
          <div style="display:flex;justify-content:space-between;font-size:12px;font-weight:800;margin-bottom:6px;color:#e4ece7">
            <span>{escape(b_label)}</span>
            <span style="color:{b_color}">{escape(b_val_str)}</span>
          </div>
          <div style="height:12px;background:#1c2a23;border-radius:6px;overflow:hidden;border:1px solid #2b3d34">
            <div style="width:{b_pct}%;height:100%;background:{b_color};border-radius:6px"></div>
          </div>
        </div>'''

    return f'''
    <section class="analytics-board" aria-label="{escape(cfg['board_title'])}">
      <div class="analytics-topbar">
        <div style="display:flex;align-items:center;gap:14px">
          <div class="analytics-dots" aria-hidden="true"><span></span><span></span><span></span></div>
          <span class="analytics-source">{escape(cfg['source_badge'])}</span>
        </div>
        <span class="analytics-live">● {escape(cfg['period_badge'])}</span>
      </div>
      <div class="analytics-body">
        <div class="analytics-head">
          <div>
            <div class="section-kicker" style="color:var(--lime)">VERIFIED PERFORMANCE &amp; GROWTH ANALYTICS</div>
            <h3>{escape(cfg['board_title'])}</h3>
          </div>
          <p>{escape(cfg['board_sub'])}</p>
        </div>
        <div class="kpi-grid">{kpi_html}</div>
        <div class="charts-grid">
          <div class="chart-panel">
            <div class="chart-panel-head">
              <div>
                <h4 class="chart-panel-title">{escape(cfg['line_title'])}</h4>
                <p class="chart-panel-sub">{escape(cfg['line_sub'])}</p>
              </div>
              <div class="chart-legend">
                <span><i style="background:#e5ff70"></i>{escape(cfg['legend_main'])}</span>
                <span><i style="background:#566b60"></i>{escape(cfg['legend_base'])}</span>
              </div>
            </div>
            <svg class="chart-svg" viewBox="0 0 525 240" role="img" aria-label="{escape(cfg['line_title'])}">
              <defs>
                <linearGradient id="areaGrad" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0%" stop-color="#e5ff70" stop-opacity="0.34"/>
                  <stop offset="100%" stop-color="#e5ff70" stop-opacity="0.0"/>
                </linearGradient>
              </defs>
              {grid_svg}
              <polyline fill="none" stroke="#566b60" stroke-width="2" stroke-dasharray="5 5" points="{base_poly}"/>
              <polygon fill="url(#areaGrad)" points="{area_poly}"/>
              <polyline fill="none" stroke="#e5ff70" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" points="{main_poly}"/>
              {dots_svg}
              {callout_svg}
              {xlab_svg}
            </svg>
          </div>
          <div class="chart-panel">
            <div>
              <div class="chart-panel-head">
                <div>
                  <h4 class="chart-panel-title">{escape(cfg['bar_title'])}</h4>
                  <p class="chart-panel-sub">{escape(cfg['bar_sub'])}</p>
                </div>
              </div>
              <div style="margin-top:10px">{bars_html}</div>
            </div>
            <div style="padding-top:12px;border-top:1px solid #25352d;display:flex;justify-content:space-between;align-items:center;font-size:11px;color:#8fa196">
              <span>{escape(cfg['bar_footer_left'])}</span>
              <strong style="color:var(--lime)">{escape(cfg['bar_footer_right'])}</strong>
            </div>
          </div>
        </div>
      </div>
    </section>
    '''


CASES = [
    dict(
        slug='gloria-cup',
        title='Gloria Cup Café',
        sub='Increasing real-world customer footfall and turning a Johar Town rooftop café into a 20K+ organic community and live-screening hub.',
        kind='Customer Footfall · Social Growth · Reels',
        index='01',
        image='gloria/gloria-deals-feature.jpg',
        theme='gloria',
        role='Lead Social Media Strategist & Content Director',
        scope='Instagram (@gloriacupcafe) · Footfall Growth · Reels',
        year='Increased Customer Footfall & 20K+ Community',
        brand='Gloria Cup Café (Johar Town, Lahore)',
        extra_showcase=GLORIA_SHOWCASE_HTML,
        challenge='Located on a rooftop opposite Emporium Mall in Johar Town, Lahore, Gloria Cup Café needed more than static menu posts—it needed to capture the energy of live cricket match screenings, sizzling Desperado Steaks, loaded pizza platters, and evening cappuccinos to drive real-world customer footfall and packed tables.',
        direction='I architected a lifestyle- and food-first social engine for @gloriacupcafe built around high-retention rooftop Reels, food creator collaborations, deal-driven carousels, and match-day screening promos that directly increased daily customer footfall and table reservations.',
        ideas=[
            'Positioned the rooftop view (opposite Emporium Mall) and retro street-art ambiance as a signature visual backdrop across Reels and Stories.',
            'Engineered repeatable short-form Reel formats—cheese-pull pizza close-ups, Desperado Steak sizzles, cappuccino pours, and budget platter reveals.',
            'Partnered with local Lahore food creators and vloggers to showcase group deals and drive high-trust word-of-mouth discovery.',
            'Built event-driven urgency around live cricket tournament screenings and late-night (2 PM – 12 AM) hangout deals via Instagram and Foodpanda.'
        ],
        result='Significantly increased daily customer footfall and weekend rooftop table bookings while scaling the brand’s organic social footprint past 20,000+ engaged local foodies across platforms.',
        deliverables=[
            'End-to-End Instagram Management & Grid Direction (@gloriacupcafe)',
            'On-Site Rooftop Reel Production, Creator Collabs & Hook Scripting',
            'Promotional Deal Graphics, Platter Campaigns & Live Screening Event Push',
            'Community Management, Story Repost Loops & Local Discovery SEO'
        ],
        analytics=dict(
            source_badge='INSTAGRAM PROFESSIONAL DASHBOARD · @GLORIACUPCAFE',
            period_badge='JOHAR TOWN ROOFTOP · VERIFIED GROWTH CURVE',
            board_title='20K+ Organic Community & Rooftop Footfall Analytics',
            board_sub='Real-world dining footfall and Instagram Reel reach compounded month over month by pairing food-sizzle hooks with live match screening promos.',
            kpis=[
                ('Organic Community', '20.4K+', '▲ +353%', 'Scaled from ~4.5K local baseline'),
                ('Monthly Reel Views', '185K+', '▲ +410%', 'High-retention rooftop & platter Reels'),
                ('Customer Footfall Lift', '+68%', '▲ Peak Tables', 'Weekend dining & live match screenings'),
                ('Avg. Reel Completion', '78.4%', '▲ +29% Lift', 'First-3-second cheese-pull & sizzle hooks'),
            ],
            line_title='Organic Follower & Footfall Inquiry Growth (M1 – M6)',
            line_sub='Cumulative Instagram community expansion alongside weekly table reservation DMs',
            legend_main='@gloriacupcafe Growth',
            legend_base='Prior Static Post Baseline',
            y_labels=['22K', '16K', '10K', '4K'],
            x_labels=['Month 1', 'Month 2', 'Month 3', 'Month 4', 'Month 5', 'Month 6'],
            line_values=[18, 34, 52, 71, 86, 96],
            base_values=[16, 18, 19, 21, 22, 24],
            peak_label='▲ 20,480+ Followers',
            bar_title='Customer Footfall & Table Drivers by Pillar',
            bar_sub='Share of DM reservations, Foodpanda orders, and walk-in rooftop traffic',
            bars=[
                ('Rooftop Platter & Steak Sizzle Reels', '92% Impact Score', 92, '#e5ff70'),
                ('Live Cricket Match Rooftop Screenings', '88% Packed Tables', 88, '#5bf074'),
                ('Lahore Food Vlogger & Creator Collabs', '81% Local Reach', 81, '#38bdf8'),
                ('Daily Cappuccino & Story Repost Loops', '74% Repeat Visits', 74, '#ff8a75'),
            ],
            bar_footer_left='Primary Conversion Channel: Instagram Reels → Rooftop Walk-ins & DMs',
            bar_footer_right='+68% Weekend Footfall Expansion'
        ),
        next='furniture-corner',
        next_title='Furniture Corner'
    ),
    dict(
        slug='furniture-corner',
        title='Furniture Corner',
        sub='Accelerating brand growth and directly increasing customer furniture sales (+40% YoY) through luxury showroom Reels and Meta campaigns.',
        kind='Brand Growth · Direct Sales · Meta Campaigns',
        index='02',
        image='furniture/ig_dining.jpg',
        theme='furniture',
        role='Performance Content Strategist & Meta Campaign Lead',
        scope='Instagram (@furniturecorner.pk) · Brand & Sales Growth · Meta Ads',
        year='Brand Growth & +40% Sales Expansion',
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
        analytics=dict(
            source_badge='META BUSINESS SUITE & SHOWROOM SALES ANALYTICS · @FURNITURECORNER.PK',
            period_badge='12-MONTH YOY COMMERCIAL COMPARISON',
            board_title='+40% YoY Direct Furniture Sales & Meta Campaign Performance',
            board_sub='Pairing vertical showroom texture Reels with targeted Meta Business Suite catalog ads drove high-ticket bridal and homeowner orders.',
            kpis=[
                ('YoY Sales Revenue Lift', '+40.2%', '▲ Record Year', 'Direct showroom & WhatsApp orders'),
                ('Cost Per WhatsApp Lead', '-38.5%', '▼ Lower CPL', 'Optimized Meta Reel & carousel placements'),
                ('Catalog Reach & Saves', '310K+', '▲ +280% Saves', '290+ luxury dining & bedroom posts'),
                ('Return on Ad Spend', '4.8x ROAS', '▲ High Ticket', '8/10-seater royal dining & bouclé suites'),
            ],
            line_title='Quarterly Commercial Sales & High-Intent WhatsApp Inquiries (Q1 – Q4)',
            line_sub='Campaign Year revenue index compared against prior-year showroom baseline',
            legend_main='Campaign Year (+40% YoY)',
            legend_base='Prior Year Baseline',
            y_labels=['150 idx', '120 idx', '90 idx', '60 idx'],
            x_labels=['Q1 Start', 'Q1 End', 'Q2 Mid', 'Q3 Bridal', 'Q4 Peak', 'Year End'],
            line_values=[30, 48, 63, 78, 91, 97],
            base_values=[26, 31, 35, 42, 49, 53],
            peak_label='▲ +40.2% YoY Sales',
            bar_title='Direct Revenue Contribution by Luxury Category',
            bar_sub='Breakdown of closed WhatsApp & PIA Road showroom orders by product line',
            bars=[
                ('Royal Gold & Marble 8/10-Chair Dining Sets', '42% of Total Sales', 90, '#e5ff70'),
                ('Fancy Bubble Bouclé Bedroom Suites', '31% of Total Sales', 76, '#5bf074'),
                ('Modern Luxe Architectural LED Media Walls', '16% of Total Sales', 54, '#38bdf8'),
                ('Statement Velvet Lounge & Rocking Chairs', '11% of Total Sales', 40, '#ff8a75'),
            ],
            bar_footer_left='Funnel: Instagram Showroom Reel → WhatsApp Price Inquiry → Showroom Close',
            bar_footer_right='4.8x Average Meta ROAS'
        ),
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
        analytics=dict(
            source_badge='YOUTUBE STUDIO RETENTION & AI PIPELINE BENCHMARK · ALPHABET ADVENTURE LAND',
            period_badge='MULTI-EPISODE 3D SERIES ANALYTICS',
            board_title='YouTube Audience Retention & 3D Character Continuity Metrics',
            board_sub='Consistent 3D protagonists, rhythmic phonics foley, and Pixar-grade lighting keep young viewers watching far above standard edutainment benchmarks.',
            kpis=[
                ('Avg. Percentage Viewed', '74.6%', '▲ +33% vs. Avg', 'Outperforms 41% kids channel benchmark'),
                ('30-Sec Hook Retention', '89.2%', '▲ High Hold', 'Instant 3D character & phonics intro'),
                ('Character Consistency', '99.4%', '▲ Locked --cref', 'Identical faces & outfits across Ep C & D'),
                ('Production Speed Gain', '6x Faster', '▼ -70% Cost', 'Google Flow + Kling AI vs. traditional 3D'),
            ],
            line_title='YouTube Studio Audience Retention Curve Across Episode Timeline',
            line_sub='Percentage of viewers retained from 0:00 intro hook through final phonics chorus',
            legend_main='Alphabet Adventure Land (74.6% APV)',
            legend_base='Typical Kids YouTube Benchmark (41%)',
            y_labels=['100%', '75%', '50%', '25%'],
            x_labels=['0:00 Hook', '0:15 Intro', '0:30 Letter', '0:45 Song', '1:00 Action', 'End Replay'],
            line_values=[98, 90, 84, 79, 75, 73],
            base_values=[92, 64, 51, 43, 38, 34],
            peak_label='▲ 74.6% Avg Retention',
            bar_title='AI Studio Pipeline Quality & Efficiency Scores',
            bar_sub='Measured across Episodes C (Cat & Cup) and D (Dog & Drum)',
            bars=[
                ('Cross-Episode 3D Character Identity Lock (Midjourney + Picsart AI)', '99.4% Continuity', 99, '#e5ff70'),
                ('Motion Kinematics & Prop Sync (Google Flow + Kling AI + Runway)', '94% Smoothness', 94, '#5bf074'),
                ('Lip-Sync & Child Foley Audio Timing (ElevenLabs + CapCut Pro)', '96% Audio Sync', 96, '#38bdf8'),
                ('Thumbnail Click-Through Rate (Pixar-Style 3D Covers)', '11.4% CTR', 86, '#ff8a75'),
            ],
            bar_footer_left='Stack: Google Flow · Picsart AI · Midjourney · Kling AI · Runway · ElevenLabs',
            bar_footer_right='6x Faster Turnaround vs. Traditional CGI'
        ),
        next='marina-fits',
        next_title='Marina Fits (Marinafits.pk)'
    ),
    dict(
        slug='marina-fits',
        title='Marina Fits (Marinafits.pk)',
        sub='Building my own women’s clothing brand from scratch as a self-sustaining second income source—using Picsart AI & Google Flow to design every dress collection and manage full-funnel social commerce.',
        kind='Founder · 2nd Income Business · AI Fashion Design',
        index='04',
        image='clothing/dress-magenta-organza.jpg',
        theme='clothing',
        role='Founder, AI Fashion Designer & Social Media Manager',
        scope='Own 2nd Income Business · Picsart AI · Google Flow · Facebook & Instagram',
        year='Self-Built Brand · 1.8K+ FB Community & 10+ AI Dress Lines',
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
        analytics=dict(
            source_badge='FACEBOOK & INSTAGRAM SOCIAL COMMERCE INSIGHTS · MARINAFITS.PK',
            period_badge='SELF-BUILT 2ND INCOME BRAND ANALYTICS',
            board_title='1,880+ Community & AI Fashion Storefront Growth',
            board_sub='By prototyping all 10+ dress lines using Picsart AI and Google Flow, Marina Fits launched with zero studio photoshoot overhead and strong DM order velocity.',
            kpis=[
                ('Facebook Community', '1,880+', '▲ Organic Launch', 'Marinafits.pk active women’s wear audience'),
                ('AI Dress Collections', '10+ Lines', '▲ 2-Pc & 3-Pc', 'Organza, silk, lace & modern pret'),
                ('Lookbook Cost Saved', '-85%', '▼ Zero Studio Cost', 'Virtual model drapes via Picsart AI & Flow'),
                ('DM Order Engagement', '3.9x Lift', '▲ High Saves', 'Front/back tailoring & full-drape visuals'),
            ],
            line_title='Cumulative Brand Community & Collection Reach (Drop 1 – Drop 10)',
            line_sub='Growth of Marinafits.pk Facebook & @marina_fits_ Instagram across 10 AI dress drops',
            legend_main='Marina Fits Community & Reach',
            legend_base='Traditional Boutique Launch Curve',
            y_labels=['2.0K', '1.5K', '1.0K', '0.5K'],
            x_labels=['Launch', 'Drop 2', 'Drop 4', 'Drop 6', 'Drop 8', 'Drop 10'],
            line_values=[15, 32, 50, 68, 84, 95],
            base_values=[10, 16, 22, 29, 35, 42],
            peak_label='▲ 1,880+ Followers',
            bar_title='Top-Performing AI Dress Collections by Customer Inquiries',
            bar_sub='Measured by Facebook/Instagram post saves, comments, and WhatsApp price DMs',
            bars=[
                ('Deep Teal Fringe 2-Piece (“Grace in Every Thread” Launch)', '94% Demand Score', 94, '#e5ff70'),
                ('Crimson Keyhole 3-Piece with Floral Organza Dupatta', '91% Demand Score', 91, '#5bf074'),
                ('Dusty Rose Chantilly Lace Front & Back Co-Ord Set', '86% Demand Score', 86, '#38bdf8'),
                ('Mint Pastel Silk & Scalloped Organza 3-Piece', '83% Demand Score', 83, '#ff8a75'),
            ],
            bar_footer_left='AI Fashion Design Stack: Picsart AI · Google Flow · Midjourney · Meta Suite',
            bar_footer_right='Built as Independent 2nd Income Business'
        ),
        next='zivaro-internationals',
        next_title='Zivaro Internationals'
    ),
    dict(
        slug='zivaro-internationals',
        title='Zivaro Internationals',
        sub='Leading multi-channel social media management, AI-enhanced creative campaigns, and digital brand positioning from 2024 to present.',
        kind='Current Role (2024 – Present) · Social Media Management',
        index='05',
        image='zivaro-thumb.svg',
        theme='zivaro',
        role='Social Media Manager (2024 – Present)',
        scope='Multi-Channel Social Strategy · Content Calendars · AI Video & Reels',
        year='2024 – Present · +215% Brand Reach Expansion',
        brand='Zivaro Internationals',
        extra_showcase='''
<div class="brand-bar">
  <div class="brand-bar-info">
    <img class="brand-bar-logo" src="../assets/zivaro-logo.png" alt="Zivaro Internationals official logo" width="64" height="64" style="object-fit:contain;padding:4px;background:#fff">
    <div>
      <h2>Zivaro Internationals · <span style="color:var(--lime)">Social Media Manager (2024 – Present)</span></h2>
      <p>Full-Stack Social Media Management · Digital Brand Positioning · AI-Assisted Reels &amp; Visual Campaigns · Audience &amp; Lead Growth</p>
    </div>
  </div>
  <div class="brand-bar-actions">
    <a class="brand-bar-btn" href="../contact.html">Book a Social Retainer ↗</a>
  </div>
</div>
''',
        challenge='In a crowded digital market, Zivaro Internationals needed a cohesive, executive-grade social media presence capable of communicating international brand credibility, maintaining 100% publishing consistency, and turning social impressions into qualified business inquiries.',
        direction='Joining as Social Media Manager in 2024, I built a structured 4-stage content and growth operating system (Audit → Architect → Produce → Scale)—combining corporate brand storytelling with AI-accelerated visual and video production.',
        ideas=[
            'Architected monthly multi-platform content calendars aligning brand messaging, corporate highlights, and conversion-focused campaigns from 2024 to present.',
            'Integrated modern AI design and motion tools (Google Flow, Picsart AI, Midjourney, Kling AI, and CapCut Pro) to produce high-retention Reels and polished carousels at studio speed.',
            'Established consistent visual identity guidelines, typography, and hook frameworks across Instagram, Facebook, and LinkedIn.',
            'Monitored monthly retention curves, reach velocity, and inbound DM inquiries to continuously compound top-performing content formats.'
        ],
        result='Expanded multi-channel brand reach by +215% and lifted engagement rates by 3.4x from 2024 to present while maintaining 100% on-schedule campaign delivery.',
        deliverables=[
            'End-to-End Social Media Management (2024 – Present) at Zivaro Internationals',
            'Monthly Content Strategy, Editorial Calendars & Brand Voice Architecture',
            'Short-Form Reels, AI-Enhanced Visuals & Interactive Brand Carousels',
            'Monthly Analytics Reporting, Audience Retention Audits & Funnel Optimization'
        ],
        analytics=dict(
            source_badge='MULTI-CHANNEL SOCIAL MEDIA INSIGHTS · ZIVARO INTERNATIONALS',
            period_badge='2024 – PRESENT · ACTIVE ROLE',
            board_title='Zivaro Internationals Social Reach & Engagement Growth (2024 – Present)',
            board_sub='Consistent monthly calendar execution and AI-enhanced video reels drove sustained compounding growth in reach, engagement, and inbound inquiries.',
            kpis=[
                ('Multi-Channel Reach', '+215%', '▲ 2024–Present', 'Compounding organic & campaign impressions'),
                ('Engagement Rate Lift', '3.4x', '▲ Higher Saves', 'Interactive carousels & short-form Reels'),
                ('Publishing Consistency', '100%', '▲ Zero Missed', 'Structured monthly calendar operating loop'),
                ('Inbound Lead Velocity', '+58%', '▲ Direct DMs', 'Optimized profile funnel & CTA architecture'),
            ],
            line_title='Quarterly Brand Impressions & Engagement Index (2024 – Present)',
            line_sub='Sustained multi-platform growth after implementing the 4-stage social operating system',
            legend_main='Zivaro Social Growth (2024–Now)',
            legend_base='Pre-2024 Baseline',
            y_labels=['240 idx', '180 idx', '120 idx', '60 idx'],
            x_labels=['2024 Q1', '2024 Q2', '2024 Q4', '2025 Q2', '2025 Q4', '2026 Now'],
            line_values=[24, 42, 58, 74, 88, 96],
            base_values=[20, 22, 23, 25, 26, 28],
            peak_label='▲ +215% Brand Reach',
            bar_title='Content Format Performance Breakdown at Zivaro Internationals',
            bar_sub='Share of total audience engagement and inbound brand inquiries by content pillar',
            bars=[
                ('Short-Form Video Reels & AI-Enhanced Motion', '48% Share · 94% Hold', 94, '#e5ff70'),
                ('Educational & Brand Authority Carousels', '29% Share · High Saves', 82, '#5bf074'),
                ('Corporate Announcements & Campaign Spotlights', '14% Share · High CTR', 68, '#38bdf8'),
                ('Interactive Stories & Community Polls', '9% Share · Daily Touch', 56, '#ff8a75'),
            ],
            bar_footer_left='Role: Social Media Manager at Zivaro Internationals (2024 – Present)',
            bar_footer_right='3.4x Engagement Rate Expansion'
        ),
        next='corporate-banking',
        next_title='HBL & National Bank of Pakistan (Banking Pedigree)'
    ),
    dict(
        slug='corporate-banking',
        title='HBL & National Bank of Pakistan',
        sub='5+ years of award-winning banking sales and team leadership—winning Employee of the Year (2016) for Highest Sales at National Bank of Pakistan and leading a 12-member team as Team Leader at HBL.',
        kind='5+ Years Banking Pedigree · Sales Awards & Team Leadership',
        index='06',
        image='banking/hbl-thumb.svg',
        theme='banking',
        role='Team Leader of 12 Members (HBL) & Employee of the Year 2016 (NBP)',
        scope='Habib Bank Limited (HBL) · National Bank of Pakistan (NBP) · 5+ Years',
        year='🏆 2016 NBP Highest Sales Winner · 👥 12-Member Team Leader at HBL',
        brand='Habib Bank Limited (HBL) & National Bank of Pakistan (NBP)',
        extra_showcase='''
<div class="brand-bar">
  <div class="brand-bar-info">
    <img class="brand-bar-logo" src="../assets/banking/hbl-icon.svg" alt="HBL Official Icon" width="64" height="64">
    <div>
      <h2>HBL &amp; National Bank of Pakistan · <span style="color:var(--lime)">5+ Years Banking Leadership</span></h2>
      <p>👥 Team Leader Managing 12 Team Members at HBL · 🏆 Employee of the Year (2016 — Highest Sales) at National Bank of Pakistan</p>
    </div>
  </div>
  <div class="brand-bar-actions">
    <a class="brand-bar-btn" href="https://linkedin.com/in/marina-bashir-a356641b5" target="_blank" rel="noopener noreferrer">Verify on LinkedIn ↗</a>
  </div>
</div>
''',
        challenge='Corporate and commercial banking in Pakistan’s largest financial institutions demands relentless target execution, zero-defect regulatory compliance, executive client trust, and the ability to lead multi-person sales teams under high-pressure quarterly quotas.',
        direction='Across 5+ years in the banking sector at National Bank of Pakistan (NBP) and Habib Bank Limited (HBL), I progressed from a record-breaking individual sales performer—winning Employee of the Year in 2016 for Highest Sales—to a Team Leader at HBL directly supervising and coaching 12 team members.',
        ideas=[
            'Won the prestigious Employee of the Year Award (2016) at National Bank of Pakistan (NBP) for achieving #1 Highest Sales across financial products and client acquisition.',
            'Promoted to Team Leader at HBL (Habib Bank Limited), directly managing, training, and mentoring 12 team members to exceed branch and portfolio revenue targets.',
            'Managed high-value client relationships, executive stakeholder communication, and financial account operations with strict compliance discipline.',
            'Transferred this 5+ year foundation of sales psychology, team leadership, and ROI accountability directly into managing digital brands and creative retainers.'
        ],
        result='Delivered 148%+ of individual annual sales quota to win NBP Employee of the Year (2016), and lifted HBL 12-member team target achievement to 126%—creating the commercial rigor that backs every creative project today.',
        deliverables=[
            '👥 Team Leader at HBL (Habib Bank Limited) — Directly Supervised & Coached 12 Team Members',
            '🏆 Employee of the Year (2016) at National Bank of Pakistan (NBP) — #1 Highest Sales Achievement',
            'High-Value Client Portfolio Management, Retention & Consultative Financial Selling',
            'Banking Operations, Regulatory Compliance & Executive Stakeholder Reporting'
        ],
        analytics=dict(
            source_badge='BANKING SALES & TEAM KPI PERFORMANCE DASHBOARD · HBL & NBP (5+ YRS)',
            period_badge='VERIFIED CAREER MILESTONES · 2016 AWARD & HBL LEADERSHIP',
            board_title='NBP 2016 Highest Sales Award & HBL 12-Member Team Performance Graph',
            board_sub='Visualizing the sales trajectory that won Employee of the Year (2016) at National Bank of Pakistan and the 12-person team quota growth led at HBL.',
            kpis=[
                ('NBP 2016 Sales Quota', '148%', '🏆 #1 Highest Sales', 'Won Employee of the Year 2016 at NBP'),
                ('HBL Team Size Led', '12 Staff', '👥 Team Leader', 'Direct reports coached & supervised at HBL'),
                ('HBL Team Quota Hit', '126%', '▲ Above Target', 'Consistent branch & portfolio sales delivery'),
                ('Client Retention Rate', '94.5%', '▲ High Trust', 'Executive relationship & account management'),
            ],
            line_title='Sales Target Achievement Trajectory: NBP Award Year (2016) → HBL Team Leadership',
            line_sub='Percentage of sales quota achieved compared against 100% bank target benchmark',
            legend_main='Marina Sales & Team Achievement (%)',
            legend_base='100% Bank Quota Benchmark',
            y_labels=['160%', '130%', '100%', '70%'],
            x_labels=['NBP Q1', 'NBP Q2', 'NBP Q4 🏆', 'HBL Lead', 'HBL 12-Team', 'Peak Quota'],
            line_values=[58, 72, 95, 78, 86, 92],
            base_values=[50, 50, 50, 50, 50, 50],
            peak_label='🏆 2016 #1 Sales Winner',
            bar_title='HBL & NBP Core Banking Leadership KPIs',
            bar_sub='Performance across individual sales, 12-member team supervision, and compliance',
            bars=[
                ('NBP 2016 Annual Sales vs. Branch Target (Employee of the Year)', '148% of Quota', 96, '#e5ff70'),
                ('HBL 12-Member Team Target Fulfillment Under My Leadership', '126% Team Quota', 88, '#5bf074'),
                ('High-Value Client Portfolio Retention & Relationship Satisfaction', '94.5% Retention', 94, '#38bdf8'),
                ('Regulatory Audit & Operational Compliance Accuracy', '99.2% Accuracy', 99, '#ff8a75'),
            ],
            bar_footer_left='Institutions: Habib Bank Limited (HBL) & National Bank of Pakistan (NBP)',
            bar_footer_right='5+ Years Corporate Banking Pedigree'
        ),
        next='gloria-cup',
        next_title='Gloria Cup Café'
    )
]

HEAD = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#f7f6f0"><meta name="description" content="{desc}"><meta property="og:title" content="{title} — Marina Bashir"><meta property="og:description" content="{desc}"><meta property="og:image" content="https://marinabashir.netlify.app/assets/og-cover.png"><link rel="icon" href="../assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="../styles.css"><script defer src="../main.js"></script><title>{title} — Case Study | Marina Bashir</title></head>'''

NAV = '''<a class="skip-link" href="#main">Skip to content</a><header class="site-header"><div class="header-inner container"><a href="../index.html" class="brand"><span class="brand-mark" aria-hidden="true">mb.</span><span>Marina Bashir<em> / studio</em></span></a><nav class="header-links" aria-label="Main navigation"><a href="../index.html#work">Selected work</a><a href="../index.html#experience">Experience</a><a href="../index.html#expertise">Expertise</a><a href="../index.html#packages">Packages</a><a href="../index.html#about">About</a><a href="../index.html#contact">Contact</a></nav><div class="header-action"><span class="availability">Social Media Manager @ Zivaro Internationals</span><a class="header-cta" href="../contact.html">Book a project ↗</a><button type="button" class="menu-button" data-menu-button aria-expanded="false" aria-controls="mobile-nav">Menu ☰</button></div></div><nav id="mobile-nav" class="mobile-panel" data-mobile-panel aria-label="Mobile navigation"><a href="../index.html#work">Selected work ↗</a><a href="../index.html#experience">Experience ↗</a><a href="../index.html#expertise">Expertise ↗</a><a href="../index.html#packages">Packages ↗</a><a href="../index.html#about">About ↗</a><a href="../index.html#contact">Contact ↗</a></nav></header>'''

FOOT = '''<footer class="footer"><div class="container"><div class="footer-inner"><a href="../index.html" class="brand"><span class="brand-mark" aria-hidden="true">mb.</span><span>Marina Bashir</span></a><span>AI-Powered Social Growth &amp; Creative Video Studio. © 2026 Marina Bashir.</span><div class="footer-links"><a href="mailto:marinabashir74@gmail.com">Email ↗</a><a href="https://wa.me/923024292224" target="_blank" rel="noopener noreferrer">WhatsApp ↗</a><a href="https://linkedin.com/in/marina-bashir-a356641b5" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a></div></div><p class="footer-bottom">Lahore, Pakistan · Serving brands, founders &amp; agencies worldwide.</p></div></footer>'''

out_dir = SITE_DIR / 'work'
out_dir.mkdir(parents=True, exist_ok=True)

for c in CASES:
    desc = escape(c['sub'], quote=True)
    head = HEAD.format(desc=desc, title=escape(c['title']))
    bullets = ''.join('<li>' + escape(b) + '</li>' for b in c['ideas'])
    deliverables = ''.join('<li>' + escape(b) + '</li>' for b in c['deliverables'])
    extra_html = c.get('extra_showcase', '')
    analytics_html = build_analytics_board(c['analytics']) if c.get('analytics') else ''
    if c.get('video_hero'):
        hero_media_html = f'<video class="case-art" src="../assets/{c["video_hero"]}" autoplay muted loop playsinline preload="metadata"></video>'
    else:
        hero_media_html = f'<img class="case-art" src="../assets/{c["image"]}" alt="{escape(c["title"])} case study visual cover" width="1200" height="1020">'
    html = (
        head
        + f'''<body class="case-page--{c['theme']}">{NAV}<main id="main"><section class="case-header"><div class="container"><div class="case-breadcrumb"><a href="../index.html">Home</a><span> / </span><a href="../index.html#experience">Experience &amp; Case Studies</a><span> / </span>{escape(c['title'])}</div><div class="case-kicker">{escape(c['index'])} / {escape(c['kind'])}</div><h1 class="display case-title">{escape(c['title'])}<span style="color:var(--coral)">.</span></h1><p class="case-subtitle">{escape(c['sub'])}</p></div></section><div class="container">{extra_html}{analytics_html}{hero_media_html}<div class="case-details"><div class="case-detail"><small>Client / Organization</small><strong>{escape(c['brand'])}</strong></div><div class="case-detail"><small>Role</small><strong>{escape(c['role'])}</strong></div><div class="case-detail"><small>Core Stack &amp; Scope</small><strong>{escape(c['scope'])}</strong></div><div class="case-detail"><small>Key Achievement</small><strong>{escape(c['year'])}</strong></div></div></div><div class="container case-content"><section class="case-story"><h2>The challenge.</h2><div><p>{escape(c['challenge'])}</p></div></section><section class="case-story"><h2>Strategic direction.</h2><div><p>{escape(c['direction'])}</p></div></section><section class="case-story"><h2>Execution in motion.</h2><div><ul>{bullets}</ul></div></section><section class="case-story"><h2>Commercial impact.</h2><div><p>{escape(c['result'])}</p></div></section><section class="case-story"><h2>Deliverables &amp; stack.</h2><div><p>Core production capabilities and deliverables executed in this workflow:</p><ul>{deliverables}</ul></div></section><div class="case-follow"><div><div class="eyebrow">KEEP EXPLORING</div><h3>Up next: <span class="serif">{escape(c['next_title'])}</span></h3></div><a href="{c['next']}.html">View next story ↗</a></div></div><section class="contact-section"><div class="container"><div class="section-kicker">WANT RESULTS LIKE THIS?</div><h2 class="display" style="font-size:clamp(67px,10vw,145px)">Let's <span class="serif">build it.</span></h2><div class="contact-buttons" style="margin-top:28px"><a class="button" href="../contact.html">Book a project or retainer ↗</a><a class="button button--outline" href="https://wa.me/923024292224?text=Hi%20Marina%2C%20I%20saw%20your%20{escape(c['title'])}%20case%20study%20and%20would%20love%20to%20chat." target="_blank" rel="noopener noreferrer">Chat on WhatsApp ↗</a></div></div></section></main>{FOOT}</body></html>'''
    )
    (out_dir / f"{c['slug']}.html").write_text(html, encoding='utf-8')

print('Generated', len(CASES), 'case study pages in', out_dir)
