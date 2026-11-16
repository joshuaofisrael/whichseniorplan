#!/bin/bash
# Ping IndexNow after the domain is live and pages are indexable. Do not run during noindex preview.
KEY=c641d3cb68a0047708c9064020aa6977
cd "$(dirname "$0")"
if [ $# -gt 0 ]; then URLS=$(printf '"%s",' "$@"); else URLS=$(grep -o '<loc>[^<]*' sitemap.xml | sed 's/<loc>//' | sed 's/.*/"&"/' | paste -sd, -); fi
curl -s -o /dev/null -w "IndexNow HTTP %{http_code}\n" -H "Content-Type: application/json; charset=utf-8" https://api.indexnow.org/indexnow \
 -d "{\"host\":\"whichseniorplan.com\",\"key\":\"$KEY\",\"keyLocation\":\"https://whichseniorplan.com/$KEY.txt\",\"urlList\":[${URLS%,}]}"
