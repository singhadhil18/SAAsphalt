"""Generates the SA Asphalt static site.

Run from anywhere:  python build/build.py
Writes the HTML pages into the site root. Content lives in build/content.py;
this file holds the shared layout and section templates.
"""
from html import escape as e
from pathlib import Path

import content as C

ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------- icons
ICONS = {
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12h15M13 6l6 6-6 6"/></svg>',
    "chev": '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="M9 5l7 7-7 7"/></svg>',
    "wa": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 00-8.6 15.1L2 22l5-1.3A10 10 0 1012 2zm0 18.2a8.2 8.2 0 01-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1112 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 01-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 00-.7.3 3 3 0 00-.9 2.2 5.2 5.2 0 001.1 2.7 11.8 11.8 0 004.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 001.8-1.3 2.2 2.2 0 00.1-1.3c0-.1-.2-.2-.5-.3z"/></svg>',
    "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
    "flag": '<svg viewBox="0 0 20 26" aria-hidden="true"><path d="M3 2v22" stroke="#e31e24" stroke-width="3" stroke-linecap="round"/><path d="M4 3l13 3.5-9 3.5z" fill="#e31e24"/><path d="M8 11.5l9-3.4" stroke="#12a04b" stroke-width="2.6" stroke-linecap="round"/></svg>',
    "home": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 3l9 8h-3v9h-5v-6h-2v6H6v-9H3z"/></svg>',
    "building": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4 21V4h11v4h5v13h-6v-4h-4v4zm3-14v2h2V7zm4 0v2h2V7zm-4 4v2h2v-2zm4 0v2h2v-2zm5 2v2h2v-2z"/></svg>',
    "gear": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 8.5a3.5 3.5 0 100 7 3.5 3.5 0 000-7zm8.6 5l1.9 1.5-2 3.4-2.3-.9a7.6 7.6 0 01-2.2 1.3l-.4 2.4h-4l-.4-2.4a7.6 7.6 0 01-2.2-1.3l-2.3.9-2-3.4 1.9-1.5a7.7 7.7 0 010-2.6L1.5 9.5l2-3.4 2.3.9A7.6 7.6 0 018 5.7l.4-2.4h4l.4 2.4a7.6 7.6 0 012.2 1.3l2.3-.9 2 3.4-1.9 1.5a7.7 7.7 0 010 2.6z"/></svg>',
    "school": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 3L1 9l11 6 9-4.9V17h2V9zM5 13.2v4L12 21l7-3.8v-4L12 17z"/></svg>',
    "cross": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M9 3h6v6h6v6h-6v6H9v-6H3V9h6z"/></svg>',
    "star": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3 7 7 .6-5.3 4.7 1.6 7.2L12 17.8 5.7 21.5l1.6-7.2L2 9.6 9 9z"/></svg>',
    "swap": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M7 7h13l-4-4M17 17H4l4 4"/></svg>',
}


def icon(name):
    return ICONS[name]


def tick():
    return f'<span class="tick">{icon("check")}</span>'


def img(src, alt, cls="", lazy=True, style="", caption=None):
    attrs = [f'src="assets/img/{src}"', f'alt="{e(alt)}"']
    if cls:
        attrs.append(f'class="{cls}"')
    if lazy:
        attrs.append('loading="lazy"')
    if style:
        attrs.append(f'style="{style}"')
    if caption:
        attrs.append(f'data-caption="{e(caption)}"')
    return f"<img {' '.join(attrs)}>"


def wa_link(text=None):
    url = f"https://wa.me/{C.WHATSAPP_INTL}"
    if text:
        from urllib.parse import quote
        url += "?text=" + quote(text)
    return url


# ---------------------------------------------------------------- layout
NAV = [("index.html", "Home"), ("services.html", "Services"), ("projects.html", "Projects"), ("about.html", "About"), ("contact.html", "Contact")]


def logo():
    return (f'<a class="logo" href="index.html" aria-label="SA Asphalt home">{icon("flag")}'
            '<span class="logo-text"><span class="logo-sa">S.A.</span><span class="logo-asphalt">ASPHALT</span></span></a>')


