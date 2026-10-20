document.addEventListener("DOMContentLoaded", () => {
  const navbar = document.querySelector(".kora-navbar");
  const backToTop = document.getElementById("backToTop");
  const year = document.getElementById("year");

  year.textContent = new Date().getFullYear();

  window.addEventListener("scroll", () => {
    navbar.classList.toggle("scrolled", window.scrollY > 40);
    backToTop.classList.toggle("show", window.scrollY > 500);
  });

  backToTop.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));

  // Close mobile navigation after clicking a link.
  document.querySelectorAll("#mainNav .nav-link, #mainNav .dropdown-item").forEach(link => {
    link.addEventListener("click", () => {
      const nav = document.getElementById("mainNav");
      if (nav.classList.contains("show")) {
        bootstrap.Collapse.getOrCreateInstance(nav).hide();
      }
    });
  });

  // Set minimum booking date to today.
  const dateInput = document.querySelector('input[type="date"]');
  if (dateInput) {
    const today = new Date();
    const localDate = new Date(today.getTime() - today.getTimezoneOffset() * 60000)
      .toISOString().split("T")[0];
    dateInput.min = localDate;
  }

  // Demo booking form — replace this with your backend/API later.
  const bookingForm = document.getElementById("bookingForm");
  const bookingMessage = document.getElementById("bookingMessage");

  bookingForm.addEventListener("submit", (event) => {
    event.preventDefault();
    bookingMessage.classList.remove("d-none");
    bookingForm.reset();
    setTimeout(() => bookingMessage.classList.add("d-none"), 7000);
  });

  // Demo newsletter form.
  const newsletterForm = document.getElementById("newsletterForm");
  newsletterForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const button = newsletterForm.querySelector("button");
    const original = button.textContent;
    button.textContent = "Subscribed ✓";
    newsletterForm.reset();
    setTimeout(() => button.textContent = original, 3000);
  });

  // Smooth scrolling for same-page anchors.
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function (event) {
      const target = document.querySelector(this.getAttribute("href"));
      if (!target) return;
      event.preventDefault();
      target.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });
});
