from pathlib import Path

import pandas as pd
from flask import Flask, render_template, request
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "yield_prediction_dataset.csv"

FEATURE_COLUMNS = [
    "latitude",
    "longitude",
    "NDVI",
    "GNDVI",
    "NDWI",
    "SAVI",
    "soil_moisture",
    "temperature",
    "rainfall",
    "crop_type",
    "NDVI_temp",
    "NDVI_rainfall",
    "SAVI_soil_moisture",
]


def prepare_dataset():
    df = pd.read_csv(DATA_PATH)
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")].copy()

    for col in [
        "latitude",
        "longitude",
        "NDVI",
        "GNDVI",
        "NDWI",
        "SAVI",
        "soil_moisture",
        "temperature",
        "rainfall",
        "yield",
    ]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=[
        "latitude",
        "longitude",
        "NDVI",
        "GNDVI",
        "NDWI",
        "SAVI",
        "soil_moisture",
        "temperature",
        "rainfall",
        "crop_type",
        "yield",
    ]).copy()

    df["NDVI_temp"] = df["NDVI"] * df["temperature"]
    df["NDVI_rainfall"] = df["NDVI"] * df["rainfall"]
    df["SAVI_soil_moisture"] = df["SAVI"] * df["soil_moisture"]

    encoder = LabelEncoder()
    df["crop_type"] = encoder.fit_transform(df["crop_type"].astype(str))

    X = df[FEATURE_COLUMNS].copy()
    y = df["yield"]

    scaler = StandardScaler()
    X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=FEATURE_COLUMNS)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(random_state=42, n_estimators=500)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    return model, scaler, encoder, {
        "row_count": len(df),
        "r2_score": round(r2_score(y_test, y_pred), 4),
    }


MODEL, SCALER, ENCODER, METRICS = prepare_dataset()
CROP_CHOICES = ENCODER.classes_.tolist()


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    form_data = None

    if request.method == "POST":
        form_data = request.form.to_dict()
        feature_row = {
            "latitude": float(form_data["latitude"]),
            "longitude": float(form_data["longitude"]),
            "NDVI": float(form_data["NDVI"]),
            "GNDVI": float(form_data["GNDVI"]),
            "NDWI": float(form_data["NDWI"]),
            "SAVI": float(form_data["SAVI"]),
            "soil_moisture": float(form_data["soil_moisture"]),
            "temperature": float(form_data["temperature"]),
            "rainfall": float(form_data["rainfall"]),
            "crop_type": ENCODER.transform([form_data["crop_type"]])[0],
            "NDVI_temp": 0.0,
            "NDVI_rainfall": 0.0,
            "SAVI_soil_moisture": 0.0,
        }

        feature_row["NDVI_temp"] = feature_row["NDVI"] * feature_row["temperature"]
        feature_row["NDVI_rainfall"] = feature_row["NDVI"] * feature_row["rainfall"]
        feature_row["SAVI_soil_moisture"] = feature_row["SAVI"] * feature_row["soil_moisture"]

        row_df = pd.DataFrame([feature_row], columns=FEATURE_COLUMNS)
        scaled_row = pd.DataFrame(SCALER.transform(row_df), columns=FEATURE_COLUMNS)
        prediction = round(float(MODEL.predict(scaled_row)[0]), 2)

    return render_template(
        "index.html",
        crop_choices=CROP_CHOICES,
        metrics=METRICS,
        prediction=prediction,
        form_data=form_data,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
