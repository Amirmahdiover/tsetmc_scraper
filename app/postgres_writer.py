# app/postgres_writer.py
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models_postgres import MarketSymbolORM
from app.models import MarketSymbol, BestLimit

def save_market_data_to_postgres(data: list[MarketSymbol]):
    """Insert or update market data into PostgreSQL."""
    db: Session = SessionLocal()
    try:
        for item in data:

            if isinstance(item, dict):
                item = MarketSymbol(**item)
            blDs_serializable = [
                bl.model_dump() if isinstance(bl, BestLimit) else bl
                for bl in item.blDs
            ]
            record = MarketSymbolORM(
                
                ins_code=item.insCode,
                lva=item.lva,
                lvc=item.lvc,
                eps=item.eps,
                pe=item.pe,
                pmd=item.pmd,
                pmo=item.pmo,
                qtj=item.qtj,
                pdv=item.pdv,
                ztt=item.ztt,
                qtc=item.qtc,
                bv=item.bv,
                pc=item.pc,
                pcpc=item.pcpc,
                pmn=item.pmn,
                pmx=item.pmx,
                py=item.py,
                pf=item.pf,
                pcl=item.pcl,
                vc=item.vc,
                csv=item.csv,
                insID=item.insID,
                pMax=item.pMax,
                pMin=item.pMin,
                ztd=item.ztd,
                dEven=item.dEven,
                hEven=item.hEven,
                pClosing=item.pClosing,
                iClose=item.iClose,
                yClose=item.yClose,
                pDrCotVal=item.pDrCotVal,
                zTotTran=item.zTotTran,
                qTotTran5J=item.qTotTran5J,
                qTotCap=item.qTotCap,
                blDs=blDs_serializable,
            )
            db.add(record)

        db.commit()
        print(f"✅ Saved {len(data)} records to PostgreSQL.")
    except Exception as e:
        db.rollback()
        print("❌ Error saving to DB:", e)
    finally:
        db.close()
