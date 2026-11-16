# Which Senior Plan launch checklist

Status 16 Nov 2026: v1 is on `main` with `noindex` on every page, root relative paths, and `CNAME` containing `whichseniorplan.com`.

The domain exists and is still parked at Namecheap (`whichseniorplan.com` A `162.255.119.70`, `www` CNAME `parkingpage.namecheap.com`). GitHub Pages cannot serve the apex until DNS changes. No money was spent in this build.

## 1. Point DNS at GitHub Pages

In Namecheap Advanced DNS, remove the parking records, then:

- A records on `@`: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
- CNAME `www` to `joshuaofisrael.github.io`

## 2. Flip the index flag

```
./deploy.sh --launch
```

That rebuild removes `noindex`, adds the shared Cloudflare Web Analytics beacon, keeps root paths and the CNAME, and runs `check.py --launch` plus the legal gate. Commit and push that build only after DNS is answering for the apex.

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
