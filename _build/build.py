#!/usr/bin/env python3
"""Which Senior Plan static site.
  python3 _build/build.py            # noindex on every page, root paths, CNAME, no beacon
  python3 _build/build.py --launch   # indexable, Cloudflare beacon, GA4 after consent, same paths and CNAME
Dates are editorial constants. Do not replace them with the build clock.
GA4_ID is empty until the owner pastes a G- measurement id. check.py --launch fails while it is empty.
"""
import html, json, os, re, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from guides import GUIDES
from state_extras import EXTRAS
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAUNCH = "--launch" in sys.argv  # single flag: False until whichseniorplan.com is live
BASE = "https://whichseniorplan.com/"
BRAND = "Which Senior Plan"
PUBLISHED = "2026-11-16"
CHECKED = "16 Nov 2026"
INDEXNOW_KEY = "c641d3cb68a0047708c9064020aa6977"
CF_BEACON_TOKEN = "eac63f2b5dbc4539a2d95249baab6472"
GA4_ID = "G-F440SDE14K"  # Owner pastes a G-XXXXXXXXXX measurement id. Empty fails the launch check.
ADSENSE_PUB = "ca-pub-5681559774142917"
LEGAL_LINE = "© 2026 Joshua Israel Ventures LLC. All rights reserved. Which Senior Plan is a trade name of Joshua Israel Ventures LLC, a Florida limited liability company."
E = html.escape
STATES = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "states.json"), encoding="utf-8"))
PAGES = []
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONTB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def u(path):
    return path

def url(path):
    return BASE + path.lstrip("/")

def write(path, content):
    fp = os.path.join(ROOT, path.lstrip("/"))
    if path.endswith("/"):
        fp = os.path.join(fp, "index.html")
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w", encoding="utf-8").write(content)

LOGO = '<svg width="34" height="34" viewBox="0 0 64 64" aria-hidden="true" focusable="false"><rect width="64" height="64" rx="14" fill="#12324a"/><circle cx="32" cy="30" r="16" fill="#f6f3ec"/><path d="M32 34 L18 18 h8 l6 10 6-10 h8 z" fill="#0f5c63"/><rect x="18" y="40" width="28" height="6" rx="3" fill="#c4892a"/></svg>'
NAV = [("/", "Home"), ("/guides/", "Guides"), ("/states/", "States"), ("/guides/enrollment-periods/", "Deadlines"), ("/guides/ship-counseling/", "Free help")]

def expand(body):
    def repl(m):
        return f'<a href="{u(m.group(1))}">{E(m.group(2))}</a>'
    return re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", repl, body)

def crumbs_html(crumbs):
    if not crumbs:
        return ""
    items = []
    for i, (p, n) in enumerate(crumbs):
        if i < len(crumbs) - 1:
            items.append(f'<li><a href="{u(p)}">{E(n)}</a></li>')
        else:
            items.append(f'<li aria-current="page">{E(n)}</li>')
    return '<nav class="crumbs" aria-label="Breadcrumb"><ol>' + "".join(items) + "</ol></nav>"

# AdSense low-value-content fix (20 Nov 2026): paths listed in _build/thin-noindex.txt
# get noindex,follow and stay out of the sitemap until they have real unique substance.
_THIN_NOINDEX = set()
try:
    import os as _os
    with open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "thin-noindex.txt"), encoding="utf-8") as _fh:
        _THIN_NOINDEX = {l.strip().strip("/") for l in _fh if l.strip() and not l.startswith("#")}
except FileNotFoundError:
    pass


def _is_thin(path):
    return str(path).strip("/") in _THIN_NOINDEX


