// ===============================
// 🌿 HISTORY PAGE INTERACTIVITY
// ===============================

document.addEventListener("DOMContentLoaded", () => {
    console.log("📜 History page loaded!");

    const cards = document.querySelectorAll(".history-card");

    // Add animation when scrolling into view
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.2 });

    cards.forEach(card => {
        observer.observe(card);
    });
});
