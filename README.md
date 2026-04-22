🚀 Credit Default Prediction API

Production-ready Machine Learning API to predict loan default risk using FastAPI + Docker + CI/CD

💡 Overview

This project is a Credit Risk Prediction System that predicts whether a borrower is likely to default on a loan.

It includes:

📊 Data preprocessing & feature engineering
🤖 ML model training (Logistic Regression, XGBoost)
⚖️ Class imbalance handling (SMOTE + Tomek)
📈 Model evaluation (ROC-AUC, KS, Gini)
🚀 Deployment using FastAPI + Docker
🏗️ Project Structure
.
├── .github/workflows/       # CI/CD pipelines
│
├── app/
│   ├── artifacts/
│   │   └── model_data.joblib   # Trained model + scaler + features
│   │
│   ├── __init__.py
│   ├── main.py                # FastAPI entry point
│   └── prediction_helper.py  # Prediction logic
│
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
🧠 Key Features
Predicts loan default probability
Pre-trained ML model (saved as .joblib)
Clean API structure using FastAPI
Modular prediction pipeline
Dockerized for easy deployment
CI/CD ready
📊 Model Details
🎯 Target Variable
default
0 → No Default
1 → Default
🔍 Input Features
👤 Customer Information
Age
Income
Residence Type (Owned / Rented / Mortgage)
💳 Credit Information
Credit Utilization
Number of Open Accounts
Average DPD
Delinquency Ratio
💰 Loan Information
Loan Amount
Loan Tenure (Months)
Loan Purpose (Home / Education / Personal / Auto)
Loan Type (Secured / Unsecured)
📥 Example API Request
{
  "age": 32,
  "income": 750000,
  "loan_amount": 250000,
  "loan_tenure_months": 36,
  "avg_dpd_per_delinquency": 2.5,
  "delinquency_ratio": 15.0,
  "credit_utilization_ratio": 45.0,
  "number_of_open_accounts": 3,
  "residence_type": "Owned",
  "loan_purpose": "Personal",
  "loan_type": "Unsecured"
}
📤 Example Response
{
  "default_probability": 0.23,
  "prediction": "Low Risk"
}
🧾 Model Artifact

The trained model is stored here:

app/artifacts/model_data.joblib

It contains:

Trained ML model
Feature list
Scaler
⚙️ Installation & Setup
1️⃣ Clone Repo
git clone https://github.com/your-username/credit-default-api.git
cd credit-default-api
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run FastAPI Server
uvicorn app.main:app --reload
4️⃣ Open API Docs
http://127.0.0.1:8000/docs
🐳 Run with Docker
Build Image
docker build -t credit-risk-api .
Run Container
docker run -p 8000:8000 credit-risk-api
🔁 CI/CD

Located in:

.github/workflows/

Includes:

Automated builds
Testing pipelines
Deployment workflows
📈 Model Performance
Metric	Value
Accuracy	93%
Recall (Default)	94%
F1 Score	0.70
ROC-AUC	0.98
Gini	0.96
⚡ Future Improvements
Add SHAP explainability
Add authentication layer (JWT)
Deploy on cloud (AWS/GCP)
Add frontend dashboard
👨‍💻 Author

Shashwat

⭐ Support

If this project helped you, give it a ⭐ on GitHub 🚀
