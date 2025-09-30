from flask import Flask, request, jsonify
import numpy as np
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Toy model (fits on synthetic data at startup). Replace with your trained model.
rng = np.random.default_rng(42)
X = rng.normal(size=(500, 5))
y2 = (X.mean(axis=1) + rng.normal(scale=0.5, size=500) > 0).astype(int)  # proxy for >=2x
y10 = (X.mean(axis=1) + rng.normal(scale=1.0, size=500) > 1.2).astype(int) # proxy for >=10x
clf2 = LogisticRegression().fit(X, y2)
clf10 = LogisticRegression().fit(X, y10)

def make_features(history):
    # simple stats over last N items
    arr = np.array(history[-20:], dtype=float)
    feats = np.array([
        arr.mean(), arr.std() if len(arr)>1 else 0.0,
        np.median(arr), arr.min(), arr.max()
    ]).reshape(1, -1)
    return feats

@app.post("/predict")
def predict():
    body = request.get_json(force=True)
    history = body.get("history", [])
    if not history:
        return jsonify(error="history is required"), 400
    X = make_features(history)
    p2 = float(clf2.predict_proba(X)[0,1])
    p10 = float(clf10.predict_proba(X)[0,1])
    return jsonify(p_ge_2x=round(p2, 4), p_ge_10x=round(p10, 4))

if __name__ == "__main__":
    app.run(debug=True)
