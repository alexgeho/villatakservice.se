(function () {
  const body = document.body;
  const menuToggle = document.querySelector(".menu-toggle");
  const nav = document.querySelector(".site-nav");

  const closeMenu = function () {
    if (!menuToggle || !nav) return;
    nav.classList.remove("is-open");
    menuToggle.setAttribute("aria-expanded", "false");
    body.classList.remove("menu-open");
  };

  if (menuToggle && nav) {
    menuToggle.addEventListener("click", function () {
      const isOpen = nav.classList.toggle("is-open");
      menuToggle.setAttribute("aria-expanded", String(isOpen));
      body.classList.toggle("menu-open", isOpen);
    });

    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", closeMenu);
    });

    document.addEventListener("click", function (event) {
      if (
        nav.classList.contains("is-open") &&
        !nav.contains(event.target) &&
        !menuToggle.contains(event.target)
      ) {
        closeMenu();
      }
    });

    window.addEventListener("resize", function () {
      if (window.innerWidth > 760) {
        closeMenu();
      }
    });
  }

  const currentPath = (window.location.pathname.split("/").pop() || "index.html").toLowerCase();
  document.querySelectorAll("[data-nav]").forEach(function (link) {
    const href = (link.getAttribute("href") || "").toLowerCase();
    if (!href) return;
    const target = href.split("#")[0];
    const isArticleTemplate = currentPath === "artikel.html" && target === "artiklar.html";
    const isActive =
      target === currentPath || (target === "index.html" && currentPath === "") || isArticleTemplate;
    if (isActive) {
      link.classList.add("active");
      link.setAttribute("aria-current", "page");
    }
  });

  document.querySelectorAll("[data-accordion]").forEach(function (accordion) {
    const items = Array.from(accordion.querySelectorAll(".faq-item"));
    items.forEach(function (item) {
      const button = item.querySelector(".faq-question");
      const answer = item.querySelector(".faq-answer");
      const sign = item.querySelector("[data-sign]");
      if (!button || !answer || !sign) return;

      button.addEventListener("click", function () {
        const isOpen = button.getAttribute("aria-expanded") === "true";

        items.forEach(function (otherItem) {
          const otherButton = otherItem.querySelector(".faq-question");
          const otherAnswer = otherItem.querySelector(".faq-answer");
          const otherSign = otherItem.querySelector("[data-sign]");
          if (!otherButton || !otherAnswer || !otherSign) return;
          otherButton.setAttribute("aria-expanded", "false");
          otherAnswer.hidden = true;
          otherSign.textContent = "+";
        });

        if (!isOpen) {
          button.setAttribute("aria-expanded", "true");
          answer.hidden = false;
          sign.textContent = "-";
        }
      });
    });
  });

  const yearNodes = document.querySelectorAll("[data-year]");
  yearNodes.forEach(function (node) {
    node.textContent = String(new Date().getFullYear());
  });
})();

/* =====================================================================
   Consent Mode v2 + GA4 + Meta Pixel  (samtyckesstyrd spårning)
   ---------------------------------------------------------------------
   All spårning är avstängd (denied) tills besökaren aktivt accepterar.
   [OWNER] Fyll i era ID:n nedan – tomma värden = ingen spårning laddas.
   ===================================================================== */
