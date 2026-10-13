/* SA Asphalt — site behaviour */
(function () {
  "use strict";
  var WHATSAPP = "27836030953";

  // Mobile navigation
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) { nav.classList.remove("open"); toggle.setAttribute("aria-expanded", "false"); }
    });
  }

  // Footer year
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  // Lightbox: any <img class="zoomable"> or image inside a .gallery / .gallery-3 figure.
  // Images that share a [data-lightbox-group] ancestor can be stepped through with the arrows.
  var box, boxImg, boxCap, items = [], index = 0;
  function buildBox() {
    box = document.createElement("div");
    box.className = "lightbox";
    box.setAttribute("role", "dialog");
    box.setAttribute("aria-modal", "true");
    box.setAttribute("aria-label", "Photo viewer");
    box.innerHTML = '<figure style="margin:0"><img alt=""><figcaption></figcaption></figure>' +
      '<button class="lb-close" aria-label="Close">&times;</button>' +
      '<button class="lb-prev" aria-label="Previous photo">&#8249;</button>' +
      '<button class="lb-next" aria-label="Next photo">&#8250;</button>';
    document.body.appendChild(box);
    boxImg = box.querySelector("img");
    boxCap = box.querySelector("figcaption");
    box.querySelector(".lb-close").addEventListener("click", close);
    box.querySelector(".lb-prev").addEventListener("click", function () { show(index - 1); });
    box.querySelector(".lb-next").addEventListener("click", function () { show(index + 1); });
    box.addEventListener("click", function (e) { if (e.target === box) close(); });
    document.addEventListener("keydown", function (e) {
      if (!box.classList.contains("open")) return;
      if (e.key === "Escape") close();
      if (e.key === "ArrowLeft") show(index - 1);
      if (e.key === "ArrowRight") show(index + 1);
    });
  }
  function show(i) {
    index = (i + items.length) % items.length;
    var img = items[index];
    boxImg.src = img.dataset.full || img.currentSrc || img.src;
    boxImg.alt = img.alt;
    var cap = img.dataset.caption || (img.closest("figure") && img.closest("figure").querySelector("figcaption")) || null;
    boxCap.textContent = typeof cap === "string" ? cap : (cap ? cap.textContent : img.alt);
    var multi = items.length > 1;
    box.querySelector(".lb-prev").style.display = multi ? "" : "none";
    box.querySelector(".lb-next").style.display = multi ? "" : "none";
  }
  function open(img) {
    if (!box) buildBox();
    var group = img.closest("[data-lightbox-group]");
    items = group ? Array.prototype.filter.call(group.querySelectorAll("img"), function (el) { return !el.closest("[hidden]"); }) : [img];
    box.classList.add("open");
    show(items.indexOf(img));
    box.querySelector(".lb-close").focus();
  }
  function close() { box.classList.remove("open"); }
  document.addEventListener("click", function (e) {
    var img = e.target.closest("img.zoomable, .gallery img, .gallery-3 img, .comm-card button");
    if (!img) return;
    if (img.tagName === "BUTTON") img = img.querySelector("img");
    e.preventDefault();
    open(img);
  });

  // Community filters
  var filters = document.querySelectorAll(".filter");
  if (filters.length) {
    var cards = document.querySelectorAll(".comm-card");
    var count = document.querySelector(".filter-count");
    filters.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var cat = btn.dataset.filter;
        filters.forEach(function (b) { b.setAttribute("aria-pressed", b === btn ? "true" : "false"); });
        var shown = 0;
        cards.forEach(function (card) {
          var match = cat === "all" || card.dataset.cat === cat;
          card.hidden = !match;
          if (match) shown++;
        });
        if (count) count.textContent = cat === "all" ? "Showing all " + shown + " photographs" : "Showing " + shown + " photograph" + (shown === 1 ? "" : "s");
      });
    });
  }

  // Quote form: builds a WhatsApp message (the site is static and stores nothing)
  var form = document.getElementById("quote-form");
  if (form) {
    var params = new URLSearchParams(window.location.search);
    var preset = params.get("service");
    if (preset && form.service) {
      Array.prototype.forEach.call(form.service.options, function (o) { if (o.value === preset) form.service.value = preset; });
    }
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var err = form.querySelector(".form-error");
      if (!form.checkValidity()) {
        err.style.display = "block";
        form.reportValidity();
        return;
      }
      err.style.display = "none";
      var f = form.elements;
      var lines = [
        "Hello SA Asphalt, I would like a quote.",
        "",
        "Name: " + f.name.value.trim(),
        "Phone / WhatsApp: " + f.phone.value.trim(),
        "Site location / suburb: " + f.location.value.trim(),
        "Service: " + f.service.value,
        f.size.value.trim() ? "Approx. area / size: " + f.size.value.trim() : "",
        "Preferred timing: " + f.timing.value,
        "",
        "Project details: " + f.details.value.trim(),
        "",
        "I will attach photographs of the area."
      ].filter(function (l, i, a) { return l !== "" || (a[i - 1] !== "" && i > 0); });
      window.open("https://wa.me/" + WHATSAPP + "?text=" + encodeURIComponent(lines.join("\n")), "_blank", "noopener");
    });
  }
})();
