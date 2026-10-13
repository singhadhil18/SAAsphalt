"""One-off pages: home, services, about, projects, contact, quote, community, privacy, 404."""
from html import escape as e

import content as C
from build import (bars, clients_chips, cta, gallery3, icon, img, link_buttons, media, page, service_card,
                   split, strip, tick, ticks, wa_button, wa_link, ROOT)

AREA = C.AREA


def home():
    home_cards = "".join(service_card(s, home=True) for s in C.SERVICES if s["home"])
    pills = [(f'{s["slug"]}.html', s["home_title"]) for s in C.SERVICES if not s["home"]]
    pills.insert(1, ("quote.html?service=Tar+Shield+Coating", "Tar Shield Coating"))
    pills.insert(5, ("quote.html?service=Traffic+Calming", "Traffic Calming"))
    pill_html = "".join(f'<a class="chip chip-light" href="{href}">{e(label)}</a>' for href, label in pills)
    sectors = [("home", "Homes & driveways", "Residential"), ("building", "Businesses & carparks", "Commercial"),
               ("gear", "Industrial sites", "Heavy-duty"), ("school", "Schools", "Education"), ("cross", "Hospitals", "Healthcare")]
    sector_html = "".join(
        f'<div class="sector"><span class="icon-dot">{icon(i)}</span><h3>{t}</h3><p>{d}</p></div>' for i, t, d in sectors)
    features = [("check", "SABS-approved materials", "Correct grades selected for the job."),
                ("star", "Experienced team", "Skilled staff from office to site."),
                ("gear", "Modern equipment", "Machinery suited to proper preparation and compaction."),
                ("swap", "Hands-on management", "Clear communication and quality oversight.")]
    feature_html = "".join(
        f'<div class="card icon-card"><span class="icon-dot">{icon(i)}</span><div><h3>{t}</h3><p>{d}</p></div></div>' for i, t, d in features)

    body = f"""<section class="hero hero-home">
  <div class="hero-media">{img("home-hero.jpg", "SA Asphalt team rolling a new residential driveway", lazy=False)}</div>
  <div class="wrap"><div class="hero-copy">
    <span class="eyebrow" style="color:#fff">Professional asphalt &amp; paving contractors in the {AREA}</span>
    {bars()}
    <h1>Built to last. <span class="red">Quality you can see.</span></h1>
    <p>SA Asphalt delivers professional asphalt, paving and exterior works for residential, commercial and industrial properties across the {AREA}.</p>
    <div class="btn-row">
      <a class="btn btn-red" href="services.html">Our Services &rarr;</a>
      {wa_button()}
      <a class="btn btn-outline" href="projects.html">View Projects</a>
    </div>
    <div class="hero-tags"><span>Local experts</span><span>Quality work</span><span>Built to last</span></div>
  </div></div>
</section>
{strip(["Quality workmanship", "20+ years industry experience", "Right equipment", C.AREA_SHORT])}
{split(media("home-driveway.jpg", "Domestic asphalt driveway curving past a garden", "Domestic driveway"),
       f'''<span class="eyebrow">Durban's trusted asphalt specialists</span>
  <h2>Proper preparation. <span class="red">Professional finish.</span></h2>
  <p class="muted">Through hard work, attention to detail and a commitment to quality workmanship, SA Asphalt has built a strong reputation in the asphalt paving industry.</p>
  <p class="muted">We work across residential, commercial and industrial environments, delivering everything from new installations to resurfacing, repairs and complete exterior upgrades.</p>
  <div class="callout">Proper preparation. Quality materials. Professional workmanship. No shortcuts.</div>
  {ticks(["SABS-approved materials", "Experienced team", "Hands-on management", "Clear communication"])}''')}
<section class="half half-dark half-flip">
  <div class="half-copy">
    <span class="eyebrow">Repairs that address the problem</span>
    <h2>Stop patching. <span class="red" style="display:block">Start fixing.</span></h2>
    <p>Cracks, potholes and failing asphalt don't repair themselves. Left untreated, small problems can become larger and more expensive.</p>
    <div class="chips"><span class="chip">Potholes</span><span class="chip">Cracking</span><span class="chip">Surface failure</span><span class="chip">Water damage</span></div>
    <p><strong style="color:#fff">SA Asphalt focuses on long-term, cost-effective solutions rather than temporary repairs.</strong></p>
    <div class="btn-row"><a class="btn btn-green" href="{wa_link("Hi SA Asphalt, here are photos of the area that needs repair.")}" target="_blank" rel="noopener">Send photos on WhatsApp</a></div>
  </div>
  <div class="half-media">{img("chicken-licken.jpg", "Repaired asphalt at the Chicken Licken entrance", cls="zoomable", caption="Chicken Licken entrance repair")}</div>
</section>
<section class="section section-light" id="services"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Residential &bull; Commercial &bull; Industrial</span><h2>Our <span class="red">services</span></h2><p>Select a service to explore the work we carry out across the {AREA}.</p></div>
  <div class="svc-grid">{home_cards}</div>
  <hr class="svc-rule">
  <div class="chips chips-center">{pill_html}</div>
</div></section>
<section class="half half-dark">
  <div class="half-media">{img("home-residential.jpg", "Long asphalt driveway leading up to a house", cls="zoomable")}</div>
  <div class="half-copy">
    <span class="eyebrow">Residential services</span>
    <h2>Because your home deserves a <span class="red">driveway built to last.</span></h2>
    <p>A professionally surfaced driveway improves more than appearance. Correct preparation, drainage and surfacing contribute to durability, usability and long-term property value.</p>
    {ticks(["Asphalt driveways", "Paved driveways", "Entrance areas & pathways", "Drainage & retaining systems", "Precast fencing"], "list-ticks")}
    <a class="btn btn-green btn-block" href="quote.html?service=Asphalt+Driveways">Get a Residential Quote</a>
  </div>
</section>
<section class="half half-flip">
  <div class="half-copy">
    <span class="eyebrow">Commercial &amp; industrial</span>
    <h2>Surfacing solutions <span class="red">built for business.</span></h2>
    <p class="muted">From parking areas and access roads to industrial yards and repair work, SA Asphalt delivers professional surfacing solutions for commercial and industrial sites, including Crompton Hospital, Woolworths, Chelsea School and Enviroserv.</p>
    {ticks(["Office parks & retail properties", "Warehouses & loading areas", "Schools & education facilities", "Hospitals & healthcare sites", "Industrial premises"], "list-ticks")}
    <a class="btn btn-red btn-block" href="quote.html?service=Commercial+%26+Industrial+Asphalt">Discuss Your Project</a>
  </div>
  <div class="half-media">{img("home-commercial.jpg", "Newly surfaced hospital entrance road with a safety mirror", cls="zoomable")}</div>
</section>
<section class="section section-dark"><div class="wrap">
  <div class="split" style="align-items:end;margin-bottom:28px">
    <div><span class="eyebrow">Before &amp; after</span><h2 class="big-title" style="margin:0">Projects. <span class="red">Proven results.</span></h2></div>
    <p class="muted" style="margin:0">See the difference proper preparation and professional workmanship can make.</p>
  </div>
  <div class="ba" data-lightbox-group="home-ba">
    <figure>{img("home-before.jpg", "Failed asphalt and exposed pothole before repair", caption="Before: Chicken Licken entrance")}<span class="badge">Before</span></figure>
    <figure>{img("chicken-licken.jpg", "Completed repair at the Chicken Licken entrance", caption="After: Chicken Licken entrance")}<span class="badge badge-after">After</span></figure>
  </div>
  <p class="ba-caption">Chicken Licken &mdash; entrance &amp; carpark repair project</p>
</div></section>
{split(img("home-quality.jpg", "Finished asphalt driveway at a residential property", cls="zoomable"),
       f'''<span class="eyebrow">Quality control</span>
  <h2>Quality is the <span class="red">foundation of our work.</span></h2>
  <p class="muted">Every project is managed with attention to preparation, materials, workmanship and finish. Quality control is central to how SA Asphalt works.</p>
  <div class="feature-grid">{feature_html}</div>''')}
<section class="section section-dark"><div class="wrap split">
  <div class="mosaic" data-lightbox-group="surface">
    {img("spca-road.jpg", "Newly surfaced road with centre line marking")}
    {img("bobcat.jpg", "Bobcat preparing the ground")}
    {img("home-surface-3.jpg", "Completed asphalt surface outside a home")}
  </div>
  <div>
    <span class="eyebrow">Site preparation &amp; earthworks</span>
    <h2>A great surface <span class="red">starts underneath.</span></h2>
    <p class="muted">The finished asphalt is only as good as its foundation. We consider levels, grading, drainage, soil conditions, vegetation and base preparation before the final surface is installed.</p>
    <ol class="num-list"><li>Assess levels, drainage and site conditions</li><li>Clear, grade and prepare the base correctly</li><li>Compact and surface using suitable equipment</li></ol>
  </div>
</div></section>
{split(img("svc-precast.jpg", "Dark grey precast boundary fence", cls="zoomable"),
       f'''<span class="eyebrow">Additional exterior works</span>
  <h2>Precast fencing &amp; <span class="red">boundary walls.</span></h2>
  <p class="muted">SA Asphalt installs durable precast fencing and boundary-wall systems for residential and commercial properties.</p>
  <p class="muted">Available in a range of finishes and styles, precast fencing provides a practical, low-maintenance solution for privacy, security and property boundaries.</p>
  {ticks(["Brick-pattern finishes", "Horizontal panel systems", "Residential boundaries", "Commercial properties"])}
  <div class="btn-row" style="margin-top:24px"><a class="btn btn-red" href="quote.html?service=Precast+Fencing">Get a Precast Fence Quote</a></div>''', flip=True)}
<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Where we work</span><h2 class="big-title">Residential &bull; Commercial &bull; Industrial</h2><p>Flexible capability across small and large projects, with project examples in homes, business premises, schools and healthcare sites.</p></div>
  <div class="sectors">{sector_html}</div>
</div></section>
<section class="section section-light"><div class="wrap">
  <div class="section-head"><span class="eyebrow red">Projects completed</span><h2>Trusted across the {AREA}</h2><p>A selection of the hospitals, schools, retailers and businesses SA Asphalt has completed work for.</p></div>
  {clients_chips()}
  <!-- Google Reviews widget: connect the live Google Reviews embed here once the site is deployed. -->
</div></section>
<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Follow our work</span><h2>See our <span class="red">latest projects</span></h2><p>Recent SA Asphalt project photography from across the {AREA}.</p></div>
  <div class="thumbs" data-lightbox-group="latest">
    {img("svc-paving.jpg", "Paving installation in progress", cls="zoomable")}
    {img("home-surface-3.jpg", "Completed asphalt surface outside a home", cls="zoomable")}
    {img("home-commercial.jpg", "Hospital entrance road", cls="zoomable")}
    {img("precast-brown.jpg", "Brick-pattern precast fence", cls="zoomable")}
  </div>
  <div class="btn-row" style="margin-top:22px"><a class="btn btn-outline-dark" href="projects.html">View Projects</a><a class="btn btn-outline-dark" href="quote.html">Get a Quote</a></div>
</div></section>
<section class="cta cta-red"><div class="wrap">
  <div><span class="eyebrow" style="color:#fff">Fast quotation</span><h2>Need asphalt, paving or exterior work?</h2><p>Send us photos of the area, your location and an approximate size. We'll review the project requirements and get back to you with the next step.</p></div>
  <div class="btn-col">{wa_button()}<a class="btn btn-outline" href="tel:{C.OFFICE_TEL}">Call {C.OFFICE}</a></div>
</div></section>"""
    return page("index.html", "SA Asphalt | Asphalt, Paving & Exterior Works in the Durban Metropolitan Area",
                f"SA Asphalt delivers professional asphalt, paving and exterior works for residential, commercial and industrial properties across the {AREA}.",
                body, active="index.html")