(function () {
  // [OWNER] GA4 Measurement ID, t.ex. "G-XXXXXXXXXX". Tomt = GA4 laddas ej.
  var GA4_ID = "";
  // [OWNER] Meta (Facebook) Pixel ID, t.ex. "123456789012345". Tomt = pixel laddas ej.
  var META_PIXEL_ID = "";
  var STORAGE_KEY = "vts_consent"; // "granted" | "denied"

  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = window.gtag || gtag;

  // Consent Mode v2 – DEFAULT DENIED (måste sättas före all laddning)
  gtag("consent", "default", {
    ad_storage: "denied",
    ad_user_data: "denied",
    ad_personalization: "denied",
    analytics_storage: "denied",
    functionality_storage: "granted",
    security_storage: "granted",
    wait_for_update: 500
  });

  var gaLoaded = false, metaLoaded = false;

  function currentFile() {
    return (window.location.pathname.split("/").pop() || "").toLowerCase();
  }

  function fireLeadConversion() {
    if (!GA4_ID) return;
    if (currentFile() === "tack.html") {
      gtag("event", "generate_lead", {
        currency: "SEK",
        value: 0,
        event_category: "contact",
        event_label: "kontaktformular"
      });
    }
  }

  function loadGA4() {
    if (gaLoaded || !GA4_ID) return;
    gaLoaded = true;
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(GA4_ID);
    document.head.appendChild(s);
    gtag("js", new Date());
    gtag("config", GA4_ID, { anonymize_ip: true });
    fireLeadConversion();
  }

  function loadMetaPixel() {
    if (metaLoaded || !META_PIXEL_ID) return;
    metaLoaded = true;
    /* Standard Meta Pixel bootstrap – laddas endast efter samtycke */
    !function (f, b, e, v, n, t, s) {
      if (f.fbq) return; n = f.fbq = function () {
        n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments);
      };
      if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = "2.0";
      n.queue = []; t = b.createElement(e); t.async = !0; t.src = v;
      s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s);
    }(window, document, "script", "https://connect.facebook.net/en_US/fbevents.js");
    window.fbq("init", META_PIXEL_ID);
    window.fbq("track", "PageView");
    if (currentFile() === "tack.html") { window.fbq("track", "Lead"); }
  }

  function grantConsent() {
    gtag("consent", "update", {
      ad_storage: "granted",
      ad_user_data: "granted",
      ad_personalization: "granted",
      analytics_storage: "granted"
    });
    loadGA4();
    loadMetaPixel();
  }

  function persist(v) { try { window.localStorage.setItem(STORAGE_KEY, v); } catch (e) {} }
  function read() { try { return window.localStorage.getItem(STORAGE_KEY); } catch (e) { return null; } }

  function showBanner() {
    if (document.getElementById("cookie-banner")) return;
    var b = document.createElement("div");
    b.id = "cookie-banner";
    b.className = "cookie-banner";
    b.setAttribute("role", "dialog");
    b.setAttribute("aria-live", "polite");
    b.setAttribute("aria-label", "Samtycke till cookies");
    b.innerHTML =
      '<div class="cookie-banner__inner">' +
      '<p class="cookie-banner__text">Vi använder cookies för att mäta och förbättra webbplatsen. ' +
      'Du väljer själv – inget laddas innan du samtycker. Läs mer i vår ' +
      '<a href="integritetspolicy.html">integritetspolicy</a>.</p>' +
      '<div class="cookie-banner__actions">' +
      '<button type="button" class="btn btn-secondary" data-cc="deny">Endast nödvändiga</button>' +
      '<button type="button" class="btn btn-primary" data-cc="accept">Acceptera alla</button>' +
      '</div>' +
      '</div>';
    (document.body || document.documentElement).appendChild(b);
    b.querySelector('[data-cc="accept"]').addEventListener("click", function () {
      persist("granted"); grantConsent(); b.parentNode && b.parentNode.removeChild(b);
    });
    b.querySelector('[data-cc="deny"]').addEventListener("click", function () {
      persist("denied"); b.parentNode && b.parentNode.removeChild(b);
    });
  }

  var stored = read();
  if (stored === "granted") {
    grantConsent();
  } else if (stored === "denied") {
    /* behåll denied – ingen spårning */
  } else {
    showBanner();
  }
})();

/* =====================================================================
   Kalkylator: grov uppskattning av takbyte  (lead-magnet)
   ---------------------------------------------------------------------
   [OWNER] RATES nedan är branschtypiska spann (kr/m² inkl. material,
   före ROT) – verifiera/justera mot era egna kalkyler. Verktyget ger
   en icke-bindande uppskattning, aldrig en offert.
   ===================================================================== */
