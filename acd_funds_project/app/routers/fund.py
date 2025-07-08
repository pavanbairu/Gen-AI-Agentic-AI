### app/routers/fund.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.fund_schemas import FundBase, PolicyFundBase
from app.core.database import get_db
from app.crud import fund_crud
from typing import List

router = APIRouter()

@router.get("/", response_model=List[FundBase])
def list_all_funds(db: Session = Depends(get_db)):
    return fund_crud.get_all_funds(db) 

@router.get("/policy/{policy_number}", response_model=List[PolicyFundBase])
def get_policy_fund_details(policy_number: str, db: Session = Depends(get_db)):
    data = fund_crud.get_policy_funds(db, policy_number)
    if not data:
        raise HTTPException(status_code=404, detail="No funds found for policy")
    return data