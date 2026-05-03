import json
import os
import boto3
import pandas as pd
import joblib
import psycopg2

s3 = boto3.client("s3")

MODEL_FILE = "/tmp/water_model.pkl"
INPUT_FILE = "/tmp/water_potability.csv"
OUTPUT_FILE = "/tmp/predictions.csv"


def get_db_connection():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        connect_timeout=5
    )


def save_prediction_to_db(input_data, prediction_result):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id SERIAL PRIMARY KEY,
            ph FLOAT,
            hardness FLOAT,
            solids FLOAT,
            chloramines FLOAT,
            sulfate FLOAT,
            conductivity FLOAT,
            organic_carbon FLOAT,
            trihalomethanes FLOAT,
            turbidity FLOAT,
            prediction INT,
            prediction_label TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        INSERT INTO predictions (
            ph, hardness, solids, chloramines, sulfate, conductivity,
            organic_carbon, trihalomethanes, turbidity,
            prediction, prediction_label
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        input_data.get("ph"),
        input_data.get("Hardness"),
        input_data.get("Solids"),
        input_data.get("Chloramines"),
        input_data.get("Sulfate"),
        input_data.get("Conductivity"),
        input_data.get("Organic_carbon"),
        input_data.get("Trihalomethanes"),
        input_data.get("Turbidity"),
        prediction_result["prediction"],
        prediction_result["prediction_label"]
    ))

    conn.commit()
    cursor.close()
    conn.close()


def load_model(bucket_name):
    s3.download_file(bucket_name, "model/water_model.pkl", MODEL_FILE)
    return joblib.load(MODEL_FILE)


def predict_single(model, input_data):
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]

    return {
        "prediction": int(prediction),
        "prediction_label": "Potable" if prediction == 1 else "Not Potable"
    }


def batch_predict(bucket_name):
    s3.download_file(bucket_name, "raw/water_potability.csv", INPUT_FILE)

    model = load_model(bucket_name)

    df = pd.read_csv(INPUT_FILE)
    df = df.fillna(df.mean(numeric_only=True))

    if "Potability" in df.columns:
        X = df.drop("Potability", axis=1)
    else:
        X = df

    df["Prediction"] = model.predict(X)
    df["Prediction_Label"] = df["Prediction"].apply(
        lambda x: "Potable" if x == 1 else "Not Potable"
    )

    df.to_csv(OUTPUT_FILE, index=False)
    s3.upload_file(OUTPUT_FILE, bucket_name, "predictions/predictions.csv")

    return {"message": "Batch prediction completed successfully."}


def lambda_handler(event, context):
    bucket_name = os.environ["BUCKET_NAME"]

    if "body" in event:
        body = json.loads(event["body"]) if isinstance(event["body"], str) else event["body"]

        model = load_model(bucket_name)
        result = predict_single(model, body)

        save_prediction_to_db(body, result)

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(result)
        }

    result = batch_predict(bucket_name)

    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }
