from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.prediction_helper import predict
from pydantic import BaseModel


class CreditRiskInput(BaseModel):
    age: int
    income: float
    loan_amount: float
    loan_tenure_months: int
    avg_dpd_per_delinquency: float
    delinquency_ratio: float
    credit_utilization_ratio: float
    num_open_accounts: int
    residence_type: str
    loan_purpose: str
    loan_type: str


class CreditRiskOutput(BaseModel):
    probability: float
    credit_score: int
    rating: str


app = FastAPI()

# ✅ CORS middleware add karo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # development ke liye sab allow
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping")
def ping():
    return "Credit risk prediction server"


@app.post("/predict_credit_risk", response_model=CreditRiskOutput)
def predict_credit_risk(input_data: CreditRiskInput):
    try:

        probability, credit_score, rating = predict(
            input_data.age,
            input_data.income,
            input_data.loan_amount,
            input_data.loan_tenure_months,
            input_data.avg_dpd_per_delinquency,
            input_data.delinquency_ratio,
            input_data.credit_utilization_ratio,
            input_data.num_open_accounts,
            input_data.residence_type,
            input_data.loan_purpose,
            input_data.loan_type,
        )

        return CreditRiskOutput(
            probability=probability, credit_score=credit_score, rating=rating
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
