from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models_postgres import MarketSymbolORM
from app.models import MarketSymbol, BestLimit

def read_market_data_from_postgres() -> list[MarketSymbol]:
    db: Session = SessionLocal()
    try:
        records = db.query(MarketSymbolORM).all()
        return [
            MarketSymbol(
                insCode=rec.ins_code,
                lva=rec.lva,
                lvc=rec.lvc,
                eps=rec.eps,
                pe=rec.pe,
                pmd=rec.pmd,
                pmo=rec.pmo,
                qtj=rec.qtj,
                pdv=rec.pdv,
                ztt=rec.ztt,
                qtc=rec.qtc,
                bv=rec.bv,
                pc=rec.pc,
                pcpc=rec.pcpc,
                pmn=rec.pmn,
                pmx=rec.pmx,
                py=rec.py,
                pf=rec.pf,
                pcl=rec.pcl,
                vc=rec.vc,
                csv=rec.csv,
                insID=rec.insID,
                pMax=rec.pMax,
                pMin=rec.pMin,
                ztd=rec.ztd,
                dEven=rec.dEven,
                hEven=rec.hEven,
                pClosing=rec.pClosing,
                iClose=rec.iClose,
                yClose=rec.yClose,
                pDrCotVal=rec.pDrCotVal,
                zTotTran=rec.zTotTran,
                qTotTran5J=rec.qTotTran5J,
                qTotCap=rec.qTotCap,

                # ✅ Convert each dict in blDs to a BestLimit object
                blDs=[
                    BestLimit(**bl) for bl in rec.blDs
                ] if rec.blDs else [],

                id=rec.id
            )
            for rec in records
        ]
    finally:
        db.close()
