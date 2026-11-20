#!/usr/bin/env python3
"""Site QA. Usage: check.py [--launch]
Preview (default): noindex on every page, root-relative paths, CNAME present, no beacon, no GA4.
Launch: indexable except 404, Cloudflare beacon and the GA4 loader on every page.
Fails if GA4_ID is empty, or if any page lacks the beacon or the GA4 loader.
"""
import glob, html, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "_build"))
from guides import GUIDES

# Paths in _build/thin-noindex.txt are intentionally noindex (AdSense low-value-content fix, 20 Nov 2026).
import os as _os
_THIN = set()
try:
    with open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "thin-noindex.txt"), encoding="utf-8") as _fh:
        _THIN = {l.strip().strip("/") for l in _fh if l.strip() and not l.startswith("#")}
except FileNotFoundError:
    pass


def _thin_rel(rel):
    r = str(rel).replace("\\", "/")
    if r.endswith("index.html"):
        r = r[: -len("index.html")]
    return r.strip("/") in _THIN


LAUNCH = "--launch" in sys.argv
LEGAL = {"terms", "privacy", "disclaimer", "copyright", "ad-disclosure", "editorial-policy"}
NEED_BOTS = ["Googlebot", "Bingbot", "GPTBot", "ClaudeBot", "PerplexityBot", "OAI-SearchBot", "CCBot", "Google-Extended", "Applebot-Extended", "Bytespider"]
FOOTER = ["/about/", "/contact/", "/privacy/", "/terms/", "/disclaimer/", "/copyright/", "/ad-disclosure/", "/image-policy/"]
KEY_FAQ = {
    "index.html",
    "guides/index.html",
    "states/index.html",
    "guides/original-medicare-vs-medicare-advantage/index.html",
    "guides/how-to-compare-plans/index.html",
    "guides/medigap-plan-letters/index.html",
    "guides/enrollment-periods/index.html",
}
BAD_SOURCE_HOSTS = ("wikipedia.org", "nerdwallet.com", "forbes.com", "reddit.com", "healthline.com", "youtube.com")
INDEXNOW_KEY = "c641d3cb68a0047708c9064020aa6977"
STATES = json.load(open(os.path.join(ROOT, "_build", "states.json"), encoding="utf-8"))
bad = 0
titles = {}
descs = {}
htmls = {}

def fail(msg):
    global bad
    print(msg)
    bad += 1

cfg = open(os.path.join(ROOT, "_build", "build.py"), encoding="utf-8").read()
gid_m = re.search(r'^GA4_ID = "([^"]*)"', cfg, re.M)
GA4_ID = gid_m.group(1) if gid_m else ""
if LAUNCH:
    if GA4_ID == "":
        fail("empty-ga4-id")
    elif not re.fullmatch(r"G-[A-Za-z0-9]+", GA4_ID):
        fail("bad-ga4-id")

consent_js = open(os.path.join(ROOT, "assets", "consent.js"), encoding="utf-8").read()
if "data-gtag-src" not in consent_js or "analytics_storage" not in consent_js:
    fail("consent-js")
if consent_js.count("loadGa()") != 3:
    fail("consent-js-calls")
if re.search(r"G-[A-Za-z0-9]{4,}", consent_js):
    fail("consent-js-hardcoded-id")

