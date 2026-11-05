# Heart Disease Prediction API

A simple project to practice deploying a machine learning model with **FastAPI, Docker, and Render**.

## How it works

1. Train a Random Forest classifier using `heart.csv`.
2. Save the model with joblib.
3. Use FastAPI to accept patient features and return a prediction.
4. Package the API and model with Docker for deployment.

## Project structure

```text
app/
  main.py                  # API endpoints and model loading
  schemas.py               # Input validation
model/
  heart_model.joblib        # Saved model
train_model.py             # Model training
requirements.txt           # Python dependencies
Dockerfile                 # Container setup
docker-compose.yml         # Local container setup
```

## Train the model

Use Python 3.11. Download the [Heart Disease dataset from Kaggle](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset) and place `heart.csv` inside `data/`.

The CSV used during local setup came from a [GitHub mirror](https://github.com/sharmaroshan/Heart-UCI-Dataset/blob/master/heart.csv). Replace it with the Kaggle CSV and retrain to use the exact assignment source.

```bash
python3.11 -m venv .venv311
source .venv311/bin/activate
python -m pip install -r requirements.txt
python train_model.py
```

This saves the trained model to `model/heart_model.joblib`.

## Run with Docker

Start Docker Desktop, then run:

```bash
docker compose build
docker compose up -d
```

Open [Swagger UI](http://localhost:8000/docs) to try the API.

To stop the app:

```bash
docker compose down
```

## API endpoints

| Method | Endpoint | Purpose |
| --- | --- | --- |
| GET | `/health` | Check service and model status |
| GET | `/info` | View model type and input features |
| POST | `/predict` | Get a heart disease prediction |

Example request body for `/predict`:

```json
{
  "age": 63,
  "sex": 1,
  "cp": 3,
  "trestbps": 145,
  "chol": 233,
  "fbs": 1,
  "restecg": 0,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 2.3,
  "slope": 0,
  "ca": 0,
  "thal": 1
}
```

Response from the locally tested model:

```json
{"heart_disease": true}
```

## Deploy on Render

1. Push the project to GitHub, including `model/heart_model.joblib`.
2. Create a Render Web Service and connect the repository.
3. Select Docker and use the repository root as the build context.
4. Set the health check path to `/health` and deploy.
5. Open `/docs` on the live URL and test a prediction. Confirm `/health` reports `model_loaded: true`.

The Dockerfile uses Render's `PORT` environment variable and defaults to port 8000 locally.

Submit the GitHub repository link and live Render URL after deployment.

## Practice scope

The Docker build and local API endpoints were checked successfully. Training uses all dataset rows; no accuracy evaluation is included. This project demonstrates model deployment and is not intended for medical diagnosis.