def services():
    cards = "".join(service_card(s, show_desc=True) for s in C.SERVICES)
    body = f"""<section class="hero">
  <div class="hero-media">{img("services-hero.jpg", "Newly surfaced road with kerbing", lazy=False)}</div>
  <div class="wrap"><div class="hero-copy">
    <span class="eyebrow">Professional asphalt, paving &amp; exterior works</span>
    <h1>Our <span class="red" style="display:inline">Services</span></h1>
    {bars()}
    <p>From residential driveways to commercial carparks, repairs, paving, drainage and supporting exterior works, SA Asphalt delivers practical solutions across the {AREA}.</p>
    <div class="btn-row"><a class="btn btn-green" href="quote.html">Get a Free Quote</a><a class="btn btn-outline" href="#range">View Services</a></div>
  </div></div>
</section>
{strip(["Residential", "Commercial", "Industrial", C.AREA_SHORT])}
<section class="section section-light" id="range"><div class="wrap">
  <div class="section-head"><h2>Complete <span class="red">service range</span></h2><p>Core asphalt and paving services lead the offering, supported by drainage, line marking, retaining walls, precast fencing, earthworks and finishing services.</p></div>
  <div class="svc-grid">{cards}</div>
</div></section>
<section class="section section-dark"><div class="wrap split split-flip">
  <div class="split-media">{img("about-hero.jpg", "SA Asphalt team raking and levelling new asphalt", cls="zoomable")}</div>
  <div>
    <h2>Proper preparation. <span class="red">Professional finish.</span></h2>
    <p class="muted">SA Asphalt's approach considers levels, drainage, soil conditions, clearing and base preparation before the finished surface is installed.</p>
    {ticks(["SABS-approved materials", "Experienced on-site teams", "Modern machinery & tools", "Hands-on management"])}
  </div>
</div></section>
{cta("Not sure which service you need?", "Send photographs of the area on WhatsApp and tell us what you want to achieve. We can guide the next step.", wa_button())}"""
    return page("services.html", "Our Services | SA Asphalt",
                f"Asphalt driveways, carparks, repairs, resurfacing, paving, drainage, line marking and exterior works across the {AREA}.",
                body, active="services.html", trail=[("index.html", "Home"), (None, "Services")])