files = [f for f in glob.glob(ROOT + "/**/*.html", recursive=True) if "/_build/" not in f]
for f in files:
    raw = open(f, encoding="utf-8").read()
    rel = os.path.relpath(f, ROOT)
    htmls[rel] = raw
    top = rel.split("/")[0]
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', raw, re.S):
        try:
            json.loads(m)
        except Exception as e:
            fail(f"JSONLD {rel} {e}")
    vis = re.sub(r"<script.*?</script>", "", raw, flags=re.S)
    if top not in LEGAL and re.search(r"Joshua|Israel Ventures|©", vis):
        fail(f"LLC/© {rel}")
    if top in LEGAL and "is a trade name of Joshua Israel Ventures LLC" not in raw:
        fail(f"nolegalline {rel}")
    if not re.search(r'<link rel="canonical" href="https://whichseniorplan\.com/', raw):
        fail(f"canonical {rel}")
    if "github.io" in raw:
        fail(f"github.io {rel}")
    if raw.count("<h1") != 1:
        fail(f"h1count {rel} {raw.count('<h1')}")
    if "—" in raw or "–" in raw:
        fail(f"dash {rel}")
    brand = re.search(r'<span>(.*?)</span>', raw)
    if brand and "Medicare" in brand.group(1):
        fail(f"brand-medicare {rel}")
    svg = re.search(r"<svg[\s\S]*?</svg>", raw)
    if svg and re.search(r"Medicare", svg.group(0), re.I):
        fail(f"logo-medicare {rel}")
    desc = re.search(r'<meta name="description" content="(.*?)"', raw)
    if not desc:
        fail(f"nodesc {rel}")
    else:
        d = html.unescape(desc.group(1))
        descs.setdefault(d, []).append(rel)
        if len(d) > 155:
            fail(f"longdesc {len(d)} {rel}")
        if len(d) < 40:
            fail(f"shortdesc {len(d)} {rel}")
    if LAUNCH:
        if rel != "404.html" and "noindex" in raw and not _thin_rel(rel):
            fail(f"noindex {rel}")
        if "static.cloudflareinsights.com/beacon.min.js" not in raw:
            fail(f"nobeacon {rel}")
        if 'id="ga4-loader"' not in raw or "https://www.googletagmanager.com/gtag/js" not in raw or "/assets/consent.js" not in raw:
            fail(f"noga4 {rel}")
        if "'analytics_storage':'denied'" not in raw or "'ad_storage':'denied'" not in raw or "'ad_user_data':'denied'" not in raw or "'ad_personalization':'denied'" not in raw:
            fail(f"noconsent {rel}")
        attr = re.search(r'id="ga4-loader"[^>]*data-ga4-id="([^"]*)"', raw)
        if not attr or attr.group(1) != GA4_ID:
            fail(f"ga4-id-attr {rel}")
        if "Cookie settings" not in raw or 'id="cookie-settings"' not in raw:
            fail(f"nocookiesettings {rel}")
    else:
        if "noindex" not in raw:
            fail(f"preview-missing-noindex {rel}")
        if "beacon.min.js" in raw:
            fail(f"preview-beacon {rel}")
        if "ga4-loader" in raw or "googletagmanager.com" in raw or "/assets/consent.js" in raw:
            fail(f"preview-ga4 {rel}")
    title = html.unescape(re.search(r"<title>(.*?)</title>", raw).group(1))
    titles.setdefault(title, []).append(rel)
    if len(title) >= 60:
        fail(f"longtitle {len(title)} {title}")
    for prop in ("og:title", "og:description", "og:url", "og:image", "og:type", "og:site_name"):
        if f'property="{prop}"' not in raw:
            fail(f"og {prop} {rel}")
    if rel == "index.html" and '"@type": "WebSite"' not in raw:
        fail("nowebsite")
    if rel not in ("index.html", "404.html") and '"@type": "Article"' not in raw:
        fail(f"noarticle {rel}")
    if 'class="crumbs"' in raw and '"@type": "BreadcrumbList"' not in raw:
        fail(f"nocrumbs {rel}")
    if 'class="faq"' in raw:
        if "FAQPage" not in raw:
            fail(f"nofaqschema {rel}")
        for q in re.findall(r"<summary>(.*?)</summary>", raw):
            if html.unescape(q) not in raw:
                fail(f"faq-mismatch {rel} {q[:60]}")
    elif "FAQPage" in raw:
        fail(f"faqschema-without-visible {rel}")
    if rel in KEY_FAQ and ('class="faq"' not in raw or "FAQPage" not in raw):
        fail(f"keyfaq {rel}")
    if "Not insurance advice" not in raw:
        fail(f"noymyl {rel}")
    if "not affiliated with or endorsed by" not in raw:
        fail(f"noaffil {rel}")
    for href in FOOTER:
        if f'href="{href}"' not in raw:
            fail(f"footer {href} {rel}")
    if "Cookie settings" not in raw or 'id="cookie-settings"' not in raw:
        fail(f"nocookiesettings {rel}")
    for img in re.finditer(r"<img\b", raw, re.I):
        pre = raw[max(0, img.start() - 500):img.start()]
        a = pre.rfind("<a ")
        chunk = pre[a:] if a >= 0 else ""
        if a < 0 or "</a>" in chunk or 'href="/image-policy/"' not in chunk:
            fail(f"img-policy {rel}")
    for link in re.findall(r'(?:href|src)="(/[^"#?]*)', raw):
        if link.startswith("//"):
            fail(f"protocol-relative {rel} {link}")
            continue
        path = os.path.join(ROOT, link.lstrip("/"))
        if not (os.path.isfile(path) or os.path.isfile(os.path.join(path, "index.html"))):
            fail(f"broken {rel} {link}")
    if top in ("guides", "states") and rel.count("/") >= 2:
        sec = re.search(r'<section class="sources".*?</section>', raw, re.S)
        if not sec or not re.search(r'href="https://', sec.group(0) if sec else ""):
            fail(f"nosources {rel}")
        elif any(host in sec.group(0) for host in BAD_SOURCE_HOSTS):
            fail(f"unofficial {rel}")
        if not re.search(r'href="/guides/"', raw) and top == "guides":
            fail(f"nohub {rel}")
        if not re.search(r'href="/states/"', raw) and top == "states":
            fail(f"nohub {rel}")
        if 'class="related"' not in raw:
            fail(f"norelated {rel}")