def header(active):
    items = "".join(
        f'<li><a href="{href}"{" aria-current=\"page\"" if href == active else ""}>{label}</a></li>' for href, label in NAV)
    return f"""<div class="topbar"><div class="wrap">
  <div class="topbar-tag"><strong>SA ASPHALT</strong> &bull; {e(C.AREA_SHORT)} &bull; Local experts, quality work, built to last</div>
  <div class="topbar-links"><a href="tel:{C.MOBILE_TEL}">{C.MOBILE}</a><a href="tel:{C.OFFICE_TEL}">{C.OFFICE}</a><a href="mailto:{C.EMAIL}">{C.EMAIL}</a></div>
</div></div>
<header class="header"><div class="wrap">
  {logo()}
  <button class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="site-nav">{icon("menu")}</button>
  <nav class="nav" id="site-nav" aria-label="Main">
    <ul>{items}</ul>
    <a class="btn btn-green" href="quote.html">Get a Quote</a>
  </nav>
</div></header>"""


def crumbs(trail):
    parts = []
    for href, label in trail[:-1]:
        parts.append(f'<a href="{href}">{e(label)}</a> / ')
    parts.append(f"<strong>{e(trail[-1][1])}</strong>")
    return f'<div class="crumbs"><div class="wrap">{"".join(parts)}</div></div>'


def footer():
    return f"""<footer class="footer">
  <div class="wrap">
    <div>
      {logo()}
      <p>Professional asphalt, paving and exterior works across the {e(C.AREA)}.</p>
      <p class="est">Established 2003 &bull; {e(C.AREA_SHORT)}</p>
    </div>
    <div>
      <h4>Quick Links</h4>
      <ul>
        <li><a href="services.html">Services</a></li>
        <li><a href="projects.html">Projects / Before &amp; After</a></li>
        <li><a href="about.html">About SA Asphalt</a></li>
        <li><a href="community.html">Community Work</a></li>
        <li><a href="quote.html">Get a Quote</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </div>
    <div>
      <h4>Get in Touch</h4>
      <ul>
        <li><a href="tel:{C.MOBILE_TEL}">{C.MOBILE}</a></li>
        <li><a href="tel:{C.OFFICE_TEL}">{C.OFFICE}</a></li>
        <li><a href="mailto:{C.EMAIL}">{C.EMAIL}</a></li>
        <li><a href="https://www.saasphalt.co.za">www.saasphalt.co.za</a></li>
      </ul>
    </div>
    <div>
      <h4>Service Area</h4>
      <ul>
        <li>{e(C.AREA_SHORT)}</li>
        <li>Residential, commercial &amp; industrial</li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom"><div class="wrap">
    <span>&copy; <span data-year>2026</span> Steve Services t/a SA Asphalt. All rights reserved. <a href="privacy.html">Privacy Policy</a></span>
    <span>Durban &bull; KwaZulu-Natal &bull; South Africa</span>
  </div></div>
</footer>
<a class="float-wa" href="{wa_link()}" target="_blank" rel="noopener">{icon("wa")}<span>WhatsApp Quote</span></a>"""


ANALYTICS = """<script async src="https://www.googletagmanager.com/gtag/js?id=UA-181267603-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-181267603-1');
</script>"""


def page(filename, title, description, body, active=None, trail=None):
    crumb_html = crumbs(trail) if trail else ""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<link rel="icon" href="images/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;700;800&family=Lato:wght@400;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/site.css">
</head>
<body>
{header(active)}
{crumb_html}
<main>
{body}
</main>
{footer()}
<script src="assets/js/site.js"></script>
{ANALYTICS}
</body>
</html>
"""
    (ROOT / filename).write_text(html, encoding="utf-8")
    return filename


# ---------------------------------------------------------------- sections
def bars():
    return '<div class="bars"><span></span><span></span></div>'


def strip(items):
    lis = "".join(f'<li><span class="ring">{icon("check")}</span>{e(t)}</li>' for t in items)
    return f'<section class="strip" aria-label="Highlights"><ul class="wrap">{lis}</ul></section>'


def ticks(items, cls="ticks"):
    return f'<ul class="{cls}">' + "".join(f"<li>{tick()}{e(t)}</li>" for t in items) + "</ul>"


def two_line(h):
    """Heading given as (white, red) or a plain string."""
    if isinstance(h, (tuple, list)):
        return f'{e(h[0])} <span class="red">{e(h[1])}</span>'
    return e(h)


def hero_core(s):
    return f"""<section class="hero">
  <div class="hero-media">{img(s["hero"], s["hero_alt"], lazy=False, style=s.get("hero_pos", ""))}</div>
  <div class="wrap"><div class="hero-copy">
    <span class="eyebrow">{e(s["eyebrow"])}</span>
    <h1>{two_line(s["h1"])}</h1>
    {bars()}
    <p>{e(s["lead"])}</p>
    <div class="btn-row">
      <a class="btn btn-green" href="{wa_link("Hi SA Asphalt, I'd like a quote for " + s["name"].lower() + ".")}" target="_blank" rel="noopener">WhatsApp for a Quote</a>
      <a class="btn btn-outline" href="projects.html">View Projects</a>
    </div>
  </div></div>
