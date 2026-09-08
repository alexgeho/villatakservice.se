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
