from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException

from app.schemas import HeartFeatures

MODEL_PATH = Path(__file__).resolve().parent.parent / "model" / "heart_model.joblib"
FEATURES = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal",
]
app = FastAPI(title="Heart Disease Prediction API", version="1.0.0")

try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    model = None


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": model is not None}


@app.get("/info")
def info():
    return {"model_type": "RandomForestClassifier", "features": FEATURES}


@app.post("/predict")
def predict(data: HeartFeatures):
    if model is None:
        raise HTTPException(status_code=503, detail="Model file is missing. Train the model first.")
    row = pd.DataFrame([data.model_dump()], columns=FEATURES)
    prediction = int(model.predict(row)[0])
    return {"heart_disease": bool(prediction)}
