### app/crud/fund_crud.py

from sqlalchemy.orm import Session
from app.models.fund_models import Fund, PolicyFund, FundPrice, FundAsset

# Get all available funds
def get_all_funds(db: Session):
    return db.query(Fund).all()

# Get specific fund by code
def get_fund_by_code(db: Session, fund_code: str):
    return db.query(Fund).filter(Fund.fund_code == fund_code).first()

# Get policy funds by policy number
def get_policy_funds(db: Session, policy_number: str):
    return db.query(PolicyFund).filter(PolicyFund.policy_number == policy_number).all()

# Get policy-fund by policy number and fund code
def get_policy_fund(db: Session, policy_number: str, fund_code: str):
    return db.query(PolicyFund).filter_by(policy_number=policy_number, fund_code=fund_code).first()

# Get fund price for a given fund and date
def get_fund_price(db: Session, fund_code: str, price_date):
    return db.query(FundPrice).filter_by(fund_code=fund_code, price_date=price_date).first()

# Update fund asset table for transfer

def update_fund_assets(db: Session, source_fund, target_fund, date, amount, source_units, target_units):
    src_asset = db.query(FundAsset).filter_by(fund_code=source_fund, price_date=date).first()
    tgt_asset = db.query(FundAsset).filter_by(fund_code=target_fund, price_date=date).first()

    if src_asset:
        src_asset.total_units -= source_units
        src_asset.total_asset_value -= amount

    if tgt_asset:
        tgt_asset.total_units += target_units
        tgt_asset.total_asset_value += amount