def page(path, title, desc, body, jsonld=None, crumbs=None, noindex=False, legal=False, kind="website", lastmod=None, og_image=None):
    if _is_thin(path):
        noindex = True
    if len(title) >= 60:
        raise SystemExit(f"title {len(title)} {title}")
    if len(desc) > 155 or len(desc) < 40:
        raise SystemExit(f"desc {len(desc)} {path} {desc}")
    canon = url(path if path != "/404.html" else "/")
    if path == "/404.html":
        canon = url("/404.html")
    if not noindex:
        PAGES.append((path if path != "/404.html" else "/404.html", lastmod or PUBLISHED))
    og_img = url(og_image) if og_image else url("/og.png")
    ld = []
    if path == "/":
        ld.append({"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": BASE,
                   "description": "Plain English guides to senior health plan choices by state.",
                   "publisher": {"@type": "Organization", "name": BRAND, "url": BASE, "logo": url("/logo.png")}})
        ld.append({"@context": "https://schema.org", "@type": "Organization", "name": BRAND, "url": BASE,
                   "logo": url("/logo.png")})
    if crumbs:
        ld.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": url(p)} for i, (p, n) in enumerate(crumbs)]})
    if jsonld:
        ld += jsonld if isinstance(jsonld, list) else [jsonld]
    ldh = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    nav = "".join(f'<a href="{u(p)}"' + (' aria-current="page"' if p == path else "") + f">{n}</a>" for p, n in NAV)
    robots = "noindex, follow" if (noindex or not LAUNCH) else "index, follow, max-image-preview:large"
    beacon = (f"<!-- Cloudflare Web Analytics --><script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{\"token\": \"{CF_BEACON_TOKEN}\"}}'></script><!-- End Cloudflare Web Analytics -->") if LAUNCH else "<!-- cf-beacon: added by the launch flag -->"
    legal_html = f'<p class="legal-line">{LEGAL_LINE}</p>' if legal else ""
    cookie = f'<a href="{u("/privacy/#analytics")}" id="cookie-settings">Cookie settings</a>'
    if LAUNCH:
        ga_head = (
            f'<script id="ga4-loader" data-ga4-id="{E(GA4_ID)}" data-gtag-src="https://www.googletagmanager.com/gtag/js">'
            "window.dataLayer=window.dataLayer||[];"
            "function gtag(){dataLayer.push(arguments);}"
            "gtag('consent','default',{'ad_storage':'denied','ad_user_data':'denied','ad_personalization':'denied','analytics_storage':'denied','wait_for_update':500});"
            "gtag('set','ads_data_redaction',true);"
            "</script>"
        )
        consent = f'<script src="{u("/assets/consent.js")}" defer></script>'
    else:
        ga_head = ""
        consent = ""
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{canon}">
<meta name="robots" content="{robots}">
<meta property="og:type" content="{kind}"><meta property="og:site_name" content="{BRAND}"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{og_img}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{E(title)}"><meta name="twitter:description" content="{E(desc)}">
<link rel="icon" href="{u("/favicon.svg")}" type="image/svg+xml"><link rel="stylesheet" href="{u("/assets/style.css")}?v=4">{ldh}{ga_head}
</head><body><a class="skip" href="#main">Skip to content</a>
<div class="banner"><div class="wrap"><p>Independent guide. Not a government site. Not insurance advice. No plan sales and no quote forms.</p></div></div>
<header class="site"><div class="wrap"><a class="brand" href="{u("/")}"><span class="mark">{LOGO}</span><span>{BRAND}</span></a><nav class="main" aria-label="Main">{nav}</nav></div></header>
<main id="main" class="wrap">{crumbs_html(crumbs)}{body}</main>
<footer class="site"><div class="wrap"><p><strong>{BRAND}</strong> explains senior health plan choices in plain English, using public federal and state pages. We are not affiliated with or endorsed by the U.S. government or the federal Medicare program. We do not sell plans.</p>
<p class="flinks"><a href="{u("/about/")}">About</a> | <a href="{u("/editorial-policy/")}">Editorial and sources</a> | <a href="{u("/image-policy/")}">Image policy</a> | <a href="{u("/terms/")}">Terms of use</a> | <a href="{u("/privacy/")}">Privacy</a> | <a href="{u("/disclaimer/")}">Disclaimer</a> | <a href="{u("/ad-disclosure/")}">Advertising disclosure</a> | <a href="{u("/copyright/")}">Copyright and DMCA</a> | <a href="{u("/contact/")}">Contact</a> | {cookie}</p>
{legal_html}</div></footer>
<script src="{u("/assets/site.js")}?v=1" defer></script>{consent}{beacon}
</body></html>'''

def picker(selected=""):
    opts = ['<option value="">Choose a state</option>']
    for s in STATES:
        label = s["name"][4:].title() if s["name"].startswith("the ") else s["name"]
        if s["slug"] == "district-of-columbia":
            label = "District of Columbia"
        sel = " selected" if s["slug"] == selected else ""
        opts.append(f'<option value="{u("/states/" + s["slug"] + "/")}"{sel}>{E(label)}</option>')
    return f'''<form class="picker" action="{u("/states/")}" method="get">
