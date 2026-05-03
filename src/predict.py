import pandas as pd
import joblib


MODEL_PATH = "model/water_model.pkl"


def predict_water_quality(input_data):
    model = joblib.load(MODEL_PATH)

    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]

    return "Potable" if prediction == 1 else "Not Potable"


if __name__ == "__main__":
    sample = {
        "ph": 7.0,
        "Hardness": 204.89,
        "Solids": 20791.32,
        "Chloramines": 7.3,
        "Sulfate": 368.5,
        "Conductivity": 564.3,
        "Organic_carbon": 10.3,
        "Trihalomethanes": 86.9,
        "Turbidity": 2.96
    }

    result = predict_water_quality(sample)
    print("Prediction:", result)
