### app/routers/transfer.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.fund_schemas import TransferRequest
from app.services.fund_service import perform_transfer
from app.core.database import get_db

router = APIRouter()

@router.post("/", summary="Transfer source fund to target fund")
def transfer_funds(request: TransferRequest, db: Session = Depends(get_db)):
    try:
        return perform_transfer(
            db,
            policy_number=request.policy_number,
            source_fund=request.source_fund,
            target_fund=request.target_fund,
            date=request.effective_date
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))