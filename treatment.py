def get_treatment(disease):

    treatments = {

        "Pepper__bell___Bacterial_spot": {
            "Symptoms": "Small dark spots with yellow halos on leaves.",
            "Cause": "Bacterial infection.",
            "Treatment": "Apply copper-based bactericide.",
            "Organic": "Neem oil spray.",
            "Prevention": "Use disease-free seeds and avoid overhead watering."
        },

        "Pepper__bell___healthy": {
            "Symptoms": "Healthy crop.",
            "Cause": "No disease.",
            "Treatment": "No treatment required.",
            "Organic": "Maintain organic farming practices.",
            "Prevention": "Regular irrigation and balanced fertilizer."
        },

        "Potato___Early_blight": {
            "Symptoms": "Brown concentric spots on older leaves.",
            "Cause": "Alternaria solani fungus.",
            "Treatment": "Spray Mancozeb or Chlorothalonil.",
            "Organic": "Neem oil spray.",
            "Prevention": "Crop rotation and remove infected leaves."
        },

        "Potato___Late_blight": {
            "Symptoms": "Dark water-soaked lesions on leaves.",
            "Cause": "Phytophthora infestans.",
            "Treatment": "Copper fungicide or Metalaxyl.",
            "Organic": "Copper soap spray.",
            "Prevention": "Avoid water stagnation."
        },

        "Potato___healthy": {
            "Symptoms": "Healthy crop.",
            "Cause": "No disease.",
            "Treatment": "No treatment required.",
            "Organic": "Maintain soil fertility.",
            "Prevention": "Regular crop monitoring."
        },

        "Tomato_Bacterial_spot": {
            "Symptoms": "Small black spots on leaves and fruits.",
            "Cause": "Bacterial infection.",
            "Treatment": "Copper bactericide.",
            "Organic": "Neem oil.",
            "Prevention": "Avoid overhead irrigation."
        },

        "Tomato_Early_blight": {
            "Symptoms": "Brown circular spots on leaves.",
            "Cause": "Alternaria fungus.",
            "Treatment": "Mancozeb or Chlorothalonil.",
            "Organic": "Neem oil spray.",
            "Prevention": "Remove infected leaves."
        },

        "Tomato_Late_blight": {
            "Symptoms": "Dark brown lesions with white fungal growth.",
            "Cause": "Phytophthora infestans.",
            "Treatment": "Copper Oxychloride or Metalaxyl.",
            "Organic": "Copper-based organic fungicide.",
            "Prevention": "Avoid excessive moisture."
        },

        "Tomato_Leaf_Mold": {
            "Symptoms": "Yellow spots with mold underneath leaves.",
            "Cause": "Leaf mold fungus.",
            "Treatment": "Chlorothalonil spray.",
            "Organic": "Neem oil.",
            "Prevention": "Increase air circulation."
        },

        "Tomato_Septoria_leaf_spot": {
            "Symptoms": "Small circular spots with dark borders.",
            "Cause": "Septoria fungus.",
            "Treatment": "Copper fungicide.",
            "Organic": "Neem oil.",
            "Prevention": "Remove infected leaves."
        },

        "Tomato_Spider_mites_Two_spotted_spider_mite": {
            "Symptoms": "Yellow speckles and webbing on leaves.",
            "Cause": "Spider mite infestation.",
            "Treatment": "Miticide spray.",
            "Organic": "Neem oil and insecticidal soap.",
            "Prevention": "Maintain proper humidity."
        },

        "Tomato__Target_Spot": {
            "Symptoms": "Dark target-shaped spots on leaves.",
            "Cause": "Target Spot fungus.",
            "Treatment": "Azoxystrobin fungicide.",
            "Organic": "Copper spray.",
            "Prevention": "Remove infected plant debris."
        },

        "Tomato__Tomato_YellowLeaf__Curl_Virus": {
            "Symptoms": "Yellow curled leaves and stunted growth.",
            "Cause": "Whitefly-transmitted virus.",
            "Treatment": "Control whiteflies.",
            "Organic": "Neem oil.",
            "Prevention": "Use resistant varieties."
        },

        "Tomato__Tomato_mosaic_virus": {
            "Symptoms": "Mosaic patterns on leaves.",
            "Cause": "Tomato Mosaic Virus.",
            "Treatment": "No chemical cure.",
            "Organic": "Remove infected plants.",
            "Prevention": "Disinfect tools and use healthy seedlings."
        },

        "Tomato_healthy": {
            "Symptoms": "Healthy crop.",
            "Cause": "No disease.",
            "Treatment": "No treatment required.",
            "Organic": "Maintain balanced nutrition.",
            "Prevention": "Regular monitoring and irrigation."
        }

    }

    return treatments.get(
        disease,
        {
            "Symptoms": "Information not available.",
            "Cause": "Unknown.",
            "Treatment": "Consult the nearest agricultural extension officer.",
            "Organic": "Not available.",
            "Prevention": "Regular crop monitoring."
        }
    )