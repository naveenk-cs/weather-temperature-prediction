import joblib
import pandas as pd
model_info = joblib.load(
    "models/weather_temperature_model.pkl"
)

model = model_info["model"]
features = model_info["features"]

def predict_temperature(row):
    row = row[features].to_frame().T

    prediction = model.predict(row)[0]

    return prediction