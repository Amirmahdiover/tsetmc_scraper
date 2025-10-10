# app/models.py
from typing import List, Optional
from pydantic import BaseModel, field_validator

def _to_float_or_none(v):
    if v in (None, "-", ""):
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None

class BestLimit(BaseModel):
    n: int
    qmd: int
    zmd: int
    pmd: float
    pmo: float
    zmo: int
    qmo: int
    rid: int

class MarketSymbol(BaseModel):
    lva: str
    lvc: str

    # fields that might arrive as "-", "", "123.4", or real numbers
    eps: Optional[float] = None
    pe: Optional[float] = None
    pmd: Optional[float] = None
    pmo: Optional[float] = None
    qtj: Optional[float] = None
    pdv: Optional[float] = None
    ztt: Optional[float] = None
    qtc: Optional[float] = None
    bv: Optional[float] = None
    pc: Optional[float] = None
    pcpc: Optional[float] = None
    pmn: Optional[float] = None
    pmx: Optional[float] = None
    py: Optional[float] = None
    pf: Optional[float] = None
    pcl: Optional[float] = None

    vc: int
    csv: str
    insID: str
    pMax: Optional[float] = None
    pMin: Optional[float] = None
    ztd: Optional[float] = None

    blDs: List[BestLimit]
    id: int
    insCode: str
    dEven: int
    hEven: int

    pClosing: Optional[float] = None
    iClose: bool
    yClose: bool
    pDrCotVal: Optional[float] = None
    zTotTran: Optional[float] = None
    qTotTran5J: Optional[float] = None
    qTotCap: Optional[float] = None

    # one validator for all possibly-dirty float fields
    @field_validator(
        "eps","pe","pmd","pmo","qtj","pdv","ztt","qtc","bv","pc","pcpc",
        "pmn","pmx","py","pf","pcl","pMax","pMin","ztd","pClosing",
        "pDrCotVal","zTotTran","qTotTran5J","qTotCap",
        mode="before"
    )
    def normalize_float_fields(cls, v):
        return _to_float_or_none(v)
