"""Builds index.html for the haldi / mehndi / sangeet venue review site.

Source of truth for the facts: ~/wedding-planning/01-haldi-mehndi-sangeet/shortlist-28jan.md and
comms/outreach.md. Edit VENUES below, then run:  python3 build.py
Never put our budget, family phone numbers or anything from 09-legal on this public page.
"""
import html, os
from urllib.parse import quote_plus

HERE = os.path.dirname(os.path.abspath(__file__))
UPDATED = "25 Nov 2026"

def maps(q):
    return "https://www.google.com/maps/search/?api=1&query=" + quote_plus(q)

def imgs(folder):
    d = os.path.join(HERE, "img", folder)
    return [f"img/{folder}/{f}" for f in sorted(os.listdir(d)) if f.endswith(".jpg")]

# status: replied | partial | none | out
VENUES = [
    dict(
        id="mansavi", status="replied", name="Mansavi Villa HomeStay", kind="Homestay villa · 10 rooms",
        area="Ansal Golf Links-1, Sector Omega-1, Greater Noida", drive="55–75 min from Vaishali (may be over 1 hour)",
        map=maps("Mansavi Villa HomeStay, Ansal Golf Links 1, Greater Noida"), map_note="Address from their email",
        sleeps="All 22 ✔ (10 rooms on 27 + 28 Jan; 7 rooms + 6 mattresses on 29 Jan)",
        price="<b>₹2,05,830 + GST</b> all-in: stay ₹1,15,830 (after 10% off) + function package ₹90,000 (₹1,800 × 50: their food, standard decor, DJ, terrace free)",
        said=[
            "Confirmed rooms for all 22 for 27–30 Jan; on 29 Jan 3 rooms go to a corporate group, so 6 extra mattresses.",
            "Sent a full written quote (22 Nov): 50% advance to confirm, rest by 20 Jan; free cancellation until 16 Jan, then 50% on 17 Jan and 100% after.",
            "Food only through their caterer (no outside caterer in the kitchen). Haldi / mehndi decor and floor protection are quoted separately.",
            "Function is on their <b>rooftop terrace</b> (small front lawn). Outdoor music until 10 pm. Invited us for a visit.",
        ],
        watch="Over 1 hour away; terrace rather than a garden; most expensive so far but includes food for 50.",
        contacts=[("WhatsApp / call", "https://wa.me/919990414014", "+91 99904 14014"), ("Email", "mailto:mansavi.villa@gmail.com", "mansavi.villa@gmail.com"), ("Website", "https://mansavivilla.com", "mansavivilla.com")],
        photos=imgs("mansavi"), photo_note="⚠️ These are <b>their own marketing collages</b>: the pictures inside look like real photos of their terrace and lawn, but heavily edited. Check the real space at a visit.", photo_flag=True,
    ),
    dict(
        id="clementine", status="replied", name="Clementine Farms", kind="Farmhouse with pool · 4 rooms + hall",
        area="Flora Farm 509, Nagli Bahrampur, Sector 135, Noida", drive="45–50 min from Vaishali",
        map=maps("Flora Farm 509, Nagli Bahrampur, Sector 135, Noida"), map_note="Address from their listing, pin not confirmed: ask them for a location pin",
        sleeps="About 20 (5 double beds, 1 bunk bed, sofa-cum-bed, 4 spare mattresses). 22 is a squeeze",
        price="<b>₹20,000 for 15 people</b> (per night, to confirm) + ₹1,000 per extra person + <b>₹35,000 per function</b>. For 22 people × 3 nights + function ≈ <b>₹1.16 lakh</b> if it is per night",
        said=[
            "Available 27–30 Jan.",
            "No catering or decoration of their own, but they share vendor contacts.",
            "Pool 16×32 ft, pool deck works as a dance floor, outdoor kitchen + barbecue, fire pit, 6,000 sq ft lawn, generator 10 h free then ₹300/h.",
        ],
        watch="Tiny Instagram (about 20 followers). Ask whether ₹20k is per night or for the whole stay.",
        contacts=[("WhatsApp / call", "https://wa.me/918076313994", "+91 80763 13994"), ("Instagram", "https://www.instagram.com/clementinefarms509/", "@clementinefarms509")],
        photos=imgs("clementine"), photo_note="Real phone photos they sent on WhatsApp (two are stills from videos of their parties). No stock pictures seen.", photo_flag=False,
    ),
    dict(
        id="airbnb-pilkhuwa", status="replied", name="Hottley-Lavender Farm (Airbnb)", kind="Farmhouse · 6 bedrooms · 7 bathrooms · private pool · chef",
        area="Pilkhuwa, Uttar Pradesh (towards Hapur on NH-9)", drive="About 45–60 min from Vaishali (estimate)",
        map=maps("Pilkhuwa, Uttar Pradesh"), map_note="Airbnb shows only the area; exact address after booking, so ask the host",
        sleeps="Listed for 16+ guests, 6 beds. Ask about mattresses for 22",
        price="<b>₹78,150</b> for 3 nights (27–30 Jan) for 16 guests, incl. ₹11,921 taxes. Extra-guest charge for 22: ask",
        said=["Host Yash (1,063 reviews as a host): “Hello, Yes you can do” to our haldi + sangeet plan with outside decoration."],
        watch="Listing has only 5 reviews (5.0, Guest favourite). Ask for the exact location and the price for 22.",
        contacts=[("Airbnb listing", "https://www.airbnb.co.in/rooms/1721620218985349013", "Open on Airbnb")],
        photos=imgs("airbnb-pilkhuwa"), photo_note="Photos from the Airbnb listing: professional, look real (no stock).", photo_flag=False,
    ),
    dict(
        id="airbnb-noida", status="replied", name="The Grand Escape 112 (Airbnb)", kind="Luxury farmhouse · 4 bedrooms · pool",
        area="Noida (exact sector after booking)", drive="About 35–50 min from Vaishali (estimate)",
        map=maps("Noida Uttar Pradesh"), map_note="Airbnb shows only the area; exact address after booking, so ask the host",
        sleeps="Listed for 16+ guests (4 double beds + 4 sofas). Above 16: ₹1,000 per guest",
        price="<b>₹1,11,392</b> for 3 nights for 16 guests, incl. ₹16,992 taxes. For 22 add about ₹1,000 × 6 per night",
        said=[
            "Co-host Zaid: up to 16 guests included, ₹1,000 per extra guest; decorating is fine if nothing is damaged; the event is possible.",
            "Ace Stay Homes: they also have in-house decorators and caterers “at affordable prices”.",
        ],
        watch="New host account (about 1 month), 4 reviews (5.0).",
        contacts=[("Airbnb listing", "https://www.airbnb.co.in/rooms/1801365901927940835", "Open on Airbnb")],
        photos=imgs("airbnb-noida"), photo_note="Photos from the Airbnb listing: professional, look real (no stock).", photo_flag=False,
    ),
    dict(
        id="mulberry", status="replied", name="Mulberry Farm", kind="Farm cottage · 3 bedrooms · pool · big lawn",
        area="Green Beauty Farms, Sector 135, Noida", drive="45–50 min from Vaishali",
        map=maps("Mulberry Farm Sector 135 Noida"), map_note="Search pin, not confirmed: ask them for a location pin",
        sleeps="<b>Only 11 people</b> (“3bhk with farm with 4 toilets”). Extra rooms at their hotel in Sector 94",
        price="<b>27 Jan already booked.</b> 28 Jan ₹35,000 · 29 Jan ₹15,000 · 30 Jan ₹15,000",
        said=[
            "Could work only as the 28 Jan function venue, with the stay elsewhere.",
            "Asked on 24 Nov: “Pls confirm your booking”. Nothing booked.",
        ],
        watch="Doesn't fit 22 people, and the 27 Jan arrival night is taken.",
        contacts=[("WhatsApp / call", "https://wa.me/919599760808", "+91 95997 60808"), ("Website", "https://mulberryfarm.in/", "mulberryfarm.in")],
        photos=imgs("mulberry"), photo_note="Real photos they sent on WhatsApp (pool with fairy lights, cottage, gazebo, rooms). A gate poster says “Corporate Party”, so they do host events.", photo_flag=False,
    ),
    dict(
        id="lotus", status="replied", name="Lotus Farm (via GoYard)", kind="Farmhouse · 4BHK · lawn, gazebo, pool",
        area="Sector 135, Noida (exact farm not shared)", drive="45–50 min from Vaishali",
        map=None, map_note="Location not shared yet: ask GoYard for the exact pin",
        sleeps="Up to about 30 with extra mattresses (GoYard)",
        price="4BHK listed around ₹18,000–22,000 per night. No written quote yet",
        said=[
            "GoYard (an agent) offered this farm and Priti Garden and said they can do all 3 days for us, verbally.",
            "Outside caterer and decorator OK; DJ until 10:30 pm; haldi, mehndi and sangeet allowed. They have an event there on 26 Jan.",
        ],
        watch="Agent, not the owner; no written quote; visit before paying anything.",
        contacts=[("WhatsApp / call (GoYard)", "https://wa.me/919315597376", "+91 93155 97376")],
        photos=imgs("goyard-lotus"), photo_note="Photos sent by GoYard on WhatsApp. They look like real photos of a farm, but they came from an agent, so confirm at a visit that it's the same place.", photo_flag=False,
    ),
    dict(
        id="priti", status="replied", name="Priti Garden (via GoYard)", kind="Cottage on a big lawn · 4BHK · pool",
        area="Sector 128, near Amity University, Noida", drive="35–45 min from Vaishali",
        map=None, map_note="Location not shared yet: ask GoYard for the exact pin",
        sleeps="Up to about 30 with extra mattresses (GoYard)",
        price="Same as Lotus Farm: 4BHK around ₹18,000–22,000 per night; no written quote",
        said=["Same GoYard terms as Lotus Farm. The pool was empty in their photos. They also sent a video of a reception held there."],
        watch="Agent, not the owner; no written quote.",
        contacts=[("WhatsApp / call (GoYard)", "https://wa.me/919315597376", "+91 93155 97376")],
        photos=imgs("goyard-priti"), photo_note="Photos sent by GoYard; look like real photos. Confirm at a visit.", photo_flag=False,
        extra=dict(title="⚠️ GoYard's “decor ideas” (flagged: not their own work)", note="GoYard said “all this work was done at the farm”, but at least two of these pictures carry other businesses' watermarks (WedMeGood, a decorator's logo). Treat them as a Pinterest-style mood board, not proof.", photos=imgs("goyard-decor-flagged")),
    ),
    dict(
        id="airbnb-gurugram", status="replied", name="Opulent Farms (Airbnb)", kind="Farm stay · 4 bedrooms · pool",
        area="Gurugram, Haryana", drive="<b>About 75–100 min from Vaishali, well over the 1-hour limit</b>",
        map=maps("Gurugram Haryana"), map_note="Airbnb shows only the area; exact address after booking",
        sleeps="Listed for 16+ guests (5 beds)",
        price="<b>₹76,211</b> for 3 nights for 16 guests, incl. ₹11,625 taxes",
        said=["Host Mayank (Superhost, 15 reviews, 4.93): “Yes we can plan this together. We have our decor team also who can help you with event decor.”"],
        watch="Too far for the families; kept only for completeness.",
        contacts=[("Airbnb listing", "https://www.airbnb.co.in/rooms/1629017916826716630", "Open on Airbnb")],
        photos=imgs("airbnb-gurugram"), photo_note="Photos from the Airbnb listing: look real (no stock).", photo_flag=False,
    ),
    # ---- no proper reply ----
    dict(
        id="brigadier", status="none", name="Brigadier's Retreat Farm", kind="Farmhouse · 5 rooms · lawn for about 100",
        area="Sector 135, Noida", drive="45–50 min from Vaishali",
        map=maps("Brigadier's Retreat Farm Sector 135 Noida"), map_note="Search pin, not confirmed",
        sleeps="5 rooms (listing)", price="Listing suggested about ₹20,000 per night plus extra-guest fees; no quote",
        said=["Offered a live video-call tour on 21 Nov; we asked for photos; no reply since."],
        watch="The only one with a haldi review online.", contacts=[("WhatsApp / call", "https://wa.me/919821213586", "+91 98212 13586")],
        photos=[], photo_note="", photo_flag=False,
    ),
    dict(
        id="partyvillas", status="none", name="PartyVillas: farm in Mohan Nagar", kind="Booking platform (agent Anushka)",
        area="Mohan Nagar, Ghaziabad", drive="15–30 min from Vaishali",
        map=None, map_note="No address yet: ask them",
        sleeps="Unknown", price="No price yet",
        said=["The 4 farms we picked on their site are “not in tieup” any more. Their only Ghaziabad farm is in Mohan Nagar; they asked “are you comfortable”."],
        watch="Closest option so far, but no photos or details.", contacts=[("WhatsApp (Anushka)", "https://wa.me/919818927372", "+91 98189 27372")],
        photos=[], photo_note="", photo_flag=False,
    ),
    dict(
        id="sloshout", status="none", name="Sloshout (booking platform)", kind="Agent (Deepali)",
        area="Delhi / Noida options", drive="—", map=None, map_note="Nothing shared yet",
        sleeps="—", price="—",
        said=["They asked for our guest numbers and dates. Our answer hasn't gone out yet."],
        watch="", contacts=[("WhatsApp (Deepali)", "https://wa.me/919818932385", "+91 98189 32385")],
        photos=[], photo_note="", photo_flag=False,
    ),
]