<label for="state-picker">Plans and contacts by state</label>
<select id="state-picker" name="state">{"".join(opts)}</select>
<button class="btn" id="state-go" type="button">Show this state</button>
</form><p class="note">Or open the <a href="{u("/states/")}">full state list</a>.</p>'''

def src_list(sources):
    return "<ul>" + "".join(f'<li><a href="{E(h)}" rel="noopener" target="_blank">{E(n)}</a></li>' for n, h in sources) + "</ul>"

def faq_block(faqs):
    return '<section class="faq" aria-labelledby="faq-h"><h2 id="faq-h">Questions people ask</h2>' + "".join(
        f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in faqs) + "</section>"

def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def article_ld(h1, path, published=None, modified=None, image=None):
    pub = published or PUBLISHED
    mod = modified or pub
    return {"@context": "https://schema.org", "@type": "Article", "headline": h1,
            "datePublished": pub, "dateModified": mod,
            "image": url(image) if image else url("/og.png"), "mainEntityOfPage": url(path),
            "author": {"@type": "Organization", "name": BRAND, "url": BASE},
            "publisher": {"@type": "Organization", "name": BRAND, "url": BASE, "logo": {"@type": "ImageObject", "url": url("/logo.png")}}}

def byline(checked=None):
    return f'<p class="byline">By {BRAND}. Last checked {checked or CHECKED}.</p>'

def notice():
    return '<p class="notice">General information from public pages. This is not insurance advice, not a recommendation, and not a government site.</p>'

def hero_thumb(image, alt, caption=None):
    cap = caption or "Photo used as the article thumbnail."
    # The whole caption points at the image policy, not only the label.
    return (
        f'<figure class="hero-thumb">'
        f'<a href="{u("/image-policy/")}"><img src="{u(image)}" width="1280" height="720" alt="{E(alt)}"></a>'
        f'<figcaption><a href="{u("/image-policy/")}">AI generated image. {E(cap)}</a></figcaption>'
        f'</figure>'
    )

def next_reads_html(items, heading="Keep reading"):
    if not items:
        return ""
    # Every <img> must sit inside an open <a href="/image-policy/"> (check.py).
    cards = []
    for it in items:
        path, label, image, alt = it[0], it[1], it[2], it[3]
        cards.append(
            f'<li>'
            f'<a href="{u("/image-policy/")}" class="nr-img"><img src="{u(image)}" width="480" height="270" alt="{E(alt)}" loading="lazy"></a>'
            f'<a class="nr-cap" href="{u("/image-policy/")}">AI generated image</a>'
            f'<a class="nr-title" href="{u(path)}">{E(label)}</a>'
            f'</li>'
        )
    hid = "next-reads-h" if heading == "Keep reading" else "related-reads-h"
    return (
        f'<section class="next-reads" aria-labelledby="{hid}">'
        f'<h2 id="{hid}">{E(heading)}</h2>'
        f'<ul>{"".join(cards)}</ul>'
        f'</section>'
    )

def compare_box(html_inner):
    return f'<aside class="compare" aria-label="Check another year">{html_inner}</aside>'

def guide_pages():
    for g in GUIDES:
        related = list(g["related"])
        if not any(p == "/guides/" for p, _n in related):
            related.append(("/guides/", "All guides"))
        gchecked = g.get("checked", CHECKED)
        gpub = g.get("published", PUBLISHED)
        gmod = g.get("modified", gpub)
        gimg = g.get("image")
        thumb = hero_thumb(gimg, g.get("image_alt", g["h1"]), g.get("image_caption")) if gimg else ""
        mid = next_reads_html(g.get("next_reads_mid") or g.get("next_reads") or [], "Related guides") if (g.get("next_reads_mid") or g.get("next_reads")) else ""
        end = next_reads_html(g.get("next_reads_end") or g.get("next_reads") or [], "Keep reading") if (g.get("next_reads_end") or g.get("next_reads")) else ""
        # If only one next_reads list is provided, show it mid-article (after body insert point) and at end.
        body_html = expand(g["body"])
        if mid and "<!--NEXT_READS-->" in body_html:
            body_html = body_html.replace("<!--NEXT_READS-->", mid, 1)
            mid_placed = True
        else:
            mid_placed = False
        mid_block = "" if mid_placed else mid
        compare = expand(g.get("compare_html", ""))
        body = f'''<article class="prose"><h1>{E(g["h1"])}</h1>{byline(gchecked)}{notice()}
{thumb}{compare}
{body_html}
{mid_block}
{faq_block(g["faqs"])}
<section class="sources"><h2>Sources</h2>{src_list(g["sources"])}
<p class="note">Last checked {gchecked}. We cite the page we read. Dollar amounts appear only for the year the official page labels.</p></section>
{end}
<p class="related">''' + " · ".join(f'<a href="{u(p)}">{E(n)}</a>' for p, n in related) + "</p></article>"
        write(g["path"], page(g["path"], g["title"], g["desc"], body,
                              [article_ld(g["h1"], g["path"], gpub, gmod, gimg), faq_ld(g["faqs"])],
                              [("/", "Home"), ("/guides/", "Guides"), (g["path"], g["h1"])],
                              kind="article", lastmod=gmod, og_image=gimg))

def guides_index():
    groups = [
        ("The two paths", [0, 1, 2]),
        ("Medigap letters", [3, 19, 24]),
        ("Drugs", [4, 15]),
        ("Deadlines", [5, 6, 7, 8, 9, 10]),
        ("Costs and help", [11, 22, 23, 12, 13, 14, 16, 17]),
        ("Comparing", [18]),
        ("Programs and benefits", [20, 21]),
    ]
    # indexes into GUIDES must match add() order
    blocks = []
    for name, idxs in groups:
        items = "".join(f'<li><a href="{u(GUIDES[i]["path"])}">{E(GUIDES[i]["h1"])}</a></li>' for i in idxs)
        blocks.append(f"<h2>{E(name)}</h2><ul>{items}</ul>")
    faqs = [
        ("Which guide should I read first?", "Start with Original Medicare or Medicare Advantage, then open the deadline or the cost that applies to you."),
        ("How many national guides are here?", f"{len(GUIDES)} explainers on the federal rules, plus a page for each state and the District of Columbia."),
    ]
    GUIDES_INDEX_UPDATED = "2026-11-21"
    body = f'<article class="prose"><h1>Guides</h1>{byline(GUIDES_INDEX_UPDATED)}{notice()}<p>{len(GUIDES)} explainers on the federal rules, plus a page for each state and the District of Columbia. Start with the choice between Original Medicare and Medicare Advantage, then open the deadline or the cost that applies to you. The <a href="{u("/guides/medicare-costs-2027/")}">2027 Medicare costs</a> page has the new Part A and Part B amounts from CMS. Income brackets that raise those premiums are on the <a href="{u("/guides/irmaa-brackets-2027/")}">2027 IRMAA</a> page. The <a href="{u("/guides/medigap-guaranteed-issue-rights/")}">guaranteed issue</a> page lists when a company must sell a Medigap policy, and the <a href="{u("/guides/medicare-savings-programs/")}">savings program</a> page has the 2026 income limits Medicare.gov still prints.</p>{"".join(blocks)}<p><a href="{u("/states/")}">State contacts</a> · <a href="{u("/guides/how-to-compare-plans/")}">How to compare plans</a></p>{faq_block(faqs)}</article>'
    desc = "Plain English guides to Medicare plan choices, deadlines, Medigap letters, Part D, PACE, and state help lines."
    write("/guides/", page("/guides/", "Which Medicare Guide Should I Read?", desc, body,
                           [article_ld("Guides", "/guides/", modified=GUIDES_INDEX_UPDATED), faq_ld(faqs)],
                           [("/", "Home"), ("/guides/", "Guides")], kind="article", lastmod=GUIDES_INDEX_UPDATED))

def medigap_note(s):
    name = s["name"]
    if s["medigap"] == "massachusetts":
        return f"""<p>Massachusetts does not use the usual letter chart. Medicare.gov lists a Core Plan, a Supplement 1 Plan, and a Supplement 1A Plan. Core does not cover the Part A deductible, skilled nursing coinsurance, the Part B deductible, or foreign travel. Supplement 1 covers those, including the Part B deductible. Supplement 1A covers the Part A deductible, skilled nursing coinsurance, and foreign travel, and it does not cover the Part B deductible. Supplement 1 is closed to people who became eligible on or after January 1, 2020. Mental health inpatient days are 60 per calendar year on Core and 120 per benefit year on the other two.</p>"""
    if s["medigap"] == "minnesota":
        return f"""<p>Minnesota uses its own Medigap design. Medicare.gov lists a Basic Plan and an Extended Basic Plan. Extended Basic covers the Part A inpatient deductible. Basic does not, unless you add it. Foreign travel emergency is 80 percent on both. Outpatient mental health is 50 percent on both. Usual and customary fees are 80 percent on Extended Basic and are not covered on Basic unless you add them. Minnesota also has its own versions of some lettered plans, including a high deductible Plan F only for people who were eligible before January 1, 2020.</p>"""
    if s["medigap"] == "wisconsin":
        return f"""<p>Wisconsin does not sell the usual 10 letters as the base policy. Medicare.gov says there is one Medigap plan, and companies may add riders such as the Part A deductible, extra home health visits, the Part B deductible, Part B excess charges, and foreign travel. Cost sharing plans similar to Plan K and Plan L are available, and so is a high deductible option. The state insurance department is the place to ask which riders a company sells.</p>"""
    return f"""<p>In {E(name)}, Medigap policies use the standardized letters Medicare.gov publishes for most states: A, B, C, D, F, G, K, L, M, and N. The same letter has the same basic benefits at every company. The premium is not standardized, and this page does not list premiums or company names.</p>"""

def state_pages():
    for s in STATES:
        place = s["name"]
        label = "District of Columbia" if s["slug"] == "district-of-columbia" else s["name"]
        path = f'/states/{s["slug"]}/'
        ship_rows = "".join(f'<tr><th scope="row">{E(c["label"])}</th><td>{E(c["value"])}</td></tr>' for c in s["ship_contacts"])
        med_rows = "".join(f'<tr><th scope="row">Phone</th><td>{E(p)}</td></tr>' for p in s["medicaid"]["phones"])
        doi = f'<p>State insurance department: <a href="{E(s["doi"])}" rel="noopener" target="_blank">homepage we confirmed</a>. Medigap companies are regulated there. We did not copy a rate sheet.</p>' if s["doi"] else "<p>We did not confirm a state insurance department homepage on this pass, so we are not guessing a web address. A SHIP counselor can point you to the office that regulates Medigap.</p>"
        higher = "<p>Medicare.gov says 2026 Medicare Savings Program income limits are slightly higher in this state than the federal table on our savings program page. We are not printing a higher dollar amount we did not read. Ask the Medicaid agency.</p>" if s["msp_higher"] else ""
        faqs = [
            (f"Who offers free Medicare counseling in {place}?", f'{s["ship_name"]} is the program listed on shiphelp.org. The number on that page is {s["ship_contacts"][0]["value"]}.'),
            (f"Where do I apply for a Medicare Savings Program in {place}?", f'Medicaid.gov lists {s["medicaid"]["agency"]}. Applications go to the state, not to this website.'),
            (f"Does {place} use the standard Medigap letters?", "No. See the Medigap note on this page and the federal chart." if s["medigap"] != "standard" else "Yes. Medicare.gov standardizes letters A, B, C, D, F, G, K, L, M, and N in this state. Prices still differ by company."),
        ]
        sources = [
            (f'{label} SHIP listing', s["shiphelp"]),
            (s["ship_name"], s["ship_url"]),
            (f'{s["medicaid"]["agency"]} on Medicaid.gov', s["medicaid"]["directory"]),
            (s["medicaid"]["agency"], s["medicaid"]["url"]),
            ("Medicare Savings Programs", "https://www.medicare.gov/basics/costs/help/medicare-savings-programs"),
        ]
        if s["medigap"] == "massachusetts":
            sources.append(("Medigap in Massachusetts", "https://www.medicare.gov/health-drug-plans/medigap/basics/compare-plan-benefits/massachusetts"))
        elif s["medigap"] == "minnesota":
            sources.append(("Medigap in Minnesota", "https://www.medicare.gov/health-drug-plans/medigap/basics/compare-plan-benefits/minnesota"))
        elif s["medigap"] == "wisconsin":
            sources.append(("Medigap in Wisconsin", "https://www.medicare.gov/health-drug-plans/medigap/basics/compare-plan-benefits/wisconsin"))
        else:
            sources.append(("Compare Medigap plan benefits", "https://www.medicare.gov/health-drug-plans/medigap/basics/compare-plan-benefits"))
        if s["doi"]:
            sources.append(("State insurance department", s["doi"]))
        extra = EXTRAS.get(s["slug"])
        if extra:
            faqs = faqs + list(extra["faqs"])
            sources = sources + list(extra["sources"])
        checked = extra["checked"] if extra else CHECKED
        h1 = extra["h1"] if extra else f"Medicare plan choices in {place}"
        extra_html = expand(extra["html"]) if extra else ""
        compare = expand(extra["compare_html"]) if extra else ""
        reads = extra["next_reads"] if extra else None
        mid = next_reads_html(reads, "Related guides") if reads else ""
        end = next_reads_html(reads, "Keep reading") if reads else ""
        body = f'''<article class="prose"><h1>{E(h1)}</h1>{byline(checked)}{notice()}
