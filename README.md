#  Water Potability Prediction Pipeline (AWS | ML | DevOps)

Production-ready end-to-end machine learning pipeline deployed on AWS to predict water potability using real-time and batch processing.

---

##  Architecture

```text
User/API → API Gateway → Lambda (Docker) → ML Model → RDS PostgreSQL
                          ↓
                  S3 (Batch Input)
                          ↓
                     Lambda Trigger
                          ↓
                     Predictions → S3 + RDS
```

---

##  Tech Stack

* **Cloud:** AWS (Lambda, S3, API Gateway, RDS, IAM, ECR)
* **DevOps:** Docker, Terraform, Ansible
* **Data & ML:** Python (Pandas, NumPy, Scikit-learn)
* **Database:** PostgreSQL (RDS)

---

##  Features

###  Batch Processing (S3 Trigger)

* Upload CSV data to S3
* Automatically triggers Lambda
* Generates predictions at scale
* Stores results in S3 and RDS

---

###  Real-Time Prediction API

* REST API exposed via API Gateway
* Lambda processes input instantly
* Returns prediction in real-time

---

###  Data Persistence

* Predictions stored in **RDS PostgreSQL**
* Enables analytics and monitoring

---

##  Example API Request

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
```

---

##  Example Response

```json
{
  "prediction": 0,
  "prediction_label": "Not Potable"
}
```

---

##  Project Structure

```text
water-potability-aws-pipeline/
│
├── src/           # ML training & preprocessing
├── lambda/        # Lambda handler (prediction logic)
├── terraform/     # Infrastructure as Code
├── ansible/       # Automation scripts
├── Dockerfile     # Lambda container image
├── requirements.txt
└── README.md
```

---

##  Machine Learning

* Model: **Random Forest Classifier**
* Dataset: Water quality dataset
* Handles missing values and feature preprocessing
* Outputs classification + label (Potable / Not Potable)

---

##  Deployment Workflow

```bash
# Train model
python src/train_model.py

# Build Docker image
docker build -t water-potability-lambda .

# Push to ECR
docker push <your-ecr-repo>

# Deploy infrastructure
cd terraform
terraform init
terraform apply
```

---

##  Key Highlights

* Built scalable ML pipeline with **serverless architecture**
* Combined **batch + real-time processing**
* Integrated **API Gateway + Lambda for low-latency inference**
* Used **Terraform & Ansible for infrastructure automation**
* Designed **production-ready cloud ML system**

---

##  What I Learned

* Deploying machine learning models in production on AWS
* Designing event-driven serverless architectures
* Integrating APIs with ML pipelines
* Using Docker + Lambda for scalable inference
* Managing infrastructure using Terraform

---

##  Author

**Hizedihar Djato Bougonou**

* LinkedIn: https://linkedin.com/in/hizedihar-djato-bougonou
* GitHub: https://github.com/Izplatinum