</section>"""


def hero_full(s):
    return f"""<section class="hero hero-full">
  <div class="hero-media">{img(s["hero"], s["hero_alt"], lazy=False, style=s.get("hero_pos", ""))}</div>
  <div class="wrap"><div class="hero-copy">
    <div class="crumb-inline"><a href="index.html">Home</a> / <a href="services.html">Services</a> / {e(s["name"])}</div>
    <span class="eyebrow">{e(s["tier"])} service &bull; {e(C.AREA_SHORT)}</span>
    <h1 class="upper">{e(s["name"])}</h1>
    <p>{e(s["tagline"])}</p>
    <div class="btn-row">
      <a class="btn btn-green" href="quote.html?service={e(s["name"])}">Get a Free Quote</a>
      <a class="btn btn-outline" href="{wa_link()}" target="_blank" rel="noopener">WhatsApp {C.MOBILE}</a>
    </div>
  </div></div>
</section>"""


def split(media_html, copy_html, light=True, flip=False):
    return f"""<section class="section{' section-light' if light else ''}"><div class="wrap split{' split-flip' if flip else ''}">
  <div class="split-media">{media_html}</div>
  <div>{copy_html}</div>
</div></section>"""


def media(src, alt, tag=None):
    """Feature photo with an optional name-drop label."""
    label = f'<span class="media-tag">{e(tag)}</span>' if tag else ""
    return img(src, alt, cls="zoomable", caption=tag or alt) + label


def gallery(items, group):
    """items: list of (image, caption). First item is the large tile."""
    figs = "".join(
        f"<figure>{img(src, cap)}{f'<figcaption>{e(cap)}</figcaption>' if cap else ''}</figure>" for src, cap in items)
    return f'<div class="gallery" data-lightbox-group="{group}">{figs}</div>'


def gallery3(items, group):
    figs = "".join(f"<figure>{img(src, alt)}</figure>" for src, alt in items)
    return f'<div class="gallery-3" data-lightbox-group="{group}">{figs}</div>'


def link_buttons(links):
    return '<div class="links-3">' + "".join(
        f'<a class="link-btn" href="{href}">{e(label)}{icon("arrow")}</a>' for href, label in links) + "</div>"


def cta(title, text, buttons, cls=""):
    return f"""<section class="cta {cls}"><div class="wrap">
  <div><h2>{e(title)}</h2><p>{e(text)}</p></div>
  <div class="btn-row">{buttons}</div>
</div></section>"""


def wa_button(label=f"WhatsApp {C.MOBILE}", cls="btn-green"):
    return f'<a class="btn {cls}" href="{wa_link()}" target="_blank" rel="noopener">{e(label)}</a>'


def service_card(svc, show_desc=False, home=False):
    desc = f"<p>{e(svc['desc'])}</p>" if show_desc else ""
    pos = f' style="object-position:{svc["card_pos"]}"' if svc.get("card_pos") else ""
    title = svc["home_title"] if home else svc["title"]
    return (f'<a class="svc-card" href="{svc["slug"]}.html">'
            f'<img src="assets/img/{svc["card"]}" alt="{e(svc["card_alt"])}" loading="lazy"{pos}>'
            f'<div class="svc-body"><small>{e(svc["kicker"])}</small><h3>{e(title)}</h3>{desc}'
            f'<span class="go">{icon("chev")}</span></div></a>')


def clients_chips():
    return '<ul class="clients">' + "".join(f"<li>{e(c)}</li>" for c in C.CLIENTS) + "</ul>"


# ---------------------------------------------------------------- service pages
def core_service(s):
    intro_copy = (f'<h2>{two_line(s["intro_h"])}</h2>'
                  + "".join(f'<p class="muted">{e(p)}</p>' for p in s["intro_p"])
                  + ticks(s["intro_ticks"])
                  + f'<div class="callout">{e(s["callout"])}</div>')
    process = "".join(
        f'<div class="card"><span class="num">0{i}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(s["process"], 1))
    approach = "".join(
        f'<div class="card card-top"><span class="num">0{i}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(s["approach"], 1))
    related = [(f"{slug}.html", C.SERVICE_BY_SLUG[slug]["short"]) for slug in s["related"]] + [("services.html", "All Services")]
    body = f"""{hero_core(s)}
{strip(["Quality workmanship", "SABS-approved materials", "Experienced team", C.AREA_SHORT])}
{split(media(s["intro_img"], s["intro_alt"], s.get("intro_tag")), intro_copy)}
<section class="section"><div class="wrap">
  <div class="section-head"><h2>Built around <span class="red">the right process</span></h2><p>Good surfacing starts with preparation, the correct materials and disciplined workmanship.</p></div>
  <div class="cards-3">{process}</div>