<div class="answer"><p><strong>Who to call in {E(place)}:</strong> {E(s["ship_name"])}, {E(s["ship_contacts"][0]["value"])}. For help paying premiums, {E(s["medicaid"]["agency"])} runs the state Medicaid and Medicare Savings Programs. We do not list private plan names or premiums.</p></div>
<h2>Free counseling</h2>
<div class="tablewrap"><table class="stats"><tbody>
<tr><th scope="row">Program</th><td>{E(s["ship_name"])}</td></tr>
{ship_rows}
<tr><th scope="row">Program website</th><td><a href="{E(s["ship_url"])}" rel="noopener" target="_blank">Listed on shiphelp.org</a></td></tr>
<tr><th scope="row">National SHIP line</th><td>1-877-839-2675</td></tr>
</tbody></table></div>
<p class="note">Numbers are copied from the shiphelp.org page for this state. If a line has changed, use the locator on that site.</p>
<h2>Medicaid and Medicare Savings Programs</h2>
<p>Medicare Savings Programs help pay Medicare premiums and, for QMB, other Medicare cost sharing. The 2026 federal income limits are on our <a href="{u("/guides/medicare-savings-programs/")}">savings program guide</a>. The state can use higher limits. Apply with the agency below, which is the row Medicaid.gov publishes.</p>
<div class="tablewrap"><table class="stats"><tbody>
<tr><th scope="row">Agency</th><td>{E(s["medicaid"]["agency"])}</td></tr>
{med_rows}
<tr><th scope="row">Website</th><td><a href="{E(s["medicaid"]["url"])}" rel="noopener" target="_blank">Agency link from Medicaid.gov</a></td></tr>
</tbody></table></div>
{higher}
<h2>Medigap in this state</h2>
{medigap_note(s)}
{doi}{extra_html}{compare}
<h2>What is the same in every state</h2>
<p>Part A and Part B rules, the 2026 federal premiums on our <a href="{u("/guides/medicare-costs-2026/")}">costs page</a>, and the <a href="{u("/guides/enrollment-periods/")}">enrollment deadlines</a> come from federal law. Advantage and drug plans that are actually sold here are local. Compare them on Medicare.gov or with the counseling program above. Read <a href="{u("/guides/original-medicare-vs-medicare-advantage/")}">Original Medicare or Medicare Advantage</a> before you pick a path.</p>
{mid}{faq_block(faqs)}
<section class="sources"><h2>Sources</h2>{src_list(sources)}
<p class="note">Last checked {checked}. SHIP facts are from that state's shiphelp.org page. Medicaid facts are from the Medicaid.gov state directory.</p></section>
{end}<p class="related"><a href="{u("/states/")}">All states</a> · <a href="{u("/guides/ship-counseling/")}">About SHIP</a> · <a href="{u("/guides/how-to-compare-plans/")}">How to compare plans</a></p>
</article>'''
        if extra:
            desc = extra["desc"]
            title = extra["title"]
            mod = extra["modified"]
        else:
            desc = f"Free Medicare counseling, Medicaid, and Medigap rules in {label}. Official phones, no plan sales."
            if len(desc) > 155:
                desc = f"SHIP, Medicaid, and Medigap contacts for {label}. Official numbers only. No plan sales."
            title = f"Which Medicare Help Is in {label}?"
            mod = None
        write(path, page(path, title, desc, body, [article_ld(h1, path, modified=mod), faq_ld(faqs)],
                         [("/", "Home"), ("/states/", "States"), (path, label)], kind="article", lastmod=mod))

def states_index():
    items = []
    for s in STATES:
        label = "District of Columbia" if s["slug"] == "district-of-columbia" else s["name"]
        items.append(f'<li><a href="{u("/states/" + s["slug"] + "/")}">{E(label)}</a></li>')
    faqs = [
        ("Which state page should I open?", "Open the state where you live. Each page lists the SHIP counseling program from shiphelp.org and the Medicaid agency from Medicaid.gov."),
        ("Do these pages list private premiums?", "No. Federal rules that do not change by state are linked. Private plan names and premiums are not listed."),
    ]
    body = f'''<article class="prose"><h1>Plan guides for all 50 states and the District of Columbia</h1>{byline()}{notice()}
