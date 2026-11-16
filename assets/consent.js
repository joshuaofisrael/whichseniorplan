(function () {
  var KEY = "wsp-consent";
  var loader = document.getElementById("ga4-loader");
  var id = loader ? (loader.getAttribute("data-ga4-id") || "") : "";
  var src = loader ? (loader.getAttribute("data-gtag-src") || "") : "";

  function validId(value) {
    return /^G-[A-Za-z0-9]+$/.test(value);
  }

  function loadGa() {
    if (!validId(id) || !src || window.__wspGaLoaded) return;
    window.__wspGaLoaded = true;
    window.gtag("consent", "update", {
      ad_storage: "denied",
      ad_user_data: "denied",
      ad_personalization: "denied",
      analytics_storage: "granted"
    });
    var tag = document.createElement("script");
    tag.async = true;
    tag.src = src + "?id=" + encodeURIComponent(id);
    document.head.appendChild(tag);
    window.gtag("js", new Date());
    window.gtag("config", id);
  }

  function hideBanner() {
    var el = document.getElementById("consent-banner");
    if (el) el.remove();
  }

  function showBanner() {
    if (document.getElementById("consent-banner")) return;
    var bar = document.createElement("div");
    bar.id = "consent-banner";
    bar.className = "consent";
    bar.setAttribute("role", "dialog");
    bar.setAttribute("aria-label", "Cookie settings");
    bar.innerHTML = '<div class="wrap"><p>Cloudflare Web Analytics is on for page counts and does not use cookies. Google Analytics 4 loads only if you accept. Advertising storage stays off.</p><button type="button" class="btn" id="consent-accept">Accept</button><button type="button" class="btn alt" id="consent-decline">Decline</button></div>';
    document.body.appendChild(bar);
    document.getElementById("consent-accept").addEventListener("click", function () { choose("granted"); });
    document.getElementById("consent-decline").addEventListener("click", function () { choose("denied"); });
  }

  function choose(value) {
    try { localStorage.setItem(KEY, value); } catch (err) {}
    hideBanner();
    if (value === "granted") loadGa();
    else if (window.gtag) {
      window.gtag("consent", "update", {
        ad_storage: "denied",
        ad_user_data: "denied",
        ad_personalization: "denied",
        analytics_storage: "denied"
      });
    }
  }

  var saved = "";
  try { saved = localStorage.getItem(KEY) || ""; } catch (err) {}
  if (saved === "granted") loadGa();
  else if (saved !== "denied") showBanner();

  var opener = document.getElementById("cookie-settings");
  if (opener) {
    opener.addEventListener("click", function (event) {
      event.preventDefault();
      showBanner();
    });
  }
})();
