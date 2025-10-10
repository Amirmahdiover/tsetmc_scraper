# app/models_postgres.py

from sqlalchemy import Column, Integer, String, Float, Boolean, JSON
from app.database import Base

class MarketSymbolORM(Base):
    __tablename__ = "market_symbols"

    id = Column(Integer, primary_key=True, index=True)
    ins_code = Column(String, index=True)
    lva = Column(String)
    lvc = Column(String)
    
    eps = Column(Float, nullable=True)
    pe = Column(Float, nullable=True)
    pmd = Column(Float, nullable=True)
    pmo = Column(Float, nullable=True)
    qtj = Column(Float, nullable=True)
    pdv = Column(Float, nullable=True)
    ztt = Column(Float, nullable=True)
    qtc = Column(Float, nullable=True)
    bv = Column(Float, nullable=True)
    pc = Column(Float, nullable=True)
    pcpc = Column(Float, nullable=True)
    pmn = Column(Float, nullable=True)
    pmx = Column(Float, nullable=True)
    py = Column(Float, nullable=True)
    pf = Column(Float, nullable=True)
    pcl = Column(Float, nullable=True)

    vc = Column(Integer)
    csv = Column(String)
    insID = Column(String)
    pMax = Column(Float, nullable=True)
    pMin = Column(Float, nullable=True)
    ztd = Column(Float, nullable=True)

    dEven = Column(Integer)
    hEven = Column(Integer)

    pClosing = Column(Float, nullable=True)
    iClose = Column(Boolean)
    yClose = Column(Boolean)
    pDrCotVal = Column(Float, nullable=True)
    zTotTran = Column(Float, nullable=True)
    qTotTran5J = Column(Float, nullable=True)
    qTotCap = Column(Float, nullable=True)
    blDs = Column(JSON, nullable=True)