import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


DATA_PATH = "data/water_potability.csv"
MODEL_PATH = "model/water_model.pkl"


def train_model():
    df = pd.read_csv(DATA_PATH)
    df = df.fillna(df.mean(numeric_only=True))

    X = df.drop("Potability", axis=1)
    y = df["Potability"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    os.makedirs("model", exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print("Model trained successfully.")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Model saved to {MODEL_PATH}")


if __name__ == "__main__":
    train_model()
