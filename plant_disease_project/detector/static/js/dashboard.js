// 🌿 dashboard.js

document.addEventListener("DOMContentLoaded", function () {
  console.log("✅ JS loaded");
  console.log("Disease Data:", diseaseData);
  console.log("Confidence Data:", confidenceData);

  // ==============================
  // 🌱 DISEASE DISTRIBUTION (Pie)
  // ==============================
  const diseaseCtx = document.getElementById("diseaseChart");
  if (diseaseCtx && typeof diseaseData !== "undefined" && diseaseData.length > 0) {
    const labels = diseaseData.map(item => item.predicted_label);
    const dataValues = diseaseData.map(item => item.count);

    new Chart(diseaseCtx, {
      type: "pie",
      data: {
        labels: labels,
        datasets: [
          {
            label: "Disease Distribution",
            data: dataValues,
            backgroundColor: [
              "#16a085",
              "#27ae60",
              "#2980b9",
              "#8e44ad",
              "#f39c12",
              "#d35400",
              "#c0392b",
              "#7f8c8d",
            ],
            borderWidth: 1,
            hoverOffset: 12
          }
        ]
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            position: "bottom",
            labels: {
              color: "#2f3640",
              font: {
                size: 14
              }
            }
          },
          title: {
            display: false
          }
        }
      }
    });
  } else {
    console.warn("No disease data available for chart.");
  }

  // ====================================
  // 🌿 CONFIDENCE DISTRIBUTION (Line)
  // ====================================
  const confidenceCtx = document.getElementById("confidenceChart");
  if (confidenceCtx && typeof confidenceData !== "undefined" && confidenceData.length > 0) {
    const labels = confidenceData.map(item => item.range);
    const values = confidenceData.map(item => item.count);

    new Chart(confidenceCtx, {
      type: "line",
      data: {
        labels: labels,
        datasets: [
          {
            label: "Confidence Distribution",
            data: values,
            fill: true,
            borderColor: "#2ecc71",
            backgroundColor: "rgba(46, 204, 113, 0.2)",
            pointBackgroundColor: "#27ae60",
            pointBorderWidth: 2,
            tension: 0.4,
          }
        ]
      },
      options: {
        responsive: true,
        scales: {
          x: {
            title: {
              display: true,
              text: "Confidence Range",
              color: "#2c3e50",
              font: { size: 14 }
            },
            ticks: { color: "#34495e" }
          },
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: "Number of Predictions",
              color: "#2c3e50",
              font: { size: 14 }
            },
            ticks: { color: "#34495e" }
          }
        },
        plugins: {
          legend: {
            position: "bottom",
            labels: {
              color: "#2f3640",
              font: { size: 14 }
            }
          }
        }
      }
    });
  } else {
    console.warn("No confidence data available for chart.");
  }
});
