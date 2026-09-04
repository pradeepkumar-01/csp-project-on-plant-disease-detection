// 🌿 Toggles between original and heatmap overlay view
document.addEventListener("DOMContentLoaded", () => {
    const heatmap = document.querySelector(".heatmap-image");
    const toggleBtn = document.getElementById("toggle-heatmap");

    let visible = true;

    toggleBtn.addEventListener("click", () => {
        visible = !visible;
        heatmap.style.opacity = visible ? "0.6" : "0";
        toggleBtn.innerHTML = visible ? " Hide Heatmap" : " Show Heatmap";
    });

    // Subtle fade-in effect
    document.querySelector(".layout-section").style.opacity = 0;
    setTimeout(() => {
        document.querySelector(".layout-section").style.transition = "opacity 1s";
        document.querySelector(".layout-section").style.opacity = 1;
    }, 150);
});