def about():
    body = f"""<section class="hero hero-full">
  <div class="hero-media">{img("about-hero.jpg", "SA Asphalt team laying a new driveway", lazy=False)}</div>
  <div class="wrap"><div class="hero-copy">
    <div class="crumb-inline"><a href="index.html">Home</a> / About</div>
    <span class="eyebrow">About SA Asphalt</span>
    <h1 class="upper">Proper preparation.<br>Professional finish.</h1>
    <p>SA Asphalt delivers asphalt, paving, repair and supporting exterior works for residential, commercial and industrial properties across the {AREA}.</p>
    <div class="btn-row"><a class="btn btn-green" href="projects.html">View Projects</a><a class="btn btn-outline" href="quote.html">Get a Quote</a></div>
  </div></div>
</section>
{split(img("about-quality.jpg", "Finished asphalt courtyard beside a white boundary wall", cls="zoomable"),
       f'''<span class="eyebrow">How we work</span>
  <h2>Quality starts underneath</h2>
  <p class="muted">Established in 2003, SA Asphalt has built its reputation around professional asphalt surfacing, repairs, paving and exterior works across the {AREA}.</p>
  <div class="callout">A durable finish depends on what happens before the final layer goes down.</div>
  {ticks(["Residential work", "Commercial work", "Industrial work", "Repairs"])}''')}
<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Our working principles</span><h2>What clients can expect</h2></div>
  <div class="cards-3">
    <div class="card"><h3>Site-first thinking</h3><p>We look at access, existing levels, water movement, edges and how the proposed work connects to the property.</p></div>
    <div class="card"><h3>Projects completed</h3><ul class="clients-plain">{"".join(f"<li>{e(c)}</li>" for c in C.CLIENTS[:12])}</ul></div>
    <div class="card"><h3>Complete exterior capability</h3><p>Core surfacing is supported by drainage, curbing, pathways, earthworks, retaining, fencing and finishing services.</p></div>
  </div>
</div></section>
<section class="section section-light"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Selected SA Asphalt work</span><h2>Project experience across the {AREA}</h2><p>Residential, commercial and supporting exterior works completed by SA Asphalt.</p></div>
  {gallery3([("kerb-driveway.jpg", "New asphalt with kerbing beside a fence"), ("about-exp-2.jpg", "Asphalt forecourt at a school building"), ("services-hero.jpg", "Kerbed road surfacing")], "about")}
</div></section>
<section class="section section-dark"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Service range</span><h2>One team for the surrounding works</h2><p>From preparation to the final edges and markings, the service range is designed to reduce gaps between trades and create a more complete result.</p></div>
  {link_buttons([("services.html", "View all services"), ("projects.html", "View project gallery"), ("quote.html", "Request a quote")])}
</div></section>
{cta(f"Planning work in the {AREA}?", "Send the site details and photographs and we can start the quotation process.",
     '<a class="btn btn-red" href="quote.html">Get a Quote</a><a class="btn btn-green" href="contact.html">Contact Us</a>')}"""
    return page("about.html", "About SA Asphalt | Established 2003",
                f"Established in 2003, SA Asphalt delivers asphalt, paving and exterior works across the {AREA}.",
                body, active="about.html")


