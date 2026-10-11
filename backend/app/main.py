from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.auth.router import router as auth_router
from app.merchants.router import router as merchant_router
from app.wallets.router import router as wallet_router
from app.transactions.router import router as transaction_router
from app.api_keys.router import router as api_key_router
from app.payments.router import router as payment_router
from app.mpesa.router import router as mpesa_router
from app.dashboard.router import router as dashboard_router
from app.payment_requests.router import router as payment_request_router
from app.merchant_settings.router import router as merchant_settings_router

app = FastAPI(
    title="RobertPay API",
    version="1.0.0",
    description="Payment Platform API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://robertpay.vercel.app",
        "https://robertpay-eswk2k8tv-robert00-1s-projects.vercel.app",

    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(merchant_router)
app.include_router(wallet_router)
app.include_router(transaction_router)
app.include_router(api_key_router)
app.include_router(payment_router)
app.include_router(mpesa_router)
app.include_router(dashboard_router)
app.include_router(payment_request_router)
app.include_router(merchant_settings_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to RobertPay API"
    }
