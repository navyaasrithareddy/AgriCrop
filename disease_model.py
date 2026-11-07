import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

MODEL_PATH = "models/disease_model.h5"

model = load_model(MODEL_PATH)

with open("models/class_names.txt") as f:
    class_names = [line.strip() for line in f]


def predict_disease(img_path):

    img = image.load_img(
        img_path,
        target_size=(224, 224)
    )

    img_array = image.img_to_array(img)

    img_array = img_array / 255.0

    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    confidence = float(np.max(prediction)) * 100

    disease = class_names[np.argmax(prediction)]

    return disease, round(confidence, 2)  