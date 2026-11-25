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

## Animated header (25 Nov)

- "Haldi & Mehndi" title with Hindi "हल्दी · मेहंदी · संगीत" underneath.
- A swaying marigold-and-mango-leaf toran (string garland) along the top.
- Falling marigold petals.
- A mehndi mandala that draws itself and slowly turns.
- All of it is in `build.py` (`hero_svg()`) and `style.css`. Motion is turned off for anyone whose phone asks for reduced motion.

## Accept / Reject for Divya (25 Nov)

- Each venue has animated **Accept** and **Reject** buttons at the top and bottom of its card. Code: `decide.js`.
- **Order:** accepted places move to the top under "💚 Accepted", rejected ones sink to the bottom under "✕ Rejected". Tapping the chosen button again undoes it.
- **Animations:** accept bursts marigold petals and stamps "Accepted 💚"; reject shakes the card, dims it and stamps "Rejected".
- **Tally:** a sticky bar shows the accepted / to-decide / rejected counts and whether the page is connected.
- **Sharing:** choices are saved in Firebase Realtime Database and shared live with everyone who opens the link:
  - project `phuket-trip-checklist` (rish.xi@gmail.com, free Spark plan, Singapore);
  - path `/haldi/<venue-id>` = `"yes"` or `"no"`.
- **Database rules** (published 25 Nov in the Firebase console):
  - Anyone can read `/haldi`.
  - Anyone can write `/haldi/<id>`, but only if the id matches `[a-z0-9-]{2,40}` and the value is `yes` or `no` (deleting is allowed).
  - Everything else stays locked, and the Phuket `/ticks` rule is unchanged.
- **Check her choices:** `curl -s https://phuket-trip-checklist-default-rtdb.asia-southeast1.firebasedatabase.app/haldi.json`
- **Tested 25 Nov:** accept, reject, undo, and a write from another device appearing live. All test choices were deleted afterwards, so the database was empty at publish time.

## History dropdown (26 Nov)

- Rejected places no longer stay in the list. They go into a **closed "✕ Rejected · kept for history" dropdown** at the very bottom, together with the places ruled out earlier (Malhar Haveli).
- Tapping "✕ n rejected" in the sticky bar opens the dropdown.
- Section headings show counts in brackets, e.g. "💚 Accepted (nothing yet)" and "🟢 Replied: to decide (7)".