(function () {
  var form = document.getElementById("kalkyl-form");
  if (!form) return;

  var RATES = {           // kr per m², totalt inkl. material, före ROT
    betong: [1400, 2000],
    tegel:  [1800, 2600],
    plat:   [1600, 2400]
  };
  var COMPLEX = { lag: 0.97, normal: 1.0, brant: 1.18 };
  var MAT_LABEL = { betong: "Betongpannor", tegel: "Tegelpannor", plat: "Plåt" };
  var LABOUR_SHARE = 0.35;   // ungefärlig arbetskostnadsandel
  var ROT_PCT = 0.30;        // ROT 2026: 30 % av arbetskostnaden
  var ROT_CAP = 50000;       // kr/person/år (1 ägare)

  var result = document.getElementById("kalkyl-result");
  var elLow = document.getElementById("kalkyl-low");
  var elHigh = document.getElementById("kalkyl-high");
  var elRotLow = document.getElementById("kalkyl-rot-low");
  var elRotHigh = document.getElementById("kalkyl-rot-high");
  var elCta = document.getElementById("kalkyl-cta");

  function grp(n) {
    return String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, " ");
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var area = parseFloat(form.elements["area"].value);
    var mat = form.elements["material"].value;
    var comp = form.elements["lutning"].value;
    if (!area || area <= 0 || !RATES[mat] || !COMPLEX[comp]) {
      form.reportValidity && form.reportValidity();
      return;
    }
    var m = COMPLEX[comp];
    var low = RATES[mat][0] * area * m;
    var high = RATES[mat][1] * area * m;
    var rotLow = Math.min(low * LABOUR_SHARE * ROT_PCT, ROT_CAP);
    var rotHigh = Math.min(high * LABOUR_SHARE * ROT_PCT, ROT_CAP);

    elLow.textContent = grp(low);
    elHigh.textContent = grp(high);
    elRotLow.textContent = grp(low - rotLow);
    elRotHigh.textContent = grp(high - rotHigh);
    result.hidden = false;

    var msg = "Hej! Jag har använt takbyte-kalkylatorn och vill ha en kostnadsfri offert.\n\n" +
      "Takarea: ca " + area + " m²\n" +
      "Material: " + (MAT_LABEL[mat] || mat) + "\n" +
      "Taklutning/komplexitet: " + form.elements["lutning"].options[form.elements["lutning"].selectedIndex].text + "\n" +
      "Uppskattat spann (kalkylator): " + grp(low) + "–" + grp(high) + " kr, efter ROT ca " +
      grp(low - rotLow) + "–" + grp(high - rotHigh) + " kr.";
    if (elCta) {
      elCta.href = "kontakt.html?tjanst=Takbyte&meddelande=" + encodeURIComponent(msg) + "#form";
    }
  });
})();

/* =====================================================================
   Prefyll kontaktformuläret från query (?tjanst=&meddelande=)
   ===================================================================== */
(function () {
  var form = document.querySelector('form[action="sendmail.php"]');
  if (!form) return;
  var p = new URLSearchParams(window.location.search);
  var tjanst = p.get("tjanst");
  var meddelande = p.get("meddelande");
  if (tjanst) {
    var sel = form.querySelector("#tjanst");
    if (sel) {
      Array.prototype.forEach.call(sel.options, function (o) {
        if (o.value === tjanst || o.text === tjanst) { sel.value = o.value || o.text; }
      });
    }
  }
  if (meddelande) {
    var ta = form.querySelector("#meddelande");
    if (ta && !ta.value) { ta.value = meddelande; }
  }
})();

/* =====================================================================
   Klientbaserad sök (sok.html) – matchar mot window.SEARCH_INDEX
   ===================================================================== */
(function () {
  var form = document.getElementById("sok-form");
  var input = document.getElementById("sok-input");
  var out = document.getElementById("sok-results");
  if (!form || !input || !out || !window.SEARCH_INDEX) return;

  function norm(s) { return (s || "").toLowerCase(); }

  function run(q) {
    q = norm(q).trim();
    if (!q) { out.innerHTML = ""; return; }
    var terms = q.split(/\s+/);
    var hits = window.SEARCH_INDEX.map(function (it) {
      var hay = norm(it.t + " " + it.d);
      var score = 0;
      terms.forEach(function (t) { if (hay.indexOf(t) !== -1) score++; });
      if (norm(it.t).indexOf(q) !== -1) score += 2;
      return { it: it, score: score };
    }).filter(function (r) { return r.score > 0; })
      .sort(function (a, b) { return b.score - a.score; });

    out.innerHTML = "";
    if (!hits.length) {
      var none = document.createElement("p");
      none.textContent = "Inga träffar för “" + q + "”. Prova ett annat sökord.";
      out.appendChild(none);
      return;
    }
    var frag = document.createDocumentFragment();
    hits.slice(0, 20).forEach(function (r) {
      var art = document.createElement("article");
      art.className = "service-snippet";
      var h = document.createElement("h3");
      var link = document.createElement("a");
      link.className = "text-link";
      link.href = r.it.u;
      link.textContent = r.it.t;
      h.appendChild(link);
      var p = document.createElement("p");
      p.textContent = r.it.d;
      art.appendChild(h);
      art.appendChild(p);
      frag.appendChild(art);
    });
    out.appendChild(frag);
  }

  var q0 = new URLSearchParams(window.location.search).get("q");
  if (q0) { input.value = q0; run(q0); }
  form.addEventListener("submit", function (e) { e.preventDefault(); run(input.value); });
  input.addEventListener("input", function () { run(input.value); });
})();
