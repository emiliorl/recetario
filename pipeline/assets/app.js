// Home: search and filters. Recipe: saved checkboxes, tappable steps, keep-screen-on.
(function () {
  "use strict";

  function normalize(text) {
    return text.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9 ]/g, " ");
  }

  function initHome() {
    var input = document.querySelector(".search input");
    var chips = document.querySelectorAll(".chip");
    var tagChips = document.querySelectorAll(".tag-chip");
    var chapters = document.querySelectorAll(".chapter");
    var empty = document.querySelector(".empty");
    var category = "";
    var tags = new Set();

    function apply() {
      var words = normalize(input.value).split(/\s+/).filter(Boolean);
      var visibleTotal = 0;
      chapters.forEach(function (chapter) {
        var cards = chapter.querySelectorAll(".recipe-card");
        if (!cards.length) {
          // Tips section: show only when nothing is filtered.
          chapter.hidden = Boolean(category || tags.size || words.length);
          return;
        }
        var visible = 0;
        cards.forEach(function (card) {
          var cardTags = card.dataset.tags ? card.dataset.tags.split("|") : [];
          var show =
            (!category || card.dataset.category === category) &&
            Array.from(tags).every(function (t) { return cardTags.indexOf(t) !== -1; }) &&
            words.every(function (w) { return card.dataset.search.indexOf(w) !== -1; });
          card.hidden = !show;
          if (show) visible++;
        });
        chapter.hidden = visible === 0;
        visibleTotal += visible;
      });
      empty.hidden = visibleTotal > 0;
    }

    function setCategory(value) {
      category = value;
      chips.forEach(function (chip) {
        chip.setAttribute("aria-pressed", String(chip.dataset.filter === value));
      });
      apply();
    }

    chips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        setCategory(chip.dataset.filter);
        history.replaceState(null, "", category ? "#" + category : location.pathname);
      });
    });
    tagChips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        var tag = chip.dataset.tag;
        if (tags.has(tag)) tags.delete(tag); else tags.add(tag);
        chip.setAttribute("aria-pressed", String(tags.has(tag)));
        apply();
      });
    });
    input.addEventListener("input", apply);

    // Links like "../../#postres-y-pasteles" from a recipe page open that chapter filtered.
    var hash = decodeURIComponent(location.hash.slice(1));
    if (hash && document.querySelector('.chip[data-filter="' + hash + '"]')) setCategory(hash);
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