def projects():
    cards = [("home-driveway.jpg", "Residential driveway"), ("commercial-garages.jpg", "Commercial surfacing"),
             ("carpark-arrow.jpg", "Carpark work"), ("svc-paving.jpg", "Paving"), ("precast-brown.jpg", "Precast fencing"),
             ("spca-road.jpg", "Line marking"), ("earthworks-bobcat.jpg", "Earthworks"), ("svc-pathways.jpg", "Pathways")]
    card_html = "".join(f'<div class="proj-card">{img(src, t)}<h3>{e(t)}</h3></div>' for src, t in cards)
    feed = ["home-hero.jpg", "svc-carparks.jpg", "svc-paving.jpg", "svc-commercial.jpg", "roller-gallery.jpg", "home-driveway.jpg"]
    feed_html = "".join(img(f, "SA Asphalt project photo", cls="zoomable") for f in feed)
    body = f"""<section class="hero">
  <div class="hero-media">{img("projects-hero.jpg", "Resurfaced hospital carpark", lazy=False)}</div>
  <div class="wrap"><div class="hero-copy">
    <span class="eyebrow">Project portfolio</span>
    <h1 style="text-transform:none">Projects / Before &amp; After</h1>
    <p>A photo-led look at completed SA Asphalt projects across asphalt, paving, surfacing, fencing and supporting exterior works.</p>
    <div class="btn-row">
      <a class="btn btn-green" href="quote.html">Get a Quote</a>
      <a class="btn btn-white" href="{wa_link()}" target="_blank" rel="noopener">WhatsApp Us</a>
      <a class="btn btn-red" href="tel:{C.MOBILE_TEL}">Call {C.MOBILE}</a>
    </div>
  </div></div>
</section>
<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow red">Before &amp; after</span><h2 style="text-transform:none">Asphalt Repair</h2><div class="title-rule"></div></div>
  <div class="ba" data-lightbox-group="ba">
    <figure>{img("ba1-before.jpg", "Driveway area before surfacing", cls="zoomable", caption="Before")}<span class="badge">Before</span></figure>
    <figure>{img("ba1-after.jpg", "The same driveway after surfacing", cls="zoomable", caption="After")}<span class="badge badge-after">After</span></figure>
    <figure class="ba-wide">{img("ba2-composite.jpg", "Driveway before and after resurfacing", cls="zoomable")}</figure>
  </div>
</div></section>
<section class="section section-light"><div class="wrap">
  <div class="section-head"><span class="eyebrow red">Across our service range</span><h2 style="text-transform:none">Project Gallery</h2><div class="title-rule"></div></div>
  <div class="proj-grid" data-lightbox-group="projects">{card_html.replace('<img ', '<img class="zoomable" ')}</div>
</div></section>
<section class="section section-dark"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Projects completed</span><h2>Clients we have worked for</h2></div>
  {clients_chips()}
</div></section>
<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow red">Follow our work</span><h2 style="text-transform:none">Instagram Project Feed</h2><p>Recent project photography from SA Asphalt.</p></div>
  <!-- Instagram feed: replace these photos with the live SA Asphalt Instagram embed once the account is connected. -->
  <div class="thumbs thumbs-6" data-lightbox-group="feed">{feed_html}</div>
</div></section>
{cta("Need asphalt, paving or exterior work?", "Send us the location, approximate size and photographs of the area for a fast first assessment.",
     '<a class="btn btn-green" href="quote.html">Get a Quote</a>' + wa_button(f"WhatsApp {C.MOBILE}", "btn-white"))}"""
    return page("projects.html", "Projects / Before & After | SA Asphalt",
                "A photo-led look at completed SA Asphalt projects across asphalt, paving, surfacing, fencing and supporting exterior works.",
                body, active="projects.html")