OUT = [("Malhar Haveli, Sector 40 Noida", "Rajasthani haveli look, not our style (7 rooms, about 20–21 people)")]

BADGE = {"replied": ("Replied", "b-ok"), "partial": ("Partly replied", "b-mid"), "none": ("No proper reply yet", "b-wait")}

def card(v):
    b, cls = BADGE[v["status"]]
    h = [f'<section class="venue" id="{v["id"]}">']
    h.append(f'<div class="vhead"><span class="badge {cls}">{b}</span>' + ('<span class="badge b-flag">⚠️ photos flagged</span>' if v.get("photo_flag") or v.get("extra") else '') + '</div>')
    h.append(f'<h2>{html.escape(v["name"])}</h2><div class="kind">{v["kind"]}</div>')
    rows = [("📍", "Where", f'{v["area"]}<small>{v["drive"]}</small>'), ("🛏️", "Sleeps", v["sleeps"]), ("💰", "Price", v["price"])]
    h.append('<div class="facts">' + "".join(f'<div class="fact"><span class="ic">{i}</span><div><b>{k}</b><div>{t}</div></div></div>' for i, k, t in rows) + '</div>')
    h.append('<div class="said"><div class="lbl">What they said</div><ul>' + "".join(f"<li>{s}</li>" for s in v["said"]) + '</ul></div>')
    if v.get("watch"):
        h.append(f'<div class="tip">👀 {v["watch"]}</div>')
    btns = []
    if v.get("map"):
        btns.append(f'<a class="btn" href="{v["map"]}" target="_blank" rel="noopener">🗺️ Map</a>')
    for lbl, href, txt in v["contacts"]:
        icon = "📸" if "instagram" in href else "🏠" if "airbnb" in href else "🌐" if lbl == "Website" else "✉️" if href.startswith("mailto") else "💬"
        btns.append(f'<a class="btn" href="{href}" target="_blank" rel="noopener">{icon} {html.escape(txt)}</a>')
    h.append('<div class="btns">' + "".join(btns) + '</div>')
    h.append(f'<div class="mapnote">{"🗺️ " if not v.get("map") else ""}{v["map_note"]}</div>')
    if v["photos"]:
        h.append(f'<details class="gal" open><summary>📷 Photos ({len(v["photos"])})</summary><p class="pnote{" flag" if v.get("photo_flag") else ""}">{v["photo_note"]}</p><div class="grid">' + "".join(f'<a href="{p}" target="_blank"><img src="{p}" loading="lazy" alt=""></a>' for p in v["photos"]) + '</div></details>')
    if v.get("extra"):
        e = v["extra"]
        h.append(f'<details class="gal"><summary>{e["title"]} ({len(e["photos"])})</summary><p class="pnote flag">{e["note"]}</p><div class="grid">' + "".join(f'<a href="{p}" target="_blank"><img src="{p}" loading="lazy" alt=""></a>' for p in e["photos"]) + '</div></details>')
    h.append('</section>')
    return "\n".join(h)

