from treatment import get_treatment
import os
import matplotlib.pyplot as plt
from collections import Counter
from database import collection
from soil_model import predict_soil
from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os

from disease_model import predict_disease

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.route("/history")
def history():

    crop = request.args.get("crop", "").strip()
    disease = request.args.get("disease", "").strip()

    query = {}

    if crop:
        query["crop"] = {"$regex": crop, "$options": "i"}

    if disease:
        query["disease"] = {"$regex": disease, "$options": "i"}

    records = list(collection.find(query))

    return render_template(
        "history.html",
        records=records,
        crop=crop,
        disease=disease
    )

@app.route("/map")
def map_page():

    records = []

    for doc in collection.find():

        if "location" in doc and "coordinates" in doc["location"]:

            records.append({

                "crop": doc["crop"],

                "disease": doc["disease"],

                "confidence": doc["confidence"],

                "soil": doc["soil_moisture"],

                "latitude": doc["location"]["coordinates"][1],

                "longitude": doc["location"]["coordinates"][0]

            })

    return render_template(
        "map.html",
        records=records
    )
@app.route("/dashboard")
def dashboard():

    records = list(collection.find())

    total = len(records)

    healthy = 0
    diseased = 0

    moisture = []

    diseases = []

    for row in records:

        diseases.append(row["disease"])

        moisture.append(row["soil_moisture"])

        if "healthy" in row["disease"].lower():

            healthy += 1

        else:

            diseased += 1

    average = 0

    if len(moisture) > 0:

        average = round(sum(moisture)/len(moisture),2)

    counts = Counter(diseases)

    labels = list(counts.keys())

    values = list(counts.values())

    os.makedirs("static/charts",exist_ok=True)

    plt.figure(figsize=(6,6))

    plt.pie(

        values,

        labels=labels,

        autopct="%1.1f%%"

    )

    plt.title("Disease Distribution")

    plt.savefig("static/charts/pie.png")

    plt.close()
    # ---------------- Bar Chart ----------------

    plt.figure(figsize=(8,5))

    plt.bar(
      range(len(moisture)),
      moisture
    )

    plt.xlabel("Prediction Number")

    plt.ylabel("Soil Moisture (%)")

    plt.title("Soil Moisture Levels")

    plt.savefig("static/charts/bar.png")

    plt.close()
    return render_template(

    "dashboard.html",

    total=total,

    healthy=healthy,

    diseased=diseased,

    average=average,

    records=records

)

@app.route("/upload", methods=["POST"])
def upload():

    crop = request.form["crop"]

    latitude = request.form["latitude"]

    longitude = request.form["longitude"]

    temperature = request.form["temperature"]

    humidity = request.form["humidity"]

    rainfall = request.form["rainfall"]

    image = request.files["leaf"]

    filename = secure_filename(image.filename)

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    image.save(filepath)

    disease, confidence = predict_disease(filepath)
    recommendation = get_treatment(disease)

    soil = predict_soil(
        float(temperature),
        float(humidity),
        float(rainfall)
    )

    collection.insert_one({

        "crop": crop,

        "location": {
            "type": "Point",
            "coordinates": [
                float(longitude),
                float(latitude)
            ]
        },

        "temperature": float(temperature),

        "humidity": float(humidity),

        "rainfall": float(rainfall),

        "disease": disease,

        "confidence": confidence,

        "soil_moisture": soil,

        "image": filename

    })

    return render_template(

        "index.html",

        success=True,

        filename=filename,

        crop=crop,

        latitude=latitude,

        longitude=longitude,

        temperature=temperature,

        humidity=humidity,

        rainfall=rainfall,

        disease=disease,

        confidence=confidence,

        soil=soil,
        recommendation=recommendation

    )


if __name__ == "__main__":
    app.run(debug=True)