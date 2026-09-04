// 🌱 Plant and Disease Data for the Home Page
const plantData = {
    "Apple": {
        description: "Apple trees are deciduous plants that thrive in temperate climates. Their leaves are oval-shaped with serrated edges and a rich green color, playing a key role in photosynthesis and fruit development.",
        diseases: {
            "Cedar_apple_rust": "A fungal disease causing orange or yellow spots on leaves. It spreads between apple and cedar trees.",
            "Black_rot": "Characterized by dark brown or black leaf spots and rotting fruit.",
            "Apple_scab": "Causes olive-green to brown scabs on leaves and fruit, leading to deformation.",
            "healthy": "Healthy apple leaves are smooth, bright green, and free of any blemishes."
        }
    },
    "Grape": {
        description: "Grapevines are woody climbers with broad, lobed leaves. They are cultivated for their fruit used in winemaking, juice, and consumption.",
        diseases: {
            "Leaf_blight_(Isariopsis_Leaf_Spot)": "Appears as small dark lesions with yellow halos on leaves, reducing vine vigor.",
            "Black_rot": "Causes black circular spots on leaves and shriveled fruit known as 'mummies'.",
            "Esca_(Black_Measles)": "Produces tiger-stripe discolorations on leaves and black streaks inside wood.",
            "healthy": "Healthy grape leaves are large, green, and free from discoloration or holes."
        }
    },
    "Soybean": {
        description: "Soybean plants are leguminous crops with compound trifoliate leaves. They are an essential source of protein and oil globally.",
        diseases: {
            "healthy": "Healthy soybean leaves are green and glossy with no spots or blight symptoms."
        }
    },
    "Peach": {
        description: "Peach trees are small deciduous plants producing soft, juicy fruits. The leaves are long, narrow, and finely serrated.",
        diseases: {
            "Bacterial_spot": "Manifests as small dark spots on leaves and fruit, leading to leaf drop and blemished fruit.",
            "healthy": "Healthy peach leaves are vibrant green, firm, and free from holes or spots."
        }
    },
    "Tomato": {
        description: "Tomato plants are herbaceous and widely cultivated for their fleshy, red fruits. The leaves are compound and emit a distinct aroma.",
        diseases: {
            "Tomato_Yellow_Leaf_Curl_Virus": "Leads to upward curling of leaves and yellowing, stunting plant growth.",
            "Target_Spot": "Circular dark lesions with concentric rings on older leaves.",
            "Septoria_leaf_spot": "Small gray-centered dark spots primarily affecting lower leaves.",
            "Spider_mites_Two-spotted_spider_mite": "Tiny mites causing yellow speckles and webbing on leaves.",
            "Early_blight": "Dark, target-like spots leading to premature leaf death.",
            "Late_blight": "Rapidly spreading water-soaked lesions turning brown-black.",
            "Bacterial_spot": "Small dark, greasy spots on leaves and fruit reducing yield.",
            "Tomato_mosaic_virus": "Causes mottled, light and dark green leaf patterns with reduced growth.",
            "Leaf_Mold": "Velvety greenish mold on undersides of leaves in humid conditions.",
            "healthy": "Healthy tomato leaves are soft, serrated, and vibrant green."
        }
    },
    "Pepper,_bell": {
        description: "Bell pepper plants have glossy green leaves and produce colorful fruits. They prefer warm climates and well-drained soil.",
        diseases: {
            "Bacterial_spot": "Water-soaked spots on leaves that turn brown and tear easily.",
            "healthy": "Healthy bell pepper leaves are smooth, dark green, and firm."
        }
    },
    "Cherry_(including_sour)": {
        description: "Cherry trees are deciduous with shiny green, finely serrated leaves and beautiful blossoms in spring.",
        diseases: {
            "Powdery_mildew": "White powdery coating on leaf surfaces, reducing photosynthesis.",
            "healthy": "Healthy cherry leaves are vibrant green with smooth surfaces."
        }
    },
    "Strawberry": {
        description: "Strawberry plants are low-growing perennials with trifoliate leaves and red, juicy fruits. Their leaves are slightly hairy and serrated.",
        diseases: {
            "Leaf_scorch": "Small purple spots that merge into brown patches, causing leaf dryness.",
            "healthy": "Healthy strawberry leaves are green and firm with well-defined serrations."
        }
    },
    "Corn_(maize)": {
        description: "Corn is a tall annual grass crop producing ears that contain kernels. The leaves are long, flat, and arranged alternately.",
        diseases: {
            "Common_rust_": "Reddish-brown pustules on both leaf surfaces due to fungal infection.",
            "Northern_Leaf_Blight": "Long grayish lesions that run parallel to leaf veins.",
            "Cercospora_leaf_spot_Gray_leaf_spot": "Gray rectangular lesions causing leaf death in severe cases.",
            "healthy": "Healthy corn leaves are glossy green, long, and free of any rust or spots."
        }
    },
    "Potato": {
        description: "Potato plants have compound leaves and produce underground tubers. They thrive in cool, moist environments.",
        diseases: {
            "Early_blight": "Dark concentric rings on leaves starting from the lower part of the plant.",
            "Late_blight": "Large, irregular water-soaked spots that turn brown and destroy foliage.",
            "healthy": "Healthy potato leaves are uniformly green with no yellowing or dark spots."
        }
    },
    "Blueberry": {
        description: "Blueberry shrubs are perennial with small, oval, smooth-edged leaves. They produce nutrient-rich blue fruits.",
        diseases: {
            "healthy": "Healthy blueberry leaves are small, waxy, and free from any discoloration."
        }
    },
    "Raspberry": {
        description: "Raspberry plants have compound leaves with serrated margins. They produce red or black aggregate fruits.",
        diseases: {
            "healthy": "Healthy raspberry leaves are soft, green, and evenly textured."
        }
    },
    "Squash": {
        description: "Squash plants have large, lobed leaves and sprawling vines. They are widely cultivated for their edible fruit.",
        diseases: {
            "Powdery_mildew": "White, powder-like patches on leaves, reducing sunlight absorption.",
            "healthy": "Healthy squash leaves are large, green, and unblemished."
        }
    },
    "Orange": {
        description: "Orange trees are evergreen with glossy leaves and fragrant blossoms. They are a major citrus crop worldwide.",
        diseases: {
            "Haunglongbing_(Citrus_greening)": "A bacterial disease causing yellow shoots and misshapen, bitter fruit.",
            "healthy": "Healthy orange leaves are dark green and shiny, indicating proper nutrition."
        }
    }
};


