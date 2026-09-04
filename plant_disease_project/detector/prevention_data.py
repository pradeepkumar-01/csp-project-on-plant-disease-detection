# detector/prevention_data.py

PLANT_PREVENTIONS = {
    "Grape": {
        "Leaf_blight_(Isariopsis_Leaf_Spot)": {
            "description": "A fungal disease that causes small brown necrotic spots on grape leaves, which expand and merge to form large blighted patches.",
            "cause": "Caused by the Isariopsis fungus that thrives in humid and wet environments.",
            "prevention": "Prune and dispose of infected leaves, improve air circulation, avoid overhead irrigation, and apply fungicides like copper hydroxide or chlorothalonil."
        },
        "Black_rot": {
            "description": "A severe fungal disease that results in circular leaf spots, black shriveled berries, and stem cankers.",
            "cause": "Caused by the fungus *Guignardia bidwellii*, spreading through rain and wind.",
            "prevention": "Remove mummified berries and infected vines, prune properly, and spray preventive fungicides such as mancozeb or myclobutanil."
        },
        "Esca_(Black_Measles)": {
            "description": "A trunk disease causing tiger-striped leaf patterns and internal wood decay, leading to vine dieback.",
            "cause": "A complex infection caused by *Phaeomoniella chlamydospora* and related fungi.",
            "prevention": "Avoid pruning during wet weather, disinfect pruning tools, and remove infected wood promptly."
        },
        "healthy": {
            "description": "The grapevine is healthy with vigorous growth and no disease symptoms.",
            "cause": "Good cultural practices and balanced fertilization.",
            "prevention": "Continue pruning, disease monitoring, and maintain vineyard sanitation."
        }
    },

    "Soybean": {
        "healthy": {
            "description": "Soybean plants are healthy and producing normal leaves and pods.",
            "cause": "Proper crop rotation and soil nutrition.",
            "prevention": "Use certified seeds, rotate crops every 2–3 years, and manage weeds effectively."
        }
    },

    "Peach": {
        "Bacterial_spot": {
            "description": "Small, water-soaked spots on leaves and fruit leading to defoliation and fruit blemishes.",
            "cause": "Caused by *Xanthomonas arboricola pv. pruni* bacteria.",
            "prevention": "Use resistant varieties, avoid overhead watering, and apply copper-based sprays in early growth stages."
        },
        "healthy": {
            "description": "Peach tree with no visible disease symptoms.",
            "cause": "Balanced nutrition and proper pruning.",
            "prevention": "Prune regularly, maintain spacing, and apply preventive copper sprays before blooming."
        }
    },

    "Tomato": {
        "Early_blight": {
            "description": "Dark concentric lesions on lower leaves, spreading upward and causing leaf drop.",
            "cause": "Fungal infection by *Alternaria solani*.",
            "prevention": "Use disease-free seeds, rotate crops, and apply fungicides containing chlorothalonil or copper."
        },
        "Late_blight": {
            "description": "Water-soaked leaf spots that turn brown and spread rapidly in cool, moist weather.",
            "cause": "Caused by *Phytophthora infestans*, spreading through air and rain.",
            "prevention": "Destroy infected plants, avoid overhead irrigation, and spray preventive fungicides like mancozeb."
        },
        "Tomato_Yellow_Leaf_Curl_Virus": {
            "description": "Leads to upward curling and yellowing of leaves with reduced fruit set.",
            "cause": "Spread by whiteflies feeding on infected plants.",
            "prevention": "Use resistant varieties, control whiteflies using sticky traps or neem oil, and remove infected plants."
        },
        "Target_Spot": {
            "description": "Circular lesions with gray centers and dark margins on leaves.",
            "cause": "Caused by *Corynespora cassiicola*, a fungus spread through splashing water.",
            "prevention": "Avoid overcrowding, remove infected leaves, and use fungicides like chlorothalonil."
        },
        "Septoria_leaf_spot": {
            "description": "Small, circular spots with dark borders and light centers on leaves.",
            "cause": "Caused by *Septoria lycopersici*, spreading through splashing rain.",
            "prevention": "Rotate crops, water at the base, and apply copper or mancozeb fungicides."
        },
        "Spider_mites_Two-spotted_spider_mite": {
            "description": "Tiny pests causing stippling and yellowing of leaves.",
            "cause": "Caused by spider mite infestations under hot, dry conditions.",
            "prevention": "Spray with neem oil, maintain humidity, and encourage beneficial predators like ladybugs."
        },
        "Bacterial_spot": {
            "description": "Dark, water-soaked spots on leaves and fruit that may cause cracking.",
            "cause": "Caused by *Xanthomonas campestris pv. vesicatoria* bacteria.",
            "prevention": "Use disease-free seeds, apply copper bactericides, and avoid touching wet plants."
        },
        "Tomato_mosaic_virus": {
            "description": "Causes mottled leaf coloring and distorted leaf growth.",
            "cause": "Transmitted via contaminated tools and human handling.",
            "prevention": "Disinfect tools and avoid smoking or handling tobacco before touching plants."
        },
        "Leaf_Mold": {
            "description": "Velvety olive-green mold on leaf undersides leading to leaf yellowing.",
            "cause": "Caused by *Passalora fulva* thriving in high humidity.",
            "prevention": "Increase ventilation, reduce humidity, and apply fungicides like copper hydroxide."
        },
        "healthy": {
            "description": "Tomato plant is healthy and producing normal foliage and fruit.",
            "cause": "Proper nutrition and ideal environmental conditions.",
            "prevention": "Continue regular monitoring and watering at soil level."
        }
    },

    "Apple": {
        "Cedar_apple_rust": {
            "description": "Orange-yellow spots on leaves and fruit that can reduce yield.",
            "cause": "Caused by *Gymnosporangium juniperi-virginianae* cycling between apple and juniper trees.",
            "prevention": "Remove nearby junipers and spray fungicides like myclobutanil in early spring."
        },
        "Black_rot": {
            "description": "Causes black lesions on leaves, fruit rot, and stem cankers.",
            "cause": "Caused by *Botryosphaeria obtusa* fungus surviving in infected debris.",
            "prevention": "Remove infected material, prune cankers, and apply fungicides during bloom."
        },
        "Apple_scab": {
            "description": "Dark olive-green spots on leaves and fruits that can cause cracking.",
            "cause": "Caused by *Venturia inaequalis* fungus thriving in moist weather.",
            "prevention": "Use resistant varieties, rake fallen leaves, and spray fungicides during bud development."
        },
        "healthy": {
            "description": "Apple tree is in good condition with no visible infections.",
            "cause": "Proper pruning and nutrient balance.",
            "prevention": "Maintain orchard hygiene and disease monitoring."
        }
    },

    "Pepper,_bell": {
        "Bacterial_spot": {
            "description": "Water-soaked lesions on leaves and fruit leading to defoliation and rot.",
            "cause": "Caused by *Xanthomonas campestris pv. vesicatoria*.",
            "prevention": "Avoid overhead watering, rotate crops, and use copper-based sprays."
        },
        "healthy": {
            "description": "Pepper plant shows normal foliage and fruit set.",
            "cause": "Proper watering and spacing.",
            "prevention": "Monitor regularly and maintain clean cultivation."
        }
    },

    "Cherry_(including_sour)": {
        "Powdery_mildew": {
            "description": "White, powdery fungal growth on leaves and young shoots.",
            "cause": "Caused by *Podosphaera clandestina* in warm, dry climates.",
            "prevention": "Apply sulfur-based fungicides and prune to improve air circulation."
        },
        "healthy": {
            "description": "Cherry tree appears vigorous with no visible leaf discoloration.",
            "cause": "Proper fertilization and irrigation.",
            "prevention": "Maintain pruning and balanced nutrition."
        }
    },

    "Strawberry": {
        "Leaf_scorch": {
            "description": "Brown spots with purple margins on leaves leading to scorched appearance.",
            "cause": "Caused by *Diplocarpon earlianum* fungus.",
            "prevention": "Avoid overhead irrigation, remove old leaves, and use fungicides like captan."
        },
        "healthy": {
            "description": "Strawberry plant is healthy and producing green leaves and fruit.",
            "cause": "Good air flow and optimal watering.",
            "prevention": "Maintain proper spacing and remove debris after harvest."
        }
    },

    "Corn_(maize)": {
        "Common_rust_": {
            "description": "Reddish-brown pustules on leaves, reducing photosynthesis and yield.",
            "cause": "Caused by *Puccinia sorghi* fungus.",
            "prevention": "Plant resistant hybrids and apply fungicides like propiconazole if infection occurs."
        },
        "Northern_Leaf_Blight": {
            "description": "Long, grayish-green elliptical lesions on leaves that expand rapidly.",
            "cause": "Caused by *Exserohilum turcicum* fungus.",
            "prevention": "Use resistant hybrids, rotate crops, and apply fungicides during early tasseling."
        },
        "Cercospora_leaf_spot_Gray_leaf_spot": {
            "description": "Rectangular gray lesions on leaves that can merge and destroy large leaf areas.",
            "cause": "Caused by *Cercospora zeae-maydis* fungus.",
            "prevention": "Practice crop rotation, avoid dense planting, and spray fungicides preventively."
        },
        "healthy": {
            "description": "Corn plant shows green, healthy leaves and strong stalks.",
            "cause": "Good soil fertility and pest management.",
            "prevention": "Maintain spacing and apply balanced fertilizers."
        }
    },

    "Potato": {
        "Late_blight": {
            "description": "Dark brown blotches on leaves, stems, and tubers causing rot.",
            "cause": "Caused by *Phytophthora infestans*, thriving in cool, moist environments.",
            "prevention": "Destroy infected plants, avoid overhead watering, and spray mancozeb-based fungicides."
        },
        "Early_blight": {
            "description": "Dark, concentric ring spots on older leaves causing leaf loss.",
            "cause": "Caused by *Alternaria solani* fungus.",
            "prevention": "Rotate crops and use copper-based fungicides preventively."
        },
        "healthy": {
            "description": "Potato crop is healthy and free of blight symptoms.",
            "cause": "Proper management and soil health.",
            "prevention": "Maintain good field hygiene and avoid excess moisture."
        }
    },

    "Blueberry": {
        "healthy": {
            "description": "Blueberry bush is healthy and producing quality berries.",
            "cause": "Proper pruning and soil acidity maintenance.",
            "prevention": "Maintain soil pH between 4.5–5.5 and ensure good drainage."
        }
    },

    "Raspberry": {
        "healthy": {
            "description": "Raspberry plant is healthy with no sign of disease or pest damage.",
            "cause": "Adequate spacing and watering.",
            "prevention": "Prune after fruiting and avoid waterlogging."
        }
    },

    "Squash": {
        "Powdery_mildew": {
            "description": "White powdery patches on leaves that spread rapidly under warm, dry conditions.",
            "cause": "Caused by *Podosphaera xanthii* fungus.",
            "prevention": "Apply neem oil or sulfur spray, ensure spacing, and remove infected leaves."
        }
    },

    "Orange": {
        "Haunglongbing_(Citrus_greening)": {
            "description": "Yellowing of leaf veins and misshapen, bitter fruits.",
            "cause": "Bacterial infection by *Candidatus Liberibacter asiaticus* transmitted by psyllids.",
            "prevention": "Remove infected trees, control psyllids using neem or imidacloprid, and use certified disease-free plants."
        }
    }
}
