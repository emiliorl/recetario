// Decrypts the page in the browser. The key is derived from the family password with the
// same PBKDF2 settings used at build time (pipeline/crypto.py), and can be remembered per device.
(function () {
  "use strict";

  var payloadEl = document.getElementById("payload");
  var salt = payloadEl.dataset.salt;
  var iterations = Number(payloadEl.dataset.iterations);
  var storageKey = "recetario:key:" + salt;
  var appSrc = document.currentScript.dataset.app;
  var enc = new TextEncoder();

  function b64decode(text) {
    var bin = atob(text.trim());
    var bytes = new Uint8Array(bin.length);
    for (var i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
    return bytes;
  }

  function b64encode(buffer) {
    var bytes = new Uint8Array(buffer);
    var bin = "";
    for (var i = 0; i < bytes.length; i++) bin += String.fromCharCode(bytes[i]);
    return btoa(bin);
  }

  function importAesKey(raw) {
    return crypto.subtle.importKey("raw", raw, "AES-GCM", false, ["decrypt"]);
  }

  function deriveRawKey(password) {
    return crypto.subtle
      .importKey("raw", enc.encode(password), "PBKDF2", false, ["deriveBits"])
      .then(function (base) {
        return crypto.subtle.deriveBits(
          { name: "PBKDF2", hash: "SHA-256", salt: enc.encode(salt), iterations: iterations },
          base,
          256
        );
      });
  }

  function decrypt(rawKey) {
    var blob = b64decode(payloadEl.textContent);
    return importAesKey(rawKey)
      .then(function (key) {
        return crypto.subtle.decrypt({ name: "AES-GCM", iv: blob.slice(0, 12) }, key, blob.slice(12));
      })
      .then(function (plain) {
        return JSON.parse(new TextDecoder().decode(plain));
      });
  }

  function show(page) {
    document.title = page.title;
    document.body.className = page.cls;
    document.body.innerHTML = page.body;
    var app = document.createElement("script");
    app.src = appSrc;
    document.body.appendChild(app);
    if (location.hash) {
      var target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
      if (target) target.scrollIntoView();
    }
  }

  function storage(action, value) {
    try {
      if (action === "get") return localStorage.getItem(storageKey);
      if (action === "set") localStorage.setItem(storageKey, value);
      if (action === "remove") localStorage.removeItem(storageKey);
    } catch (e) { /* private mode: just ask each time */ }
    return null;
  }

  function askPassword() {
    document.body.classList.add("ask");
    var form = document.querySelector(".lock-card");
    var input = form.querySelector('input[type="password"]');
    var remember = form.querySelector('.remember input');
    var button = form.querySelector("button");
    var error = form.querySelector(".lock-error");
    input.focus();

    form.addEventListener("submit", function (event) {
      event.preventDefault();
      button.disabled = true;
      button.textContent = "Abriendo…";
      error.hidden = true;
      var rawKey;
      deriveRawKey(input.value)
        .then(function (raw) { rawKey = raw; return decrypt(raw); })
        .then(function (page) {
          if (remember.checked) storage("set", b64encode(rawKey));
          show(page);
        })
        .catch(function () {
          error.hidden = false;
          button.disabled = false;
          button.textContent = "Entrar";
          input.select();
        });
    });
  }

  if (!window.crypto || !crypto.subtle) {
    document.body.classList.add("ask");
    document.querySelector(".lock-text").textContent =
      "Este navegador no puede abrir el recetario. Prueba con uno actualizado (y con https).";
    return;
  }

  var saved = storage("get");
  if (saved) {
    decrypt(b64decode(saved)).then(show).catch(function () {
      storage("remove"); // password changed since this device last visited
      askPassword();
    });
  } else {
    askPassword();
  }
})();