<p>Each page lists the SHIP counseling program from shiphelp.org and the Medicaid agency from Medicaid.gov. Federal rules that do not change by state are linked, not repeated in full.</p>
{picker()}
<ul class="cols">{"".join(items)}</ul>
{faq_block(faqs)}</article>'''
    write("/states/", page("/states/", "Which State Medicare Page Should I Open?",
                           "SHIP counseling phones and Medicaid agencies for all 50 states and the District of Columbia.",
                           body, [article_ld("Plan guides for all 50 states and the District of Columbia", "/states/"), faq_ld(faqs)],
                           [("/", "Home"), ("/states/", "States")], kind="article"))

def home():
    cards = "".join(
        f'<li class="card"><h2><a href="{u(g["path"])}">{E(g["h1"])}</a></h2><p>{E(g["desc"])}</p></li>'
        for g in GUIDES[:6])
    faqs = [
        ("Which plan does this site tell me to pick?", "None. The guides explain Original Medicare, Medicare Advantage, Medigap letters, Part D, and enrollment deadlines. Medicare.gov and a SHIP counselor can show plans sold where you live. We do not sell plans."),
        ("Is Which Senior Plan part of Medicare?", "No. We are not affiliated with or endorsed by the U.S. government or the federal Medicare program."),
        ("Where do the dollar amounts come from?", "A dollar amount appears only when an official page labels it for that year, such as 2026 or 2027. Private plan premiums and plan names are not listed."),
    ]
    body = f'''<section class="hero"><h1>Which senior health plan should you look at?</h1>
<p class="answer">Plain English guides to Original Medicare, Medicare Advantage, Medigap letters, Part D, enrollment deadlines, and the free counseling office in every state. We cite Medicare.gov, CMS, shiphelp.org, and state agencies. We do not sell plans.</p>
{notice()}
{picker()}
<p class="btnrow"><a class="btn" href="{u("/guides/original-medicare-vs-medicare-advantage/")}">Compare the two paths</a> <a class="btn alt" href="{u("/guides/enrollment-periods/")}">See the deadlines</a></p>
</section>
<h2>Start here</h2><ul class="cards">{cards}</ul>
<h2>All {len(GUIDES)} guides</h2><p><a href="{u("/guides/")}">Browse every explainer</a>, from the <a href="{u("/guides/medicare-costs-2027/")}">2027 premium table</a> and the <a href="{u("/guides/irmaa-brackets-2027/")}">2027 IRMAA brackets</a> to Extra Help, PACE, and Medigap open enrollment. The <a href="{u("/guides/medigap-guaranteed-issue-rights/")}">guaranteed issue rights</a> page is the federal list of times a company must sell a Medigap policy. The <a href="{u("/guides/medicare-savings-programs/")}">2026 Medicare Savings Program limits</a> are the QMB, SLMB, and QI table. When you are ready to look at real contracts, read <a href="{u("/guides/how-to-compare-plans/")}">how to compare plans</a>.</p>
<h2>How the numbers are chosen</h2>
<p>A dollar amount appears only when an official page labels it for that year. Private plan premiums and plan names do not appear, because we will not invent them. The editorial rules are public on the <a href="{u("/editorial-policy/")}">editorial and sources policy</a>.</p>
{faq_block(faqs)}'''
    write("/", page("/", "Which Senior Health Plan Should I Pick?",
                    "Which senior health plan should you look at? Plain English guides to Original Medicare, Advantage, Medigap, Part D, and free counseling.",
                    body, faq_ld(faqs), lastmod="2026-11-21"))

def simple(path, title, desc, h1, inner, legal=False, modified=None):
    body = f'<article class="prose"><h1>{E(h1)}</h1>{inner}</article>'
    if legal:
        body = f'<article class="prose"><h1>{E(h1)}</h1>{inner}<p class="legal-line">{LEGAL_LINE}</p></article>'
    mod = modified or PUBLISHED
    write(path, page(path, title, desc, body, article_ld(h1, path, modified=mod),
                     [("/", "Home"), (path, h1)], legal=legal, kind="article", lastmod=mod))

def legal_pages():
    D = CHECKED
    simple("/about/", f"About {BRAND}", "What Which Senior Plan is, who it is for, and what it refuses to publish.",
           "About Which Senior Plan", f'''<p class="byline">By {BRAND}. Last checked {D}.</p>
