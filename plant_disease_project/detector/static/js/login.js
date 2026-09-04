// Simple focus effect and small animation for login form
document.addEventListener("DOMContentLoaded", () => {
    const inputs = document.querySelectorAll(".input-group input");
    const form = document.querySelector(".login-form");

    // Add green focus glow
    inputs.forEach(input => {
        input.addEventListener("focus", () => {
            input.style.borderColor = "#43a047";
            input.style.boxShadow = "0 0 5px rgba(67,160,71,0.5)";
        });
        input.addEventListener("blur", () => {
            input.style.borderColor = "#ccc";
            input.style.boxShadow = "none";
        });
    });

    // Smooth form fade-in
    form.style.opacity = 0;
    setTimeout(() => {
        form.style.transition = "opacity 1s ease-in-out";
        form.style.opacity = 1;
    }, 200);
});
