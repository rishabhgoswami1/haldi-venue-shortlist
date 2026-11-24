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


import math, random

def hero_svg():
    """Animated haldi + mehndi header: marigold toran, falling petals, self-drawing mehndi mandala."""
    rnd = random.Random(28)
    # --- marigold toran across the top ---
    toran = ['<svg class="toran" viewBox="0 0 1000 120" preserveAspectRatio="xMidYMin slice" aria-hidden="true">',
             '<defs><symbol id="mg" viewBox="-12 -12 24 24">'
             + "".join(f'<circle cx="{7*math.cos(a*math.pi/6):.2f}" cy="{7*math.sin(a*math.pi/6):.2f}" r="4.3" fill="#f07c12"/>' for a in range(12))
             + "".join(f'<circle cx="{4*math.cos(a*math.pi/4+0.3):.2f}" cy="{4*math.sin(a*math.pi/4+0.3):.2f}" r="3.4" fill="#f9a51a"/>' for a in range(8))
             + '<circle r="3" fill="#ffcd3c"/><circle r="1.4" fill="#e06a0a"/></symbol>'
             '<symbol id="leaf" viewBox="-6 0 12 30"><path d="M0 0 C7 8 6 22 0 30 C-6 22 -7 8 0 0Z" fill="#3f7d32"/><path d="M0 2 V28" stroke="#2c5b22" stroke-width=".8"/></symbol></defs>',
             '<path d="M-10 8 Q 125 26 250 8 T 500 8 T 750 8 T 1010 8" fill="none" stroke="#c2410c" stroke-width="3"/>']
    x = 12
    i = 0
    while x < 1000:
        L = [34, 52, 70, 52][i % 4]
        dur = 3.2 + (i % 5) * 0.35
        toran.append(f'<g class="hang" style="animation-duration:{dur:.2f}s;animation-delay:-{(i%7)*0.4:.1f}s">'
                     f'<line x1="{x}" y1="10" x2="{x}" y2="{L}" stroke="#b45309" stroke-width="1.2"/>'
                     + "".join(f'<use href="#mg" x="{x-9}" y="{y-9}" width="18" height="18"/>' for y in range(14, L + 1, 14))
                     + f'<use href="#mg" x="{x-11}" y="{L}" width="22" height="22"/></g>')
        if i % 2 == 0:
            toran.append(f'<g class="hang leafy" style="animation-duration:{dur+0.6:.2f}s"><use href="#leaf" x="{x+12}" y="8" width="11" height="28" transform="rotate(8 {x+17} 8)"/></g>')
        x += 46
        i += 1
    toran.append('</svg>')
    # --- falling petals ---
    petals = []
    for k in range(22):
        left = rnd.uniform(0, 100); dur = rnd.uniform(7, 13); delay = rnd.uniform(-13, 0); size = rnd.uniform(9, 18)
        drift = rnd.uniform(-60, 60)
        if k % 4 == 0:
            shape = f'<svg viewBox="-12 -12 24 24" width="{size+6:.0f}" height="{size+6:.0f}"><use href="#mg"/></svg>'
        else:
            col = rnd.choice(["#f59e0b", "#f97316", "#fbbf24", "#ea580c"])
            shape = f'<svg viewBox="0 0 10 16" width="{size*0.65:.0f}" height="{size:.0f}"><path d="M5 0 C10 5 9 12 5 16 C1 12 0 5 5 0Z" fill="{col}"/></svg>'
        petals.append(f'<span class="petal" style="left:{left:.1f}%;animation-duration:{dur:.1f}s;animation-delay:{delay:.1f}s;--drift:{drift:.0f}px">{shape}</span>')
    # --- mehndi mandala (draws itself) ---
    m = ['<svg class="mandala" viewBox="-130 -130 260 260" aria-hidden="true"><g class="spin">']
    d = 0
    def path(pd, w=2.2, extra=""):
        nonlocal d
        d += 1
        return f'<path d="{pd}" class="draw" style="animation-delay:{0.15*d:.2f}s" stroke-width="{w}" {extra}/>'
    m.append(path("M0 -10 A10 10 0 1 1 -0.01 -10Z", 2))
    m.append(path("M0 -22 A22 22 0 1 1 -0.01 -22Z"))
    for a in range(0, 360, 30):
        m.append(f'<g transform="rotate({a})">' + path("M0 -24 Q10 -40 0 -58 Q-10 -40 0 -24Z") + path("M0 -30 Q4 -40 0 -50", 1) + '</g>')
    m.append(path("M0 -64 A64 64 0 1 1 -0.01 -64Z", 1.2))
    for a in range(0, 360, 22.5) if False else [i*22.5 for i in range(16)]:
        m.append(f'<g transform="rotate({a})">' + path("M0 -68 Q16 -88 0 -110 Q-16 -88 0 -68Z") + path("M0 -76 Q6 -88 0 -100", 1) + '</g>')
    for a in range(24):
        ang = a * 15 * math.pi / 180
        m.append(f'<circle class="dot" cx="{118*math.sin(ang):.1f}" cy="{-118*math.cos(ang):.1f}" r="2.6" style="animation-delay:{3+a*0.05:.2f}s"/>')
    m.append('</g></svg>')
    return "".join(toran), "".join(petals), "".join(m)

