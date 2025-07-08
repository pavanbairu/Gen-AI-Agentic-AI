### app/models/fund_models.py

from sqlalchemy import Column, Integer, String, Float, Date
from app.core.database import Base

class Policy(Base):
    __tablename__ = "policies"
    id = Column(Integer, primary_key=True, index=True)
    policy_number = Column(String, unique=True, index=True)
    plan_code = Column(String)

class PolicyFund(Base):
    __tablename__ = "policy_funds"
    id = Column(Integer, primary_key=True, index=True)
    policy_number = Column(String, index=True)
    fund_code = Column(String, index=True)
    fund_units = Column(Float)
    income_units = Column(Float)
    reinvest_units = Column(Float)

class Fund(Base):
    __tablename__ = "funds"
    fund_code = Column(String, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)

class FundPrice(Base):
    __tablename__ = "fund_prices"
    id = Column(Integer, primary_key=True, index=True)
    fund_code = Column(String, index=True)
    price_date = Column(Date)
    price = Column(Float)

class FundAsset(Base):
    __tablename__ = "fund_assets"
    id = Column(Integer, primary_key=True, index=True)
    fund_code = Column(String, index=True)
    price_date = Column(Date)
    total_units = Column(Float)
    total_asset_value = Column(Float)