for t, fs in titles.items():
    if len(fs) > 1:
        fail(f"duptitle {t} {fs}")
for d, fs in descs.items():
    if len(fs) > 1:
        fail(f"dupdesc {fs}")

hub = htmls.get("guides/index.html", "")
for g in GUIDES:
    rel = g["path"].strip("/") + "/index.html"
    if f'href="{g["path"]}"' not in hub:
        fail(f"hub-missing {g['path']}")
    page = htmls.get(rel, "")
    if not re.search(r'href="/guides/"', page):
        fail(f"detail-missing-hub {rel}")
shub = htmls.get("states/index.html", "")
for s in STATES:
    path = f'/states/{s["slug"]}/'
    rel = path.strip("/") + "/index.html"
    if f'href="{path}"' not in shub:
        fail(f"hub-missing {path}")
    if not re.search(r'href="/states/"', htmls.get(rel, "")):
        fail(f"detail-missing-hub {rel}")

priv = htmls.get("privacy/index.html", "")
if "Google Analytics 4" not in priv or "Cloudflare Web Analytics" not in priv:
    fail("privacy-analytics")

cname = os.path.join(ROOT, "CNAME")
if not os.path.isfile(cname) or open(cname).read().strip() != "whichseniorplan.com":
    fail("CNAME")
robots = open(os.path.join(ROOT, "robots.txt"), encoding="utf-8").read()
if "Sitemap: https://whichseniorplan.com/sitemap.xml" not in robots:
    fail("robots-sitemap")
for bot in NEED_BOTS:
    if f"User-agent: {bot}\n" not in robots or "Allow: /" not in robots:
        fail(f"robots-bot {bot}")
sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
if "404" in sm or "github.io" in sm:
    fail("sitemap-bad")
locs = re.findall(r"<loc>(.*?)</loc>", sm)
if len(locs) != len(set(locs)):
    fail("sitemap-dup")
for block in re.findall(r"<url>(.*?)</url>", sm, re.S):
    if not re.search(r"<lastmod>\d{4}-\d{2}-\d{2}</lastmod>", block):
        fail("sitemap-lastmod")
        break
llms = open(os.path.join(ROOT, "llms.txt"), encoding="utf-8").read()
if "whichseniorplan.com/guides/" not in llms or "whichseniorplan.com/states/" not in llms:
    fail("llms")
key_path = os.path.join(ROOT, INDEXNOW_KEY + ".txt")
if not os.path.isfile(key_path) or open(key_path, encoding="utf-8").read().strip() != INDEXNOW_KEY:
    fail("indexnow-key")
print("files", len(files), "sitemap", len(locs), "issues", bad)
sys.exit(1 if bad else 0)