// 🌿 Initialize after DOM is loaded
document.addEventListener("DOMContentLoaded", () => {
    const plantListDiv = document.getElementById("plant-list");
    const plantInfoDiv = document.getElementById("plant-info");

    // 🌼 Generate Plant Buttons
    for (let plant in plantData) {
        const btn = document.createElement("button");
        btn.textContent = plant;
        btn.addEventListener("click", () => showPlantInfo(plant, plantData, plantInfoDiv));
        plantListDiv.appendChild(btn);
    }

    // 🌿 Default Welcome Message
    plantInfoDiv.innerHTML = `
        <div class="fade-in">
            <h3>🌱 Welcome to Plant Disease Detector</h3>
            <p>
                Our AI-powered model can detect multiple plant diseases from leaf images across various crops.
                Select a plant from the list above to learn what diseases it can detect and how they affect plant health.
            </p>
            <p><strong>Tip:</strong> Click any plant name to view its description and disease details.</p>
        </div>
    `;
    plantInfoDiv.classList.remove("hidden");
});

// 🌿 Display Selected Plant Info
function showPlantInfo(plantName, plantData, plantInfoDiv) {
    const plant = plantData[plantName];
    if (!plant) return;

    const diseaseHTML = Object.entries(plant.diseases)
        .map(([disease, desc]) => `
            <li><i class="fas fa-virus"></i> <strong>${disease}</strong> — ${desc}</li>
        `).join("");

    plantInfoDiv.innerHTML = `
        <div class="fade-in">
            <h3><i class="fas fa-leaf"></i> ${plantName}</h3>
            <p>${plant.description}</p>
            <h4><i class="fas fa-bug"></i> Categories Detected:</h4>
            <ul>${diseaseHTML}</ul>
        </div>
    `;

    plantInfoDiv.scrollIntoView({ behavior: "smooth" });
}