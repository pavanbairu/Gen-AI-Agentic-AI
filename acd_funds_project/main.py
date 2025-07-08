# main.py
# Description: Main entry point for the ACD Funds Transfer API
from fastapi import FastAPI
from app.routers import fund, transfer

app = FastAPI(title="ACD Funds API", version="1.0")

# Include routers
app.include_router(fund.router, prefix="/funds", tags=["Funds"])
app.include_router(transfer.router, prefix="/transfer", tags=["Transfer"])

@app.get("/")
def root():
    return {"message": "Welcome to the ACD Funds Transfer API"}
