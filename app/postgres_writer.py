# app/postgres_writer.py
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models_postgres import MarketSymbolORM
from app.models import MarketSymbol, BestLimit


def _market_symbol_to_dict(item: MarketSymbol) -> dict:
    blDs_serializable = [
        bl.model_dump() if isinstance(bl, BestLimit) else bl
        for bl in item.blDs
    ]

    return {
        "ins_code": item.insCode,
        "lva": item.lva,
        "lvc": item.lvc,
        "eps": item.eps,
        "pe": item.pe,
        "pmd": item.pmd,
        "pmo": item.pmo,
        "qtj": item.qtj,
        "pdv": item.pdv,
        "ztt": item.ztt,
        "qtc": item.qtc,
        "bv": item.bv,
        "pc": item.pc,
        "pcpc": item.pcpc,
        "pmn": item.pmn,
        "pmx": item.pmx,
        "py": item.py,
        "pf": item.pf,
        "pcl": item.pcl,
        "vc": item.vc,
        "csv": item.csv,
        "insID": item.insID,
        "pMax": item.pMax,
        "pMin": item.pMin,
        "ztd": item.ztd,
        "dEven": item.dEven,
        "hEven": item.hEven,
        "pClosing": item.pClosing,
        "iClose": item.iClose,
        "yClose": item.yClose,
        "pDrCotVal": item.pDrCotVal,
        "zTotTran": item.zTotTran,
        "qTotTran5J": item.qTotTran5J,
        "qTotCap": item.qTotCap,
        "blDs": blDs_serializable,
    }


def save_market_data_to_postgres(data: list[MarketSymbol]):
    """Insert new symbols or update existing symbols by insCode."""
    db: Session = SessionLocal()
    inserted_count = 0
    updated_count = 0

    try:
        for item in data:
            if isinstance(item, dict):
                item = MarketSymbol(**item)

            values = _market_symbol_to_dict(item)

            existing_record = (
                db.query(MarketSymbolORM)
                .filter(MarketSymbolORM.ins_code == item.insCode)
                .first()
            )

            if existing_record:
                for field, value in values.items():
                    setattr(existing_record, field, value)
                updated_count += 1
            else:
                record = MarketSymbolORM(**values)
                db.add(record)
                inserted_count += 1

        db.commit()
        print(
            f"✅ PostgreSQL upsert completed. "
            f"Inserted: {inserted_count}, Updated: {updated_count}"
        )

    except Exception as e:
        db.rollback()
        print("❌ Error saving to DB:", e)
        raise

    finally:
        db.close()