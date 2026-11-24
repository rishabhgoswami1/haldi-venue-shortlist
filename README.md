# Review website for Divya: haldi / mehndi / sangeet venues

- **Live:** https://rishabhgoswami1.github.io/haldi-venue-shortlist/
- **Repo:** github.com/rishabhgoswami1/haldi-venue-shortlist. It's public because GitHub Pages needs that on the free plan, and the page is marked `noindex`.
- **Built:** 25 Nov 2026 at the owner's request. It uses the same design as the Phuket family-trip site (`~/thailand-parents-trip/site`).

## How to update

1. Edit `VENUES` in `build.py`.
2. Put new photos in `img/<venue>/` as JPEGs, about 1,100 px wide.
3. Run `python3 build.py`.
4. Run `git add -A && git commit -m "…" && git push`.

## What it shows

- Replied places first, then places with no proper reply, then the ruled-out ones.
- For each place: map (or "ask them" when the location isn't known), contacts, Instagram, price, what they said, watch-outs, and photos.
- Stock or edited photos are flagged:
  - GoYard's "decor ideas";
  - Mansavi's marketing collages.

## Never on this public page

- Our budget.
- Family phone numbers or emails.
- Anything from `09-legal/`.
- The Airbnb host's private messages beyond the quoted reply (e.g. the Wi-Fi password one host sent).