</div></section>
<section class="section section-light"><div class="wrap">
  <div class="section-head"><h2>How we <span class="green">approach the job</span></h2></div>
  <div class="cards-4">{approach}</div>
</div></section>
<section class="section section-dark"><div class="wrap">
  <div class="section-head"><h2>SA Asphalt <span class="red">projects</span></h2>{f'<p>{e(s["gallery_note"])}</p>' if s.get("gallery_note") else ''}</div>
  {gallery(s["gallery"], s["slug"])}
</div></section>
<section class="section"><div class="wrap">
  <div class="section-head" style="margin-bottom:28px"><h2>Related <span class="red">services</span></h2></div>
  {link_buttons(related)}
</div></section>
{cta("Ready to discuss your project?", "Send us photos, your location and an approximate size. We can review the requirement and arrange the next step.", wa_button())}"""
    return page(f'{s["slug"]}.html', f'{s["name"]} | SA Asphalt', s["lead"], body, active="services.html",
                trail=[("index.html", "Home"), ("services.html", "Services"), (None, s["name"])])


def supporting_service(s):
    intro_copy = (f'<span class="eyebrow">Professional exterior works</span><h2>{e(s["intro_h"])}</h2>'
                  f'<p class="muted">{e(s["intro_p"])}</p>' + ticks(s["intro_ticks"])
                  + '<div class="callout">Proper preparation, practical site solutions and a professional finish.</div>')
    cards = "".join(f'<div class="card"><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d in s["cards"])
    steps = "".join(
        f'<div class="card card-top"><h3>{i}. {e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(s["steps"], 1))
    related = [(f"{slug}.html", C.SERVICE_BY_SLUG[slug]["short"]) for slug in s["related"]]
    body = f"""{hero_full(s)}
{strip([C.AREA_SHORT, "Residential", "Commercial", "Project work"])}
{split(media(s["intro_img"], s["intro_alt"], s.get("intro_tag")), intro_copy)}
<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">What we do</span><h2>Built around the site</h2><p>Every property is different. The right solution depends on levels, access, drainage, usage and how the new work connects with the surrounding area.</p></div>
  <div class="cards-3">{cards}</div>
</div></section>
<section class="section section-light"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Our process</span><h2>How we approach the job</h2></div>
  <div class="cards-4">{steps}</div>
</div></section>
<section class="section section-dark"><div class="wrap">
  <div class="section-head"><span class="eyebrow">SA Asphalt work</span><h2>SA Asphalt project photographs</h2>{f'<p>{e(s["gallery_note"])}</p>' if s.get("gallery_note") else ''}</div>
  {gallery3(s["gallery"], s["slug"])}
</div></section>
<section class="section section-light"><div class="wrap">
  <div class="section-head" style="margin-bottom:28px"><span class="eyebrow">Related services</span><h2>Complete the project</h2></div>
  {link_buttons(related)}
</div></section>
{cta("Ready to discuss your project?", "Send us the details and photographs, or request a site visit and quotation.", '<a class="btn btn-red" href="quote.html">Request a Quote</a>' + wa_button("WhatsApp Us"))}"""
    return page(f'{s["slug"]}.html', f'{s["name"]} | SA Asphalt', s["tagline"] + " " + s["intro_p"], body, active="services.html")


# ---------------------------------------------------------------- build
def main():
    import pages
    written = []
    for s in C.CORE_SERVICES:
        written.append(core_service(s))
    for s in C.SUPPORTING_SERVICES:
        written.append(supporting_service(s))
    written += pages.build_all()
    print(f"Wrote {len(written)} pages:", ", ".join(written))


if __name__ == "__main__":
    main()
