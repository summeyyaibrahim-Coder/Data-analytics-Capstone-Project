# Crop Yield Prediction Web App

This project contains a simple Flask-based web app for predicting crop yield from field characteristics and environmental variables.

## Run locally

1. Create a virtual environment:
   python3 -m venv .venv
2. Activate it:
   source .venv/bin/activate
3. Install dependencies:
   pip install -r requirements.txt
4. Start the app:
   python app.py
5. Open http://localhost:5000 in your browser.

## Model summary

The app mirrors the notebook workflow:

- loads the crop-yield dataset
- creates engineered features such as NDVI temperature and rainfall interactions
- encodes crop type
- scales features
- trains a Random Forest regressor
- predicts yield from user-entered field values
