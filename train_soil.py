import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
df = pd.read_csv("dataset/soil_data.csv")

X = df[["Temperature","Humidity","Rainfall"]]

y = df["Soil_Moisture"]

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X,y)

joblib.dump(model,"models/soil_model.pkl")

print("Soil Moisture Model Saved Successfully!")