<p>Which Senior Plan is an independent explainer of senior health plan choices in the United States. The question we answer is which kind of coverage exists, what the federal rules say, and who to call in your state.</p>
<h2>What we will not do</h2><p>We do not sell insurance, quote a premium, rank a company, or collect a form that an agent could use as a lead. We do not put the Medicare name in our logo, and we are not a government site.</p>
<h2>Where the facts come from</h2><p>Medicare.gov, CMS, shiphelp.org, Medicaid.gov, and state insurance departments we could open. The rules for what we will print are on the <a href="{u("/editorial-policy/")}">editorial and sources policy</a>.</p>
<p>See a mistake? <a href="{u("/contact/")}">Write to us</a> and include the page and the official source.</p>''')
    simple("/editorial-policy/", f"Editorial and Sources Policy | {BRAND}",
           "How Which Senior Plan checks Medicare facts, what it will not publish, and how to ask for a correction.",
           "Editorial and sources policy", f'''<p>Last updated 19 Nov 2026.</p>
<p>This is not legal advice. This is not medical advice. This is not insurance advice. The pages are general information so you can read the federal rules before you talk with Social Security, Medicare, a SHIP counselor, or your state.</p>
<h2>What we will publish</h2>
<ul>
<li>Rules and dollar amounts that we read on Medicare.gov, CMS.gov, SSA.gov, shiphelp.org, a state insurance department, or a state Medicaid agency.</li>
<li>The year the official page attaches to a dollar amount. A 2026 figure stays on a 2026 page. A 2027 figure stays on a 2027 page.</li>
<li>A last checked date, the source title, and the source URL on every guide and every state page.</li>
<li>The name and phone of a SHIP program or Medicaid agency only when the official directory prints them.</li>
</ul>
<h2>What we will not publish</h2>
<ul>
<li>A premium, copay, or plan name we did not read on an official page. Private plan prices are left to Medicare.gov and SHIP.</li>
<li>A recommendation to buy, drop, or switch a specific plan.</li>
<li>A figure for a later year on an earlier year page. The Extra Help page shows some copays under a 2027 heading; those stay off the 2026 Extra Help explainer until we publish a matching year page.</li>
<li>A state insurance department link we could not open. Ten states are missing that link on purpose.</li>
<li>Anything presented as an official Medicare communication. We are not affiliated with or endorsed by the U.S. government or the federal Medicare program.</li>
</ul>
<h2>How a page is corrected</h2>
<p>Email the address on the <a href="{u("/contact/")}">contact page</a> with the URL, the sentence, and the official page that disagrees. If we confirm the error, we change the page and we keep the last checked date honest. We do not backdate a page to look freshly updated when the words did not change.</p>
<h2>Dates</h2>
<p>datePublished on the first version of these pages is {PUBLISHED}, the day the sources were read. It is not the clock time of a later rebuild. dateModified changes only when the words change.</p>
<h2>Independence</h2>
<p>No insurer pays for a mention. There are no affiliate links. An AdSense account tag may be present for domain verification before any ad units appear. See the <a href="{u("/ad-disclosure/")}">advertising disclosure</a>.</p>''', legal=True, modified="2026-11-19")
    simple("/image-policy/", f"Image Policy | {BRAND}", "How Which Senior Plan handles images, logos, and government seals.",
           "Image policy", f'''<p>Last updated 19 Nov 2026.</p>
<h2>What we use</h2><p>The mark and the social image are simple graphics we drew for this site. They do not include a government seal, the Medicare name, or a picture of a person.</p>
<p class="brand-mark"><a href="{u("/image-policy/")}"><img src="{u("/logo.png")}" width="96" height="96" alt="Which Senior Plan mark"></a></p>
<p>Some guides use a photorealistic thumbnail created with AI. Those photos are labeled AI generated and link back to this page. They do not show a real identifiable person, a government seal, or a Medicare logo.</p>
<h2>What we do not use</h2><p>We do not use the Medicare card art, the CMS logo, state seals, or photos of real people. Any AI generated thumbnail stays labeled.</p>
<h2>Questions</h2><p>Copyright concerns go through the <a href="{u("/copyright/")}">copyright page</a> or the <a href="{u("/contact/")}">contact page</a>.</p>''', modified="2026-11-19")
    simple("/contact/", f"Contact {BRAND}", "Email Which Senior Plan at joshuaofisrael@gmail.com about a correction or a missing source.",
           "Contact", f'''<p>For a correction, a missing source, or a question about the site, email <a href="mailto:joshuaofisrael@gmail.com">joshuaofisrael@gmail.com</a>.</p>
