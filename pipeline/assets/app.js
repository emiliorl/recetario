// Home: search, category and tag filters (kept in the URL). Recipe: saved checkboxes, tappable steps, keep-screen-on.
(function () {
  "use strict";

  function normalize(text) {
    return text.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9 ]/g, " ");
  }

  function plural(n, one, many) {
    return n + " " + (n === 1 ? one : many);
  }

  function initHome() {
    var input = document.querySelector(".search input");
    var chips = document.querySelectorAll(".chip");
    var tagChips = document.querySelectorAll(".tag-chip");
    var toggle = document.querySelector(".filter-toggle");
    var badge = toggle.querySelector(".badge");
    var panel = document.getElementById("tag-panel");
    var chapters = document.querySelectorAll(".chapter");
    var count = document.querySelector(".results-bar .count");
    var clearButtons = document.querySelectorAll(".clear");
    var empty = document.querySelector(".empty");
    var cards = Array.from(document.querySelectorAll(".recipe-card")).map(function (el) {
      return {
        el: el,
        category: el.dataset.category,
        tags: el.dataset.tags ? el.dataset.tags.split("|") : [],
        search: el.dataset.search,
        title: el.dataset.title || "",
        ingredients: el.dataset.ingredients ? el.dataset.ingredients.split("|") : [],
        match: el.querySelector(".card-match"),
      };
    });
    var category = "";
    var tags = new Set();

    function matchesText(card, words) {
      return words.every(function (w) { return card.search.indexOf(w) !== -1; });
    }

    function hasTags(card, extra) {
      return Array.from(tags).every(function (t) { return card.tags.indexOf(t) !== -1; }) &&
        (!extra || card.tags.indexOf(extra) !== -1);
    }

    // "Tips" have no tags, so any tag filter hides them.
    function inCategory(card, value) {
      return value ? card.category === value : card.category !== "consejos" || !tags.size;
    }

    // When a word isn't in the title, show which ingredient it matched.
    function showMatch(card, words) {
      if (!card.match) return;
      var missing = words.filter(function (w) { return card.title.indexOf(w) === -1; });
      var line = missing.length && card.ingredients.find(function (i) {
        var text = normalize(i);
        return missing.some(function (w) { return text.indexOf(w) !== -1; });
      });
      card.match.hidden = !line;
      card.match.textContent = line ? "Lleva: " + line : "";
    }

    function apply() {
      var words = normalize(input.value).split(/\s+/).filter(Boolean);
      var recipes = 0;
      var tips = 0;
      cards.forEach(function (card) {
        var show = inCategory(card, category) && hasTags(card) && matchesText(card, words);
        card.el.hidden = !show;
        if (show && card.category === "consejos") tips++; else if (show) recipes++;
        if (show) showMatch(card, words);
      });
      chapters.forEach(function (chapter) {
        chapter.hidden = !chapter.querySelector(".recipe-card:not([hidden])");
      });

      // Each chip's number is what you'd get by picking it, given the other filters.
      chips.forEach(function (chip) {
        var value = chip.dataset.filter;
        var n = cards.filter(function (c) {
          return (value ? c.category === value : c.category !== "consejos") && hasTags(c) && matchesText(c, words);
        }).length;
        chip.querySelector("span").textContent = n;
        chip.classList.toggle("zero", n === 0 && chip.getAttribute("aria-pressed") !== "true");
      });
      tagChips.forEach(function (chip) {
        var tag = chip.dataset.tag;
        var on = tags.has(tag);
        var n = cards.filter(function (c) {
          return inCategory(c, category) && c.category !== "consejos" && hasTags(c, tag) && matchesText(c, words);
        }).length;
        chip.querySelector("span").textContent = n;
        chip.disabled = n === 0 && !on;
      });

      var filtered = Boolean(category || tags.size || words.length);
      var parts = [];
      if (recipes || !tips) parts.push(plural(recipes, "receta", "recetas"));
      if (tips) parts.push(plural(tips, "consejo", "consejos"));
      count.textContent = parts.join(" y ");
      empty.hidden = recipes + tips > 0;
      clearButtons.forEach(function (b) { b.hidden = b.parentNode !== empty && !filtered; });
      badge.hidden = !tags.size;
      badge.textContent = tags.size;
      save(words.length ? input.value.trim() : "");
    }

    // Filters live in the URL (?c=…&t=…&q=…) so coming back from a recipe keeps them.
    function save(query) {
      var params = new URLSearchParams();
      if (category) params.set("c", category);
      if (tags.size) params.set("t", Array.from(tags).join(","));
      if (query) params.set("q", query);
      var search = params.toString();
      history.replaceState(null, "", location.pathname + (search ? "?" + search : ""));
    }

    function setCategory(value) {
      category = value;
      chips.forEach(function (chip) {
        chip.setAttribute("aria-pressed", String(chip.dataset.filter === value));
      });
    }

    function setTag(tag, on) {
      if (on) tags.add(tag); else tags.delete(tag);
      tagChips.forEach(function (chip) {
        if (chip.dataset.tag === tag) chip.setAttribute("aria-pressed", String(on));
      });
    }

    // The panel sits in the sticky bar, so fold it away once you scroll on to read the results.
    var openedAt = 0;
    function openPanel(open) {
      panel.hidden = !open;
      toggle.setAttribute("aria-expanded", String(open));
      openedAt = window.scrollY;
    }
    window.addEventListener("scroll", function () {
      if (!panel.hidden && Math.abs(window.scrollY - openedAt) > 300) openPanel(false);
    }, { passive: true });

    chips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        setCategory(chip.dataset.filter);
        apply();
        chip.scrollIntoView({ block: "nearest", inline: "nearest" });
      });
    });
    tagChips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        setTag(chip.dataset.tag, !tags.has(chip.dataset.tag));
        apply();
      });
    });
    toggle.addEventListener("click", function () { openPanel(panel.hidden); });
    clearButtons.forEach(function (button) {
      button.addEventListener("click", function () {
        input.value = "";
        setCategory("");
        Array.from(tags).forEach(function (t) { setTag(t, false); });
        apply();
      });
    });
    input.addEventListener("input", apply);
    document.addEventListener("keydown", function (e) {
      var typing = /INPUT|TEXTAREA/.test(document.activeElement.tagName);
      if (e.key === "/" && !typing) { e.preventDefault(); input.focus(); }
    });

    var params = new URLSearchParams(location.search);
    // Older links used "#postres-y-pasteles".
    var initial = params.get("c") || decodeURIComponent(location.hash.slice(1));
    if (initial && document.querySelector('.chip[data-filter="' + initial + '"]')) setCategory(initial);
    (params.get("t") || "").split(",").forEach(function (t) {
      if (t && document.querySelector('.tag-chip[data-tag="' + t + '"]')) setTag(t, true);
    });
    if (tags.size) openPanel(true);
    input.value = params.get("q") || "";
    apply();
  }

  function initRecipe(main) {
    var key = "recetario:" + main.dataset.recipe;
    var boxes = main.querySelectorAll(".checklist input");
    var steps = main.querySelectorAll(".step");
    var reset = main.querySelector(".reset");

    function load() {
      try { return JSON.parse(localStorage.getItem(key)) || {}; } catch (e) { return {}; }
    }

    function save() {
      var state = { i: [], s: [] };
      boxes.forEach(function (b, n) { if (b.checked) state.i.push(n); });
      steps.forEach(function (s, n) { if (s.classList.contains("done")) state.s.push(n); });
      reset.hidden = !state.i.length && !state.s.length;
      try {
        if (reset.hidden) localStorage.removeItem(key); else localStorage.setItem(key, JSON.stringify(state));
      } catch (e) { /* storage unavailable: checks just won't persist */ }
    }

    var state = load();
    (state.i || []).forEach(function (n) { if (boxes[n]) boxes[n].checked = true; });
    (state.s || []).forEach(function (n) { if (steps[n]) steps[n].classList.add("done"); });
    reset.hidden = !(state.i || []).length && !(state.s || []).length;

    boxes.forEach(function (b) { b.addEventListener("change", save); });
    steps.forEach(function (step) {
      function toggle() { step.classList.toggle("done"); save(); }
      step.setAttribute("role", "checkbox");
      step.setAttribute("aria-checked", String(step.classList.contains("done")));
      step.addEventListener("click", function () { toggle(); step.setAttribute("aria-checked", String(step.classList.contains("done"))); });
      step.addEventListener("keydown", function (e) {
        if (e.key === " " || e.key === "Enter") { e.preventDefault(); step.click(); }
      });
    });
    reset.addEventListener("click", function () {
      boxes.forEach(function (b) { b.checked = false; });
      steps.forEach(function (s) { s.classList.remove("done"); s.setAttribute("aria-checked", "false"); });
      save();
    });

    initWakeLock(main.querySelector(".wake"));
  }

  function initWakeLock(button) {
    if (!button || !("wakeLock" in navigator)) return;
    var lock = null;
    var wanted = false;
    button.hidden = false;

    function update() { button.setAttribute("aria-pressed", String(Boolean(lock))); }

    function acquire() {
      navigator.wakeLock.request("screen").then(function (l) {
        lock = l;
        lock.addEventListener("release", function () { lock = null; update(); });
        update();
      }).catch(function () { wanted = false; update(); });
    }

    button.addEventListener("click", function () {
      wanted = !lock;
      if (lock) lock.release(); else acquire();
    });
    // The browser drops the lock when the tab is hidden; take it back on return.
    document.addEventListener("visibilitychange", function () {
      if (wanted && !lock && document.visibilityState === "visible") acquire();
    });
  }

  var lockOut = document.querySelector(".lock-out");
  if (lockOut) {
    lockOut.addEventListener("click", function () {
      try {
        Object.keys(localStorage).forEach(function (k) {
          if (k.indexOf("recetario:key:") === 0) localStorage.removeItem(k);
        });
      } catch (e) { /* nothing stored */ }
      location.reload();
    });
  }

  if (document.body.classList.contains("home")) initHome();
  var recipe = document.querySelector("main.recipe");
  if (recipe) initRecipe(recipe);
})();
