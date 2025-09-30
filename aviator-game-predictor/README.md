Aviator Game Predictor

Overview
Feature-engineered ML pipeline + Flask API that returns a probability estimate for >=2.0x ("purple") and >=10.0x ("red") events, with a tiny HTML client for demo. This aligns with your resume project.

Quickstart
1) Python 3.11+
2) pip install -r requirements.txt
3) python app.py
4) Open client/index.html in a browser

Endpoints
- POST /predict
  body: {"history":[1.12, 2.1, 5.6, ...]}
  returns: {"p_ge_2x": 0.42, "p_ge_10x": 0.03}
