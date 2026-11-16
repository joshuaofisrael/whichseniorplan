#!/usr/bin/env python3
"""Site QA. Usage: check.py [--launch]
Preview (default): noindex on every page, root-relative paths, CNAME present, no beacon.
Launch: indexable except 404, Cloudflare beacon present, still no Medicare in the site name.
"""
import glob, html, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAUNCH = "--launch" in sys.argv
LEGAL = {"terms", "privacy", "disclaimer", "copyright", "ad-disclosure", "editorial-policy"}
NEED_BOTS = ["Googlebot", "Bingbot", "GPTBot", "ClaudeBot", "PerplexityBot", "OAI-SearchBot", "CCBot", "Google-Extended", "Applebot-Extended", "Bytespider"]
bad = 0
titles = {}

def fail(msg):
    global bad
    print(msg)
    bad += 1

files = [f for f in glob.glob(ROOT + "/**/*.html", recursive=True) if "/_build/" not in f]
for f in files:
    raw = open(f, encoding="utf-8").read()
    rel = os.path.relpath(f, ROOT)
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
        if len(d) > 155:
            fail(f"longdesc {len(d)} {rel}")
        if len(d) < 40:
            fail(f"shortdesc {len(d)} {rel}")
    if LAUNCH:
        if rel != "404.html" and "noindex" in raw:
            fail(f"noindex {rel}")
        if "static.cloudflareinsights.com/beacon.min.js" not in raw:
            fail(f"nobeacon {rel}")
    else:
        if "noindex" not in raw:
            fail(f"preview-missing-noindex {rel}")
        if "beacon.min.js" in raw:
            fail(f"preview-beacon {rel}")
    title = html.unescape(re.search(r"<title>(.*?)</title>", raw).group(1))
    titles.setdefault(title, []).append(rel)
    if len(title) > 70:
        fail(f"longtitle {len(title)} {title}")
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
        if 'class="faq"' in raw:
            if "FAQPage" not in raw:
                fail(f"nofaqschema {rel}")
            for q in re.findall(r"<summary>(.*?)</summary>", raw):
                if html.unescape(q) not in raw:
                    fail(f"faq-mismatch {rel} {q[:60]}")
        elif "FAQPage" in raw:
            fail(f"faqschema-without-visible {rel}")

for t, fs in titles.items():
    if len(fs) > 1:
        fail(f"duptitle {t} {fs}")

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
llms = open(os.path.join(ROOT, "llms.txt"), encoding="utf-8").read()
if "whichseniorplan.com/guides/" not in llms or "whichseniorplan.com/states/" not in llms:
    fail("llms")
print("files", len(files), "sitemap", len(locs), "issues", bad)
sys.exit(1 if bad else 0)