def contact():
    body = f"""<section class="hero hero-full">
  <div class="hero-media">{img("contact-hero.jpg", "Newly surfaced residential driveway", lazy=False)}</div>
  <div class="wrap"><div class="hero-copy">
    <div class="crumb-inline"><a href="index.html">Home</a> / Contact</div>
    <span class="eyebrow">Contact SA Asphalt</span>
    <h1 class="upper">Talk to our team</h1>
    <p>For new quotations, site assessments, repairs or general enquiries, contact SA Asphalt by phone, WhatsApp or email.</p>
    <div class="btn-row">{wa_button("WhatsApp")}<a class="btn btn-outline" href="tel:{C.MOBILE_TEL}">Call {C.MOBILE}</a></div>
  </div></div>
</section>
<section class="section section-light"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Get in touch</span><h2>Choose the easiest way to contact us</h2></div>
  <div class="cards-3 contact-cards">
    <div class="card"><h3>Phone</h3><a href="tel:{C.MOBILE_TEL}">{C.MOBILE}</a><a href="tel:{C.OFFICE_TEL}">{C.OFFICE}</a><p>Call to discuss the type of work, location and the best next step.</p></div>
    <div class="card"><h3>WhatsApp</h3><a href="{wa_link()}" target="_blank" rel="noopener">Open WhatsApp</a><p>Useful for sending photographs of the driveway, pothole, parking area, fence or site.</p></div>
    <div class="card"><h3>Email</h3><a href="mailto:{C.EMAIL}">{C.EMAIL}</a><p>Email plans, scope details, photographs and supporting information for quotation.</p></div>
  </div>
</div></section>
<section class="section"><div class="wrap split split-flip">
  <div class="split-media">{media("crompton-entrance.jpg", "Entrance to The Crompton Hospital with new surfacing", "Crompton Hospital")}</div>
  <div>
    <span class="eyebrow">Service area</span>
    <h2>{C.AREA_SHORT}</h2>
    <p class="muted">SA Asphalt provides residential, commercial and industrial asphalt, paving and supporting exterior works across the {AREA}.</p>
    {ticks(["Asphalt & resurfacing", "Paving & pathways", "Drainage & earthworks", "Fencing & finishing"])}
  </div>
</div></section>
{cta("Use our Get-a-Quote page", "Give us the project type, area and site details in one quick form.", '<a class="btn btn-red" href="quote.html">Get a Quote</a>')}"""
    return page("contact.html", "Contact SA Asphalt", f"Contact SA Asphalt by phone, WhatsApp or email. Serving the {AREA}.",
                body, active="contact.html")


