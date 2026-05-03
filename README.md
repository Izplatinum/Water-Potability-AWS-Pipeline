# 💧 Water Potability Prediction Pipeline (AWS | ML | DevOps)

## 🚀 Overview

This project is a **production-ready, end-to-end machine learning pipeline** deployed on AWS.

It predicts whether water is **potable or not** using a trained ML model and exposes both:

- ✅ **Batch processing pipeline (S3 → Lambda)**
- ✅ **Real-time API (API Gateway → Lambda)**
- ✅ **Database persistence (RDS PostgreSQL)**

---

## 🧠 Architecture
      ┌──────────────┐
      │   User/API   │
      └──────┬───────┘
             │
    ┌────────▼────────┐
    │  API Gateway    │
    └────────┬────────┘
             │
    ┌────────▼────────┐
    │ AWS Lambda      │
    │ (Docker Image)  │
    └────────┬────────┘
             │
 ┌───────────▼───────────┐
 │  ML Model (Scikit)    │
 └───────────┬───────────┘
             │             │

┌─────────────▼─────────────┐
│ Amazon S3 (Batch Data) │
└─────────────┬─────────────┘
│
┌─────────────▼─────────────┐
│ RDS PostgreSQL (Storage) │
└───────────────────────────┘

---

## ⚙️ Tech Stack

- **Cloud:** AWS (Lambda, S3, API Gateway, ECR, RDS, IAM)
- **DevOps:** Docker, Terraform, Ansible
- **Data:** Python (Pandas, NumPy, Scikit-learn)
- **Database:** PostgreSQL (RDS)

---

## 🔄 Features

### 1. Batch Processing (S3 Trigger)
- Upload CSV → S3
- S3 triggers Lambda
- Predictions generated
- Results saved to S3

### 2. Real-Time API
- POST request → API Gateway
- Lambda runs model
- Returns prediction instantly

### 3. Database Storage
- Predictions stored in **RDS PostgreSQL**
- Enables analytics & monitoring

---

## 📊 Example API Request

```bash
curl -X POST https://YOUR_API_ENDPOINT \
  -H "Content-Type: application/json" \
  -d '{
    "ph": 7.0,
    "Hardness": 204.89,
    "Solids": 20791.32,
    "Chloramines": 7.3,
    "Sulfate": 368.5,
    "Conductivity": 564.3,
    "Organic_carbon": 10.3,
    "Trihalomethanes": 86.9,
    "Turbidity": 2.96
  }'

Response:
{
  "prediction": 0,
  "prediction_label": "Not Potable"
}

📁 Project Structure
water-potability-aws-pipeline/
│
├── src/                # ML training & prediction
├── lambda/             # Lambda handler
├── terraform/          # Infrastructure as Code
├── ansible/            # Automation scripts
├── Dockerfile          # Lambda container
├── requirements.txt
└── README.md

🧪 Machine Learning
Model: Random Forest Classifier
Dataset: Water quality dataset
Handles missing values
Outputs classification + label

🚀 Deployment
1. Train model
python src/train_model.py

2. Build Docker image
docker build -t water-potability-lambda .

3. Push to ECR
docker push <your-ecr-repo>

4. Deploy with Terraform
cd terraform
terraform init
terraform apply
