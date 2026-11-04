from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

FEATURES = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal",
]


def main():
    csv_path = Path("data/heart.csv")
    if not csv_path.exists():
        raise SystemExit("Dataset not found. Put the Kaggle heart.csv file at data/heart.csv")
    data = pd.read_csv(csv_path)
    if "target" not in data or not set(FEATURES).issubset(data.columns):
        raise SystemExit("CSV must contain the 13 expected features and a 'target' column.")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(data[FEATURES], data["target"])
    output = Path("model/heart_model.joblib")
    output.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, output)
    print(f"Saved model to {output}")


if __name__ == "__main__":
    main()
