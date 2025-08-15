 # app.py
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# load the pre-trained pipeline (Scaler + Model) once at startup
MODEL_PATH = "model/model.joblib"  # <-- place your file here
model = joblib.load(MODEL_PATH)

@app.get("/")
def home():
    return "ML API is up 🟢"

@app.post("/predict")
def predict():
    try:
        payload = request.get_json()
        # payload should be a dict of column->{"0": value} as Udacity’s example
        df = pd.DataFrame(payload)
        preds = model.predict(df)
        return jsonify({"prediction": preds.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