def summary_row(v):
    b, cls = BADGE[v["status"]]
    return f'<a class="srow" href="#{v["id"]}"><span class="dot {cls}"></span><span class="sname">{html.escape(v["name"])}</span><span class="sinfo">{v["drive"].split(" from")[0].replace("<b>","").replace("</b>","")}</span></a>'

replied = [v for v in VENUES if v["status"] != "none"]
waiting = [v for v in VENUES if v["status"] == "none"]

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Haldi Venue Shortlist</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="hero"><div class="hero-inner">
  <span class="eyebrow">💛 Haldi · Mehndi · Sangeet</span>
  <h1>Venue shortlist</h1>
  <p>Thu 28 Jan 2027 · about 50 guests · about 22 staying 27–30 Jan · within about an hour of Vaishali</p>
  <div class="legend"><span>🟢 Replied</span><span>⏳ No proper reply</span><span>⚠️ Stock or edited photos flagged</span></div>
</div></div>
<main>
<div class="rules">These are <b>first findings</b>, not bookings. Prices are what each place told us (or Airbnb showed for 27–30 Jan) and still need confirming. Tap a name to jump to it; tap a photo to open it full size.</div>

<section class="summary"><h2>At a glance <small>{len(VENUES)} places</small></h2>
<div class="slist">{"".join(summary_row(v) for v in VENUES)}</div></section>

<h3 class="group">🟢 Replied ({len(replied)})</h3>
{"".join(card(v) for v in replied)}

<h3 class="group">⏳ No proper reply yet ({len(waiting)})</h3>
{"".join(card(v) for v in waiting)}

<section><h2>Ruled out</h2>{"".join(f'<p class="note"><b>{a}</b>: {b}</p>' for a, b in OUT)}</section>

<footer>Updated {UPDATED} · Confirm everything before paying any advance.</footer>
</main>
</body>
</html>
"""
open(os.path.join(HERE, "index.html"), "w").write(page)
print("index.html written:", len(page), "bytes;", sum(len(v["photos"]) for v in VENUES), "photos")
