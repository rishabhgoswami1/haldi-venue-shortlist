/* Accept / Reject for each venue, shared live through Firebase Realtime Database.
   Data: /haldi/<venue-id> = "yes" | "no" (deleted = undecided). Rules allow only those values. */
(function () {
  var DB = "https://phuket-trip-checklist-default-rtdb.asia-southeast1.firebasedatabase.app/haldi";
  var CACHE = "haldi-decisions-v1";
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var board = document.getElementById("board");
  var cards = Array.prototype.slice.call(board.querySelectorAll("section.venue"));
  cards.forEach(function (c, i) { c.dataset.idx = i; });
  var rows = Array.prototype.slice.call(document.querySelectorAll(".srow[data-id]"));
  var slist = rows.length ? rows[0].parentNode : null;
  rows.forEach(function (r, i) { r.dataset.idx = i; });
  var heads = { yes: byId("g-yes"), rep: byId("g-rep"), wait: byId("g-wait"), no: byId("g-no") };
  var syncEl = byId("sync");
  var rejlist = byId("rejlist");
  var state = {};
  var first = true;

  function byId(id) { return document.getElementById(id); }
  function setSync(t, ok) { syncEl.textContent = t; syncEl.className = "sync " + (ok ? "ok" : "warn"); }
  try { state = JSON.parse(localStorage.getItem(CACHE)) || {}; } catch (e) { state = {}; }
  function cache() { try { localStorage.setItem(CACHE, JSON.stringify(state)); } catch (e) {} }

  function bucket(c) {
    var d = state[c.dataset.id];
    return d === "yes" ? "yes" : d === "no" ? "no" : c.dataset.grp;
  }

  function render(animate) {
    // remember positions (FLIP)
    var before = {};
    if (animate && !reduce) cards.forEach(function (c) { before[c.dataset.id] = c.getBoundingClientRect().top; });

    var groups = { yes: [], rep: [], wait: [], no: [] };
    cards.forEach(function (c) { groups[bucket(c)].push(c); });
    Object.keys(groups).forEach(function (g) { groups[g].sort(function (a, b) { return a.dataset.idx - b.dataset.idx; }); });
    ["yes", "rep", "wait", "no"].forEach(function (g) {
      board.appendChild(heads[g]);
      heads[g].hidden = groups[g].length === 0;
      groups[g].forEach(function (c) { (g === "no" ? rejlist : board).appendChild(c); });
    });
    heads.no.hidden = false; // always shown: also holds the places ruled out earlier
    byId("rej-n").textContent = groups.no.length + document.querySelectorAll("#g-no .ruled").length;

    cards.forEach(function (c) {
      var d = state[c.dataset.id] || "";
      c.classList.toggle("is-yes", d === "yes");
      c.classList.toggle("is-no", d === "no");
      c.querySelectorAll(".dbtn").forEach(function (b) { b.setAttribute("aria-pressed", b.dataset.v === d ? "true" : "false"); });
      var st = c.querySelector(".stamp");
      st.textContent = d === "yes" ? "Accepted 💚" : d === "no" ? "Rejected" : "";
    });

    // summary list order + marks
    if (slist) {
      var order = { yes: 0, rep: 1, wait: 1, no: 2 };
      rows.slice().sort(function (a, b) {
        var ca = byId(a.dataset.id), cb = byId(b.dataset.id);
        return (order[bucket(ca)] - order[bucket(cb)]) || (a.dataset.idx - b.dataset.idx);
      }).forEach(function (r) {
        var d = state[r.dataset.id] || "";
        r.dataset.state = d;
        slist.appendChild(r);
      });
    }

    var label = { yes: "💚 Accepted", rep: "🟢 Replied: to decide", wait: "⏳ No proper reply yet" };
    ["yes", "rep", "wait"].forEach(function (g) {
      var n = groups[g].length;
      heads[g].textContent = label[g] + " (" + (n ? n : g === "yes" ? "nothing yet" : 0) + ")";
    });
    heads.yes.hidden = false; // always visible, "(nothing yet)" until something is accepted

    byId("n-yes").textContent = groups.yes.length;
    byId("n-no").textContent = groups.no.length;
    byId("n-open").textContent = groups.rep.length + groups.wait.length;

    if (animate && !reduce) {
      cards.forEach(function (c) {
        var rect = c.getBoundingClientRect();
        if (!rect.height) return; // tucked inside the closed "Rejected" dropdown
        var dy = before[c.dataset.id] - rect.top;
        if (dy && c.animate) c.animate([{ transform: "translateY(" + dy + "px)" }, { transform: "none" }], { duration: 750, easing: "cubic-bezier(.2,.85,.25,1)" });
      });
    }
  }

  function burst(btn, kind) {
    if (reduce) return;
    var r = btn.getBoundingClientRect();
    var cx = r.left + r.width / 2, cy = r.top + r.height / 2;
    var n = kind === "yes" ? 18 : 8;
    for (var i = 0; i < n; i++) {
      var p = document.createElement("span");
      p.className = "spark " + kind;
      var ang = (Math.PI * 2 * i) / n + Math.random() * 0.4;
      var dist = (kind === "yes" ? 70 : 40) + Math.random() * 50;
      p.style.left = cx + "px"; p.style.top = cy + "px";
      p.style.setProperty("--dx", Math.cos(ang) * dist + "px");
      p.style.setProperty("--dy", Math.sin(ang) * dist - (kind === "yes" ? 30 : 0) + "px");
      p.style.setProperty("--rot", (Math.random() * 720 - 360) + "deg");
      p.textContent = kind === "yes" ? ["🌼", "💛", "🧡", "🌸", "✨"][i % 5] : "·";
      document.body.appendChild(p);
      setTimeout((function (el) { return function () { el.remove(); }; })(p), 1300);
    }
  }

  function decide(id, val, btn) {
    var c = byId(id);
    var cur = state[id] || "";
    var next = cur === val ? "" : val; // tapping the active choice again undoes it
    if (next) state[id] = next; else delete state[id];
    cache();
    if (next === "yes") { burst(btn, "yes"); flash(c, "pop-yes"); }
    if (next === "no") { burst(btn, "no"); flash(c, "pop-no"); if (!heads.no.open) setTimeout(function () { c.classList.add("leaving"); }, 300); }
    // let the card react in place first, then glide to its new spot
    setTimeout(function () {
      render(true);
      c.classList.remove("leaving");
      if (next === "yes" && !reduce) setTimeout(function () { c.scrollIntoView({ behavior: "smooth", block: "start" }); }, 780);
    }, reduce ? 0 : 520);
    var req = next
      ? fetch(DB + "/" + id + ".json", { method: "PUT", body: JSON.stringify(next) })
      : fetch(DB + "/" + id + ".json", { method: "DELETE" });
    req.then(function (r) { if (!r.ok) throw new Error(r.status); setSync("✓ Saved for both of us", true); })
       .catch(function () { setSync("⚠️ No internet: saved on this phone only for now", false); });
  }

  function flash(c, cls) {
    if (reduce) return;
    c.classList.remove("pop-yes", "pop-no");
    void c.offsetWidth;
    c.classList.add(cls);
    setTimeout(function () { c.classList.remove(cls); }, 900);
  }

  document.querySelectorAll(".decide").forEach(function (bar) {
    bar.addEventListener("click", function (e) {
      var b = e.target.closest(".dbtn");
      if (!b) return;
      decide(bar.dataset.id, b.dataset.v, b);
    });
  });

  // ---- live sync ----
  function applyAll(data) {
    state = {};
    Object.keys(data || {}).forEach(function (k) { if (data[k] === "yes" || data[k] === "no") state[k] = data[k]; });
    cache(); render(!first); first = false;
  }
  function applyPath(path, data) {
    if (path === "/") { applyAll(data); return; }
    var k = path.replace(/^\//, "");
    var v = (data === "yes" || data === "no") ? data : "";
    if ((state[k] || "") === v) return; // our own write echoing back
    if (v) state[k] = v; else delete state[k];
    cache(); render(true);
  }
  function connect() {
    if (!window.EventSource) { poll(); return; }
    var es = new EventSource(DB + ".json");
    es.addEventListener("put", function (e) { var m = JSON.parse(e.data); applyPath(m.path, m.data); setSync("✓ Live: choices are shared", true); });
    es.addEventListener("patch", function (e) { var m = JSON.parse(e.data); Object.keys(m.data || {}).forEach(function (k) { applyPath("/" + k, m.data[k]); }); });
    es.onerror = function () { setSync("⚠️ Offline: showing the last saved choices", false); };
  }
  function poll() {
    fetch(DB + ".json").then(function (r) { return r.json(); }).then(function (d) { applyAll(d); setSync("✓ Live: choices are shared", true); })
      .catch(function () { setSync("⚠️ Offline: showing the last saved choices", false); });
    setTimeout(poll, 15000);
  }

  var tno = document.querySelector(".tally .t-no");
  if (tno) tno.addEventListener("click", function () {
    if (heads.no.hidden) return;
    heads.no.open = true;
    heads.no.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
  });

  render(false);
  connect();
})();
