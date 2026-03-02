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
