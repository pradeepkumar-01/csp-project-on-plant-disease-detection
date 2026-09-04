// 🌿 Result Page Enhancements
document.addEventListener("DOMContentLoaded", () => {
    const resultBox = document.querySelector(".card");

    // Smooth fade-in animation on load
    resultBox.style.opacity = 0;
    setTimeout(() => {
        resultBox.style.transition = "opacity 1.2s ease-in-out";
        resultBox.style.opacity = 1;
    }, 200);

    // Optional: Add confetti for healthy plants 🌱
    const message = document.querySelector(".healthy");
    if (message) {
        createConfetti();
    }
});

function createConfetti() {
    const confettiCount = 100;
    for (let i = 0; i < confettiCount; i++) {
        const confetti = document.createElement("div");
        confetti.classList.add("confetti");
        confetti.style.left = Math.random() * 100 + "vw";
        confetti.style.animationDuration = 2 + Math.random() * 3 + "s";
        confetti.style.backgroundColor = `hsl(${Math.random() * 360}, 70%, 60%)`;
        document.body.appendChild(confetti);

        setTimeout(() => confetti.remove(), 5000);
    }
}

// 💫 Confetti Styling
const style = document.createElement('style');
style.textContent = `
.confetti {
    position: fixed;
    width: 8px;
    height: 8px;
    top: -10px;
    border-radius: 50%;
    opacity: 0.8;
    animation: fall linear forwards;
    z-index: 9999;
}
@keyframes fall {
    to {
        transform: translateY(100vh);
        opacity: 0;
    }
}`;
document.head.appendChild(style);