def quote():
    options = "".join(f'<option>{e(s["title"])}</option>' for s in C.SERVICES)
    options += "<option>Tar Shield Coating</option><option>Traffic Calming</option><option>Other / not sure</option>"
    body = f"""<section class="hero hero-full">
  <div class="hero-media">{img("quote-hero.jpg", "SA Asphalt crew surfacing a driveway with a bobcat", lazy=False, style="object-position:50% 40%")}</div>
  <div class="wrap"><div class="hero-copy">
    <div class="crumb-inline"><a href="index.html">Home</a> / Get a Quote</div>
    <span class="eyebrow">Free quotation request</span>
    <h1 class="upper">Tell us about your project</h1>
    <p>Complete the form below and it will prepare a WhatsApp message with your project details for SA Asphalt.</p>
    <div class="btn-row"><a class="btn btn-green" href="#quote">Start Quote Request</a><a class="btn btn-outline" href="tel:{C.MOBILE_TEL}">Call Instead</a></div>
  </div></div>
</section>
<section class="section section-light" id="quote"><div class="wrap quote-layout">
  <aside class="quote-aside">
    <span class="eyebrow">Before you send</span>
    <h2>Photographs help us assess the job faster</h2>
    <p>After sending the form, attach a few clear photographs in WhatsApp. For larger work we can arrange a site assessment where required.</p>
    <a class="contact-row" href="tel:{C.MOBILE_TEL}">Call: {C.MOBILE}</a>
    <a class="contact-row" href="tel:{C.OFFICE_TEL}">Office: {C.OFFICE}</a>
    <a class="contact-row" href="mailto:{C.EMAIL}">Email: {C.EMAIL}</a>
  </aside>
  <form class="form-card" id="quote-form" novalidate>
    <div class="form-grid">
      <div class="field"><label for="f-name">Name *</label><input id="f-name" name="name" required autocomplete="name"></div>
      <div class="field"><label for="f-phone">Phone / WhatsApp *</label><input id="f-phone" name="phone" type="tel" required autocomplete="tel"></div>
      <div class="field"><label for="f-location">Site location / suburb *</label><input id="f-location" name="location" required></div>
      <div class="field"><label for="f-service">Service *</label><select id="f-service" name="service" required><option value="">Choose a service</option>{options}</select></div>
      <div class="field"><label for="f-size">Approx. area / size</label><input id="f-size" name="size" placeholder="e.g. 120 m&sup2; or 30 m driveway"></div>
      <div class="field"><label for="f-timing">Preferred timing</label><select id="f-timing" name="timing"><option>As soon as possible</option><option>Within the next month</option><option>In 1&ndash;3 months</option><option>Just looking for pricing</option></select></div>
      <div class="field full"><label for="f-details">Project details *</label><textarea id="f-details" name="details" required placeholder="Tell us what work is needed, current surface condition, access issues or anything else we should know."></textarea></div>
    </div>
    <p class="form-error" role="alert">Please complete the required fields marked *.</p>
    <button class="btn btn-green btn-block" type="submit" style="margin-top:18px">Prepare WhatsApp Quote Request</button>
    <p class="form-note">This website does not store your form details. When you submit, WhatsApp opens with the information pre-filled for you to send to SA Asphalt.</p>
  </form>
</div></section>
<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Need help choosing?</span><h2>Browse the full service range</h2><p>Our Services page explains both the core asphalt services and supporting exterior work.</p></div>
  {link_buttons([("services.html", "View all services"), ("projects.html", "See projects"), ("contact.html", "Contact SA Asphalt")])}
</div></section>"""
    return page("quote.html", "Get a Free Quote | SA Asphalt",
                f"Request a free asphalt, paving or exterior works quotation from SA Asphalt in the {AREA}.",
                body, active=None, trail=None)


