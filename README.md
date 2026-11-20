# Which Senior Plan (whichseniorplan.com)

Plain English guides to Original Medicare, Medicare Advantage, Medigap letters, Part D, enrollment deadlines, free SHIP counseling, and state Medicaid programs. Static site for Joshua Israel Ventures LLC. Not a government site. No plan sales.

GitHub Pages: branch `main`, folder `/`. `CNAME` is `whichseniorplan.com`.

## Status (16 Nov 2026)

v1 is built with `noindex` on every page. Root relative paths and the CNAME file are already in place. The domain still points at Namecheap parking (`162.255.119.70`, `www` to `parkingpage.namecheap.com`), so the public hostname will not serve this site until DNS is pointed at GitHub Pages.

## Build

```
python3 _build/build.py            # noindex, root paths, CNAME, no analytics beacon
python3 _build/build.py --launch   # indexable, Cloudflare beacon, GA4 after consent
python3 _build/check.py [--launch]
python3 _build/legal_gate.py check
./deploy.sh [--launch]             # build + check + legal gate, does not push
```

The exact launch command is in LAUNCH-NOTES.md. `check.py --launch` fails while `GA4_ID` in `_build/build.py` is empty.

`LAUNCH` in `_build/build.py` is the single flag (`--launch`). Dates are the constants `PUBLISHED` (`2026-11-16`) and `CHECKED` (`16 Nov 2026`). Do not replace them with the build clock. `GA4_ID` stays `""` until the owner pastes a `G-` measurement id.

## What v1 contains

- 24 national guides under `/guides/` (20 at launch, plus give back and PACE on 18 Nov 2026, plus Medicare costs 2027 on 19 Nov 2026, plus 2027 IRMAA brackets on 20 Nov 2026)
- 51 state pages (50 states and the District of Columbia) under `/states/`
- Home, guides index, states index with a state picker
- About, editorial and sources policy, image policy, contact (mailto joshuaofisrael@gmail.com, no form), terms, privacy, disclaimer, advertising disclosure, copyright
- `sitemap.xml` (83 URLs), `robots.txt` (Google, Bing, and AI crawlers, including Bytespider), `llms.txt`, IndexNow key file
- FAQPage, Article, BreadcrumbList, and home WebSite plus Organization schema

## Sources

Checked 16 Nov 2026. Dollar amounts are 2026 figures only where Medicare.gov or CMS labels them 2026. SHIP names and phones are from each state's live page on shiphelp.org, not the April 2022 PDF. Medicaid agency names and phones are from the Medicaid.gov state directory. No private plan names or premiums.

## Launch later

See LAUNCH-NOTES.md. Do not run `./indexnow.sh` while pages are `noindex` or before DNS serves the apex.
