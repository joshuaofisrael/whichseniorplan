# Needs image (do not merge until added)

- Page: `/guides/pace-program/`
- Required file: `assets/images/household-finances-paperwork.png` (and optional `-thumb.png`)
- Bank path assigned 19 Nov 2026: `/workspace/image-bank/fiscalhour/household-finances-paperwork.png`
- Scene: household finances paperwork on a table (no logos, no readable personal data, no real faces)
- After the PNG is in `assets/images/`, wire it on the PACE guide in `_build/guides.py` as the AI-labeled hero thumbnail linking to `/image-policy/`, add mid/end next-reads with thumbs, rebuild with `./deploy.sh --launch`, then merge.