<h2>What to include</h2><p>Send the page address, the sentence that looks wrong, and a link to the Medicare.gov, CMS, shiphelp.org, or state page that shows the current fact. We update the last checked date when we re read the source.</p>
<p>This is not a quote form. Do not send your Medicare number, Social Security number, bank details, or medical records. We will not use your email to sell you a plan or to pass you to an agent.</p>
<p>There is no form on this page on purpose. A form that asks for a phone number would look like lead generation, and we do not do that.</p>''')
    simple("/terms/", f"Terms of Use | {BRAND}", "Terms of use for Which Senior Plan, an independent explainer of senior health plan choices.",
           "Terms of use", f'''<p>Last updated {D}. These terms govern your use of whichseniorplan.com. Which Senior Plan is a trade name of Joshua Israel Ventures LLC, a Florida limited liability company. By using the site you agree to these terms.</p>
<h2>Information only</h2><p>The site gives general information about federal and state health coverage rules. This is not legal advice. This is not medical advice. This is not insurance advice. Plan rules, premiums, and enrollment rights can change. Read Medicare.gov and talk with Social Security or a SHIP counselor before you enroll.</p>
<h2>No agency relationship</h2><p>We are not affiliated with or endorsed by the U.S. government or the federal Medicare program, any state Medicaid agency, or any insurance company. Names are used so you can find the official program.</p>
<h2>Acceptable use</h2><p>You may link to our pages. You may not scrape the site in bulk, republish our original text without permission, or present the site as an official government publication.</p>
<h2>Intellectual property</h2><p>Original text, design, and graphics belong to Joshua Israel Ventures LLC. Federal and state names and marks belong to their owners.</p>
<h2>Disclaimer of warranties and limitation of liability</h2><p>The site is provided as is. To the fullest extent permitted by law, Joshua Israel Ventures LLC disclaims all warranties and is not liable for decisions you make about coverage. Our total liability for a claim relating to the site is limited to 100 dollars.</p>
<h2>Governing law</h2><p>These terms are governed by the laws of the State of Florida. Questions: email <a href="mailto:joshuaofisrael@gmail.com">joshuaofisrael@gmail.com</a>.</p>''', legal=True)
    simple("/privacy/", f"Privacy Policy | {BRAND}", "How Which Senior Plan handles email, hosting logs, and analytics.",
           "Privacy policy", f'''<p>Last updated 19 Nov 2026. Which Senior Plan is a trade name of Joshua Israel Ventures LLC, a Florida limited liability company.</p>
<h2>What we collect</h2><p>The site has no account, no quote form, and no shopping cart. If you email joshuaofisrael@gmail.com, we receive whatever you put in that email and we use it to reply. Do not include your Medicare number or medical records.</p>
<h2 id="analytics">Analytics</h2><p>{"Cloudflare Web Analytics loads on every public page and counts page views. It does not use cookies and it does not track you across other sites. Google Analytics 4 loads only after you accept the consent banner. Consent Mode v2 starts with ad storage, ad user data, ad personalization, and analytics storage denied. If you decline, the Google tag is not requested. Cookie settings in the footer opens that choice again. Accepting stores the choice in local storage in this browser. The site does not set its own tracking cookie. Advertising storage stays denied either way." if LAUNCH else "This preview build does not load Cloudflare Web Analytics or Google Analytics 4. The launch build loads Cloudflare Web Analytics on every page. That tool counts page views, does not use cookies, and does not track you across other sites. Google Analytics 4 loads only after you accept the consent banner. Consent Mode v2 starts with ad storage, ad user data, ad personalization, and analytics storage denied. If you decline, the Google tag is not requested. Cookie settings in the footer opens that choice again. Advertising storage stays denied either way."}</p>
<h2>Hosting</h2><p>GitHub Pages hosts the files and may log IP addresses for security.</p>
<h2 id="advertising">Advertising</h2><p>The site includes a Google AdSense account tag (publisher id {ADSENSE_PUB}) so Google can verify the domain. No ad units are placed on the pages yet, and Consent Mode keeps advertising storage denied until that changes. The authorized digital sellers file is at <a href="{u("/ads.txt")}">/ads.txt</a>. If display ads are turned on later, this section and the <a href="{u("/ad-disclosure/")}">advertising disclosure</a> will say so first. Advertisers do not edit guides. We do not sell insurance leads.</p>
<h2>Google advertising cookies and your choices</h2><p>Third-party vendors, including Google, use cookies to serve ads based on a user's prior visits to this website or other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visit to this site and/or other sites on the Internet. You may opt out of personalized advertising by visiting <a href="https://adssettings.google.com/" rel="nofollow noopener">Google Ads Settings</a>. Alternatively, you can opt out of a third-party vendor's use of cookies for personalized advertising at <a href="https://www.aboutads.info/choices/" rel="nofollow noopener">aboutads.info/choices</a>. For more information, see <a href="https://policies.google.com/technologies/partner-sites" rel="nofollow noopener">how Google uses information from sites or apps that use its services</a>.</p>
<h2>Children</h2><p>The site is not directed to children under 13.</p>''', legal=True, modified="2026-11-19")
    simple("/disclaimer/", f"Disclaimer | {BRAND}", "Which Senior Plan is not a government site, does not sell insurance, and does not give insurance advice.",
           "Disclaimer", f'''<p>Last updated {D}.</p>
<h2>Not a government site</h2><p>Which Senior Plan is not affiliated with or endorsed by the U.S. government or the federal Medicare program. It is not a state Medicaid agency and not a SHIP program. The Medicare name on these pages identifies the federal program. It is not our name.</p>
<h2>Not insurance advice and no sales</h2><p>This is not legal advice. This is not medical advice. This is not insurance advice. We do not sell plans, and we do not take leads. Enrollment deadlines and penalties are described so you can read the official rule. They are not a personal calculation.</p>
<h2>Figures go stale</h2><p>We label 2026 amounts and the date we checked the source. The official page controls if they disagree. Private premiums are not on this site because we did not publish a number we did not read.</p>
<h2>Limitation of liability</h2><p>To the extent permitted by law, Joshua Israel Ventures LLC is not liable for a coverage decision you make after reading the site. See the <a href="{u("/terms/")}">terms of use</a>.</p>''', legal=True)
    simple("/copyright/", f"Copyright and DMCA Policy | {BRAND}", "Copyright notice and how to send a DMCA takedown for Which Senior Plan.",
           "Copyright and DMCA policy", f'''<p>Last updated {D}. Original text and graphics are owned by Joshua Israel Ventures LLC. Facts are cited to public government and SHIP pages. See the <a href="{u("/image-policy/")}">image policy</a>.</p>
