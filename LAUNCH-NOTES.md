# Which Senior Plan launch checklist

Status 16 Nov 2026: the committed pages are the preview build, with `noindex` on every page, root-relative paths, and `CNAME` containing `whichseniorplan.com`. `sitemap.xml` (with `lastmod`), `robots.txt`, `llms.txt`, and the IndexNow key file stay in place.

`GA4_ID` in `_build/build.py` is an empty string until you paste a measurement id of the form `G-XXXXXXXXXX`. Leave it blank in git until you have one. Do not put a secret in the file. A measurement id is public once a page loads it, but this repo does not invent one.

## Exact launch command

From the repository root, after `GA4_ID` is your measurement id:

```
python3 _build/build.py --launch
python3 _build/check.py --launch
python3 _build/legal_gate.py check
```

`./deploy.sh --launch` runs those three steps and does not push.

`check.py --launch` exits 1 if `GA4_ID` is empty, or if any page is missing the Cloudflare Web Analytics beacon or the GA4 loader. The loader sets Consent Mode v2 defaults to denied (`ad_storage`, `ad_user_data`, `ad_personalization`, `analytics_storage`) and `assets/consent.js` requests the Google tag only after the visitor accepts. Cookie settings in the footer reopens that choice. With a real id, the three commands exit 0.

Root-relative paths and `CNAME` `whichseniorplan.com` do not change. Commit and push the generated launch build only after DNS answers for the apex.

Preview, which is what this branch commits:

```
python3 _build/build.py
python3 _build/check.py
python3 _build/legal_gate.py check
```

The domain exists and is still parked at Namecheap (`whichseniorplan.com` A `162.255.119.70`, `www` CNAME `parkingpage.namecheap.com`). GitHub Pages cannot serve the apex until DNS changes. No money was spent in this build.

## 1. Point DNS at GitHub Pages

In Namecheap Advanced DNS, remove the parking records, then:

- A records on `@`: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
- CNAME `www` to `joshuaofisrael.github.io`

## 2. Build the indexable site

Set `GA4_ID` in `_build/build.py`, then run the exact launch command at the top of this file.

That build removes `noindex`, keeps the Cloudflare Web Analytics beacon on every page, and adds Google Analytics 4 behind the consent banner. The privacy page names both tools.

Then enforce HTTPS once the certificate is approved:

```
gh api repos/joshuaofisrael/whichseniorplan/pages
gh api -X PUT repos/joshuaofisrael/whichseniorplan/pages -F https_enforced=true
```

Check `curl -sI https://whichseniorplan.com/` and `curl -s https://whichseniorplan.com/ | grep -c noindex` (expect 0).

## 3. After the apex returns 200

- Confirm the beacon request on the live host.
- Add the domain property in Google Search Console and submit `https://whichseniorplan.com/sitemap.xml`.
- Bing import still needs Joshua's Microsoft sign in.
- Run `./indexnow.sh` (key file `c641d3cb68a0047708c9064020aa6977.txt`). Do not ping while the site is noindex.

## Gaps left on purpose

- No private plan names, star ratings, or premiums.
- Extra Help copays labeled 2027 on Medicare.gov are not copied onto the 2026 pages.
- Alaska and Hawaii Medicare Savings Program income limits are described as slightly higher. The higher dollar amounts were not printed on the federal table we read.
- State Medigap extras (birthday rules, under 65 sale requirements, rating method) are not listed, except the Massachusetts, Minnesota, and Wisconsin designs published on Medicare.gov.
- No confirmed insurance department homepage for Alaska, Arizona, Kansas, Louisiana, Massachusetts, Minnesota, Missouri, New Hampshire, New Mexico, or New York. Those pages say so instead of guessing a URL.
- Medicaid agency names are the ones Medicaid.gov prints. A consumer brand can differ (Oregon is listed as OregONEligibility; Tennessee is listed as the Department of Health).
- Territories are not separate pages. Puerto Rico Part B signup and the Extra Help exclusion for the territories are noted on the national pages.
- The Part B immunosuppressive drug income table was left off. The standard immunosuppressive premium of $121.60 is included.
