### app/schemas/fund_schemas.py

from pydantic import BaseModel
from datetime import date
from typing import Optional

class TransferRequest(BaseModel):
    policy_number: str
    source_fund: str
    target_fund: str
    effective_date: date

class FundBase(BaseModel):
    fund_code: str
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True

class PolicyFundBase(BaseModel):
    policy_number: str
    fund_code: str
    fund_units: float
    income_units: float
    reinvest_units: float

    class Config:
        orm_mode = True