TORAN, PETALS, MANDALA = hero_svg()

BADGE = {"replied": ("Replied", "b-ok"), "partial": ("Partly replied", "b-mid"), "none": ("No proper reply yet", "b-wait")}

def decide(vid, where):
    return (f'<div class="decide {where}" data-id="{vid}">'
            '<button type="button" class="dbtn yes" data-v="yes" aria-pressed="false"><span class="ico">💚</span><span class="lab">Accept</span><span class="shine"></span></button>'
            '<button type="button" class="dbtn no" data-v="no" aria-pressed="false"><span class="ico">✕</span><span class="lab">Reject</span></button>'
            '</div>')

def card(v):
    b, cls = BADGE[v["status"]]
    grp = "rep" if v["status"] != "none" else "wait"
    h = [f'<section class="venue" id="{v["id"]}" data-id="{v["id"]}" data-grp="{grp}"><div class="stamp" aria-hidden="true"></div>']
    h.append(decide(v["id"], "top"))
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
    h.append(decide(v["id"], "bottom"))
    h.append('</section>')
    return "\n".join(h)

def summary_row(v):
    b, cls = BADGE[v["status"]]
    return f'<a class="srow" data-id="{v["id"]}" href="#{v["id"]}"><span class="dot {cls}"></span><span class="sname">{html.escape(v["name"])}</span><span class="sinfo">{v["drive"].split(" from")[0].replace("<b>","").replace("</b>","")}</span></a>'

replied = [v for v in VENUES if v["status"] != "none"]
waiting = [v for v in VENUES if v["status"] == "none"]

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Haldi & Mehndi Venues</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Rozha+One&family=Yatra+One&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="hero haldi">
{TORAN}
<div class="petals" aria-hidden="true">{PETALS}</div>
{MANDALA}
<div class="hero-inner">
  <span class="eyebrow">🌼 Venue shortlist · Thu 28 Jan 2027</span>
  <h1 class="title"><span class="w-haldi">Haldi</span> <span class="amp">&amp;</span> <span class="w-mehndi">Mehndi</span></h1>
  <div class="hindi">हल्दी <span>·</span> मेहंदी <span>·</span> संगीत</div>
  <svg class="swash" viewBox="0 0 300 20" aria-hidden="true"><path d="M5 12 C 60 2, 110 20, 150 10 S 240 2, 295 12"/></svg>
  <p>About 50 guests for the day · about 22 staying 27–30 Jan · within about an hour of Vaishali</p>
  <div class="legend"><span>💚 Accept</span><span>✕ Reject</span><span>⚠️ Stock or edited photos flagged</span></div>
</div>
</header>
<main>
<div class="rules">These are <b>first findings</b>, not bookings. Prices are what each place told us (or Airbnb showed for 27–30 Jan) and still need confirming.<br><b>Your call:</b> tap <span class="mini yes">💚 Accept</span> or <span class="mini no">✕ Reject</span> on each place (top or bottom of its card). Accepted places rise to the top, rejected ones sink to the bottom, and it's saved for both of us. Tap again to undo.</div>
<div class="tally" id="tally"><span class="t-yes">💚 <b id="n-yes">0</b> accepted</span><span class="t-open">🤍 <b id="n-open">0</b> to decide</span><span class="t-no">✕ <b id="n-no">0</b> rejected</span><span class="sync" id="sync">Connecting…</span></div>

<section class="summary"><h2>At a glance <small>{len(VENUES)} places</small></h2>
<div class="slist">{"".join(summary_row(v) for v in VENUES)}</div></section>

<div class="board" id="board">
<h3 class="group g-yes" id="g-yes" hidden>💚 Accepted</h3>
<h3 class="group" id="g-rep">🟢 Replied: to decide</h3>
{"".join(card(v) for v in replied)}
<h3 class="group" id="g-wait">⏳ No proper reply yet</h3>
{"".join(card(v) for v in waiting)}
<h3 class="group g-no" id="g-no" hidden>✕ Rejected</h3>
</div>

<section><h2>Ruled out</h2>{"".join(f'<p class="note"><b>{a}</b>: {b}</p>' for a, b in OUT)}</section>

<footer>Updated {UPDATED} · Confirm everything before paying any advance.</footer>
</main>
<script src="decide.js"></script>
</body>
</html>
"""
open(os.path.join(HERE, "index.html"), "w").write(page)
print("index.html written:", len(page), "bytes;", sum(len(v["photos"]) for v in VENUES), "photos")
