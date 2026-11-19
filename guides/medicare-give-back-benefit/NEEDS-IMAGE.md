# Needs image (do not merge until added)

- Page: `/guides/medicare-give-back-benefit/`
- Required file: `assets/images/calculator-tax-forms.png` (and optional `-thumb.png`)
- Bank path assigned 19 Nov 2026: `/workspace/image-bank/fiscalhour/calculator-tax-forms.png`
- Scene: desk calculator with tax or benefit paperwork (no logos, no readable personal data, no real faces)
- After the PNG is in `assets/images/`, wire it on the give-back guide in `_build/guides.py` as the AI-labeled hero thumbnail linking to `/image-policy/`, add mid/end next-reads with thumbs, rebuild with `./deploy.sh --launch`, then merge.