COMMUNITY = [
    ("Parks & public spaces", "Durban North Swimming Pool Park", "The SA Asphalt team helping revamp a local public space."),
    ("Planting & greening", "Broadway cleaning & greening", "Hands-on planting and care for our neighbourhood."),
    ("Community support", "Working together for Ward 36", "Ellysa Entwistle and Bongeka working together in the community."),
    ("Clean-ups", "Mandela Day with DSW", "Working together with DSW on a community clean-up."),
    ("Clean-ups", "Beachwood Mangroves clean-up", "Smiles all round while helping care for this local natural area."),
    ("Clean-ups", "A hands-on approach", "Getting involved in clearing litter from our shared spaces."),
    ("Planting & greening", "Virginia Circle upliftment", "The SA Asphalt team planting trees as part of a local upliftment project."),
    ("Planting & greening", "Skills upliftment & tree planting", "Working together and sharing practical skills through community work."),
    ("Planting & greening", "Working with the Parks Department", "Selecting appropriate trees for community planting."),
    ("Parks & public spaces", "Whynotte Park, Umhlanga Rocks", "Installing bollards around the park."),
    ("Parks & public spaces", "Painting Durban North bus stops", "Giving everyday public spaces a colourful refresh."),
    ("Parks & public spaces", "Colour in our public spaces", "A completed bus-stop mural celebrating nature."),
    ("Planting & greening", "Local church verge planting", "Helping uplift the area through planting."),
    ("Planting & greening", "Caring for neighbourhood verges", "Hands-on maintenance of a planted roadside verge."),
    ("Clean-ups", "The team at work", "Clearing vegetation and loading garden material."),
    ("Clean-ups", "Clearing & collecting", "Supporting a neighbourhood clean-up with practical work."),
    ("Community support", "Briardene flood support", "Meeting with Ms Magwaza to assist during the floods."),
    ("Community support", "Smile and Wave & Marshall Security", "Working together with local community partners."),
    ("Planting & greening", "Neighbourhood planting", "A closer look at a planted verge."),
    ("Parks & public spaces", "Caring for shared spaces", "The team at work around a paved public area."),
]


def community():
    cats = ["Clean-ups", "Planting & greening", "Parks & public spaces", "Community support"]
    filters = '<button class="filter" data-filter="all" aria-pressed="true">All work</button>' + "".join(
        f'<button class="filter" data-filter="{e(c)}" aria-pressed="false">{e(c)}</button>' for c in cats)
    cards = "".join(
        f'<article class="comm-card" data-cat="{e(cat)}"><button type="button" aria-label="View photo: {e(title)}">'
        f'{img(f"community-{i:02d}.jpg", title, caption=title)}<span class="view">View photo &#8599;</span></button>'
        f'<div class="comm-body"><small>{e(cat)}</small><h3>{e(title)}</h3><p>{e(text)}</p></div></article>'
        for i, (cat, title, text) in enumerate(COMMUNITY, 1))
    body = f"""<section class="section section-dark" style="padding:70px 0"><div class="wrap split">
  <div>
    <span class="eyebrow">Durban North &bull; Ward 36 &bull; Our community</span>
    <h1 style="font-size:clamp(38px,5vw,56px)">Community Work</h1>
    <h2 style="font-size:24px;text-transform:none">Proud of our community.<br>Hands-on in making it better.</h2>
    <p class="muted">Ellysa Entwistle and the SA Asphalt team giving time, practical skills and a helping hand to the places we call home.</p>
    <a class="btn btn-green" href="#community">Explore our work &darr;</a>
  </div>
  <div class="split-media">{img("community-hero.jpg", "SA Asphalt team planting trees at a public park", cls="zoomable", lazy=False)}</div>
</div></section>
<section class="section"><div class="wrap">
  <div class="section-head" style="margin-bottom:0"><span class="eyebrow red">Local people. Shared pride.</span><h2 style="text-transform:none">Giving back starts with showing up.</h2>
  <p>From cleaning up shared spaces and planting trees to improving parks and supporting neighbours, our community work brings Ellysa Entwistle and the SA Asphalt team together with residents, local groups and municipal teams.</p></div>
</div></section>
<section class="section section-light" id="community"><div class="wrap">
  <div class="section-head" style="margin-bottom:26px"><span class="eyebrow red">Our community in action</span><h2 style="text-transform:none">Small actions. Lasting pride.</h2><p>Browse the projects and moments below. Select any photograph to view it in full.</p><div class="title-rule"></div></div>
  <div class="filters" role="group" aria-label="Filter photographs">{filters}</div>
  <p class="filter-count" aria-live="polite">Showing all {len(COMMUNITY)} photographs</p>
  <div class="comm-grid" data-lightbox-group="community">{cards}</div>
</div></section>
{split(img("community-together.jpg", "Ellysa Entwistle with a community partner at a clean-up", cls="zoomable"),
       '''<span class="eyebrow red">Working together</span>
  <h2 style="text-transform:none">Our neighbourhood.<br>Our shared responsibility.</h2>
  <p class="muted">Thank you to the residents, volunteers, local organisations and municipal teams who have worked alongside us.</p>
  <p class="muted">Proud to play our part in Durban North and Ward 36.</p>''', light=False)}
{cta("Have a community project in mind?", "Get in touch with Ellysa and the SA Asphalt team to start a conversation.",
     f'<a class="btn btn-green" href="mailto:{C.EMAIL}?subject=Community%20project">Contact Ellysa</a>', "cta-plain")}"""
    return page("community.html", "Community Work | SA Asphalt",
                "Ellysa Entwistle and the SA Asphalt team giving time, practical skills and a helping hand in Durban North and Ward 36.",
                body)


