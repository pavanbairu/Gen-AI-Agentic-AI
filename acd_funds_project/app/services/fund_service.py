### app/services/fund_service.py

from sqlalchemy.orm import Session
from app.crud import fund_crud
from app.models.fund_models import PolicyFund

def perform_transfer(db: Session, policy_number: str, source_fund: str, target_fund: str, date):
    # Fetch source policy-fund record
    policy_fund = fund_crud.get_policy_fund(db, policy_number, source_fund)
    if not policy_fund:
        raise Exception("Source fund not found for the given policy")

    source_units = policy_fund.fund_units

    src_price = fund_crud.get_fund_price(db, source_fund, date)
    tgt_price = fund_crud.get_fund_price(db, target_fund, date)

    if not src_price or not tgt_price:
        raise Exception("Missing price data for source or target fund")

    amount = source_units * src_price.price
    target_units = amount / tgt_price.price

    # Set source fund units to zero
    policy_fund.fund_units = 0

    # Update target fund units
    target_fund_rec = fund_crud.get_policy_fund(db, policy_number, target_fund)
    if target_fund_rec:
        target_fund_rec.fund_units += target_units
    else:
        new_fund = PolicyFund(
            policy_number=policy_number,
            fund_code=target_fund,
            fund_units=target_units,
            income_units=0.0,
            reinvest_units=0.0
        )
        db.add(new_fund)

    fund_crud.update_fund_assets(
        db, source_fund, target_fund, date, amount, source_units, target_units
    )

    db.commit()
    return {"message": "Transfer successful"}