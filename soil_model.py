import joblib

model = joblib.load("models/soil_model.pkl")

def predict_soil(temperature, humidity, rainfall):

    prediction = model.predict(
        [[temperature,humidity,rainfall]]
    )

    return round(float(prediction[0]),2)