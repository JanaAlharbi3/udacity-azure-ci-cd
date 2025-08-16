# app.py
from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

MODEL_PATH = os.environ.get("MODEL_PATH", "model/model.joblib")
model = joblib.load(MODEL_PATH)

# Fallback list if the model does not expose feature_names_in_
BOSTON_FEATURES = [
    "CRIM", "ZN", "INDUS", "CHAS", "NOX",
    "RM", "AGE", "DIS", "RAD", "TAX",
    "PTRATIO", "B", "LSTAT"
]

def expected_feature_order():
    # Most sklearn >=1.0 pipelines/estimators expose this after fit
    names = getattr(model, "feature_names_in_", None)
    if names is not None:
        try:
            return list(names)
        except Exception:
            pass
    # Fallback to the Boston dataset features
    return BOSTON_FEATURES

@app.get("/")
def home():
    return "ML API is up 🟢"

@app.get("/features")
def features():
    return jsonify({"feature_names": expected_feature_order()})

@app.post("/predict")
def predict():
    try:
        payload = request.get_json(force=True)

        if isinstance(payload, dict) and all(not isinstance(v, list) for v in payload.values()):
            payload = {k: [v] for k, v in payload.items()}

        df = pd.DataFrame(payload)

        # Reorder columns to what the model expects; fill any missing with 0
        expected = expected_feature_order()
        df = df.reindex(columns=expected, fill_value=0)

        preds = model.predict(df)
        return jsonify({"prediction": preds.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