<h2>Reporting infringement</h2><p>Email <a href="mailto:joshuaofisrael@gmail.com">joshuaofisrael@gmail.com</a> with your name, a description of the work, the URL on our site, a good faith statement, a statement under penalty of perjury that you are the owner or authorized to act, and your signature. We review notices and remove material when the claim holds.</p>
<h2>Counter notice</h2><p>If we removed material and you believe that was a mistake, you may send a counter notice with the details required by 17 U.S.C. section 512(g).</p>''', legal=True)
    simple("/ad-disclosure/", f"Advertising Disclosure | {BRAND}", "Which Senior Plan AdSense status, affiliate links, and insurance lead policy.",
           "Advertising and affiliate disclosure", f'''<p>Last updated 19 Nov 2026. Which Senior Plan is free to read. We do not sell leads and we do not take payment from an insurance company for a mention. There are no affiliate links.</p>
<p>A Google AdSense account tag is present for publisher verification ({ADSENSE_PUB}). No ad units are shown on the pages yet. The sellers file is <a href="{u("/ads.txt")}">ads.txt</a>. If display ads start, they will be labeled and this page will change first. Advertisers will not get to edit a guide. Questions: <a href="mailto:joshuaofisrael@gmail.com">joshuaofisrael@gmail.com</a>.</p>''', legal=True, modified="2026-11-19")

def not_found():
    body = f'<h1>Page not found</h1><p>That address is not on this site. Try the <a href="{u("/guides/")}">guides</a> or the <a href="{u("/states/")}">state list</a>.</p>'
    write("/404.html", page("/404.html", f"Page not found | {BRAND}", "That page is not on Which Senior Plan. Browse the guides or pick a state.", body, noindex=True))

def images():
    logo = Image.new("RGB", (512, 512), "#12324a")
    d = ImageDraw.Draw(logo)
    d.rounded_rectangle((28, 28, 484, 484), radius=96, outline="#c4892a", width=22)
    d.ellipse((136, 110, 376, 350), fill="#f6f3ec")
    d.polygon([(256, 300), (150, 150), (196, 128), (256, 230), (316, 128), (362, 150)], fill="#0f5c63")
    d.rounded_rectangle((170, 360, 342, 410), radius=16, fill="#c4892a")
    logo.save(os.path.join(ROOT, "logo.png"), "PNG")
    og = Image.new("RGB", (1200, 630), "#12324a")
    g = ImageDraw.Draw(og)
    g.rectangle((0, 0, 18, 630), fill="#c4892a")
    fb = ImageFont.truetype(FONTB, 78)
    fs = ImageFont.truetype(FONT, 36)
    g.text((70, 200), "Which Senior Plan", font=fb, fill="#f6f3ec")
    g.text((70, 320), "Plain English guides by state", font=fs, fill="#e7d7b0")
    g.text((70, 390), "Not a government site. No plan sales.", font=fs, fill="#f6f3ec")
    og.save(os.path.join(ROOT, "og.png"), "PNG")
    svg = LOGO.replace('width="34" height="34" ', 'xmlns="http://www.w3.org/2000/svg" ').replace(' aria-hidden="true" focusable="false"', "")
    open(os.path.join(ROOT, "favicon.svg"), "w", encoding="utf-8").write(svg)

def extras():
    open(os.path.join(ROOT, "CNAME"), "w", encoding="utf-8").write("whichseniorplan.com\n")
    open(os.path.join(ROOT, f"{INDEXNOW_KEY}.txt"), "w", encoding="utf-8").write(INDEXNOW_KEY)
    open(os.path.join(ROOT, "ads.txt"), "w", encoding="utf-8").write("")  # AdSense detached 21 Nov 2026 until the account is approved (see seo-central/site-seo-rules.md). Do not re-add.
    bots = ["*", "Googlebot", "Bingbot", "Mediapartners-Google", "OAI-SearchBot", "ChatGPT-User", "GPTBot", "PerplexityBot", "Perplexity-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "Google-Extended", "Applebot", "Applebot-Extended", "DuckAssistBot", "Amazonbot", "CCBot", "Bytespider"]
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write("".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + f"Sitemap: {BASE}sitemap.xml\n")
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"<url><loc>{url(p)}</loc><lastmod>{m}</lastmod></url>\n" for p, m in PAGES) + "</urlset>\n")
    lines = [f"# {BRAND}", "",
             "> Which Senior Plan (whichseniorplan.com) explains Original Medicare, Medicare Advantage, Medigap letters, Part D, enrollment deadlines, SHIP counseling, and state Medicaid programs in plain English. It is not a government site, it does not sell plans, and it is not insurance advice.",
             "", "Dollar amounts are printed only for the year the official page labels them, including 2026 and 2027. Each guide shows its own last checked date.", "", "## Guides"]
    for g in GUIDES:
        lines.append(f"- [{g['h1']}]({url(g['path'])})")
    lines += ["", "## States"]
    for s in STATES:
        label = "District of Columbia" if s["slug"] == "district-of-columbia" else s["name"]
        lines.append(f"- [{label}]({url('/states/' + s['slug'] + '/')})")
    lines += ["", "## Policies", f"- [Editorial and sources]({url('/editorial-policy/')})", f"- [About]({url('/about/')})", f"- [Disclaimer]({url('/disclaimer/')})"]
    open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")

if __name__ == "__main__":
    guide_pages()
    guides_index()
    state_pages()
    states_index()
    home()
    legal_pages()
    not_found()
    images()
    extras()
    print(len(PAGES), "in sitemap", "LAUNCH" if LAUNCH else "NOINDEX")