PRIVACY = [
    (None, ["At SA Asphalt, accessible from www.saasphalt.co.za, one of our main priorities is the privacy of our visitors. This Privacy Policy document contains types of information that is collected and recorded by SA Asphalt and how we use it.",
            "If you have additional questions or require more information about our Privacy Policy, do not hesitate to contact us."]),
    ("Log Files", ["SA Asphalt follows a standard procedure of using log files. These files log visitors when they visit websites. All hosting companies do this and a part of hosting services' analytics. The information collected by log files include internet protocol (IP) addresses, browser type, Internet Service Provider (ISP), date and time stamp, referring/exit pages, and possibly the number of clicks. These are not linked to any information that is personally identifiable. The purpose of the information is for analyzing trends, administering the site, tracking users' movement on the website, and gathering demographic information."]),
    ("Privacy Policies", ["Third-party ad servers or ad networks uses technologies like cookies, JavaScript, or Web Beacons that are used in their respective advertisements and links that appear on SA Asphalt, which are sent directly to users' browser. They automatically receive your IP address when this occurs. These technologies are used to measure the effectiveness of their advertising campaigns and/or to personalize the advertising content that you see on websites that you visit.",
                          "Note that SA Asphalt has no access to or control over these cookies that are used by third-party advertisers."]),
    ("Third Party Privacy Policies", ["SA Asphalt's Privacy Policy does not apply to other advertisers or websites. Thus, we are advising you to consult the respective Privacy Policies of these third-party ad servers for more detailed information. It may include their practices and instructions about how to opt-out of certain options.",
                                      "You can choose to disable cookies through your individual browser options. To know more detailed information about cookie management with specific web browsers, it can be found at the browsers' respective websites."]),
    ("Children's Information", ["Another part of our priority is adding protection for children while using the internet. We encourage parents and guardians to observe, participate in, and/or monitor and guide their online activity.",
                                "SA Asphalt does not knowingly collect any Personal Identifiable Information from children under the age of 13. If you think that your child provided this kind of information on our website, we strongly encourage you to contact us immediately and we will do our best efforts to promptly remove such information from our records."]),
    ("Online Privacy Policy Only", ["This Privacy Policy applies only to our online activities and is valid for visitors to our website with regards to the information that they shared and/or collect in SA Asphalt. This policy is not applicable to any information collected offline or via channels other than this website."]),
    ("Consent", ["By using our website, you hereby consent to our Privacy Policy and agree to its Terms and Conditions."]),
]


def privacy():
    prose = "".join((f"<h2>{e(h)}</h2>" if h else "") + "".join(f"<p>{e(p)}</p>" for p in ps) for h, ps in PRIVACY)
    body = f"""<section class="section section-dark" style="padding:60px 0"><div class="wrap">
  <span class="eyebrow">SA Asphalt</span><h1 class="upper" style="font-size:clamp(34px,5vw,52px);margin:0">Privacy Policy</h1>
</div></section>
<section class="section"><div class="wrap prose">{prose}</div></section>"""
    return page("privacy.html", "Privacy Policy | SA Asphalt", "SA Asphalt website privacy policy.", body)


def not_found():
    body = f"""<section class="hero hero-404">
  <div class="hero-media">{img("about-quality.jpg", "", lazy=False)}</div>
  <div class="wrap"><div class="hero-copy" style="max-width:640px;margin:auto">
    <span class="eyebrow">404 &bull; Page not found</span>
    <h1>Wrong turn?</h1>
    <p>The page you requested is not available. Return to the SA Asphalt homepage, browse the full service range, or request a quotation.</p>
    <div class="btn-row"><a class="btn btn-red" href="index.html">Back to Home</a><a class="btn btn-green" href="services.html">View Services</a><a class="btn btn-outline" href="quote.html">Get a Quote</a></div>
  </div></div>
</section>"""
    return page("404.html", "Page Not Found | SA Asphalt", "The page you requested is not available.", body)


def gallery_redirect():
    (ROOT / "gallery.html").write_text("""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>Projects | SA Asphalt</title>
<meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url=projects.html">
<link rel="canonical" href="projects.html"></head>
<body><p>This page has moved to <a href="projects.html">Projects / Before &amp; After</a>.</p></body></html>
""", encoding="utf-8")
    return "gallery.html"


def build_all():
    return [home(), services(), about(), projects(), contact(), quote(), community(), privacy(), not_found(), gallery_redirect()]
