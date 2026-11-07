from tensorflow.keras.preprocessing.image import ImageDataGenerator

DATASET_PATH = "dataset/PlantVillage"

datagen = ImageDataGenerator(validation_split=0.2)

generator = datagen.flow_from_directory(
    DATASET_PATH,
    target_size=(224,224),
    batch_size=32,
    class_mode="categorical",
    subset="training"
)

classes = list(generator.class_indices.keys())

with open("models/class_names.txt","w") as f:
    for c in classes:
        f.write(c + "\n")

print("class_names.txt Created Successfully!")