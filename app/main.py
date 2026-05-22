from fastapi import FastAPI, Query, HTTPException
from app.fetcher import fetch_market_data
from typing import List, Optional
from app.models import MarketSymbol  # your Pydantic model
from app.persian_converter import to_persian_dict
# --------------------------------------------------------

# Create tables in the database
from app.database import Base, engine
from app.models_postgres import MarketSymbolORM

# print("📦 Creating tables...")
Base.metadata.create_all(bind=engine)
# print("✅ Tables created successfully.")

# --------------------------------------------------------




app = FastAPI()

@app.get("/market-data")
async def get_market_data_api(
    sort_by: Optional[str] = Query(
        default="vc",
        description="Field to sort by (e.g. vc, pe, pClosing, pcl, etc.)"
    ),
    order: Optional[str] = Query(
        default="desc",
        description="Sort direction: asc (low to high) or desc (high to low)",
        regex="^(asc|desc)$"
    ),
    ins_code: Optional[str] = Query(
        default=None,
        description="Optional insCode to filter by instrument"
    )
):
    data = await fetch_market_data()

    if ins_code:
        data = [item for item in data if item.insCode == ins_code]

    allowed_sort_fields = {
        "eps", "pe", "pmd", "pmo", "qtj", "pdv", "ztt", "qtc", "bv",
        "pc", "pcpc", "pmn", "pmx", "py", "pf", "pcl", "vc",
        "pMax", "pMin", "ztd", "pClosing", "pDrCotVal",
        "zTotTran", "qTotTran5J", "qTotCap"
    }

    if sort_by not in allowed_sort_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sort_by field. Allowed fields: {sorted(allowed_sort_fields)}"
        )

    reverse = order.lower() == "desc"

    non_null_items = [
        item for item in data
        if getattr(item, sort_by, None) is not None
    ]

    null_items = [
        item for item in data
        if getattr(item, sort_by, None) is None
    ]

    non_null_items.sort(
        key=lambda x: getattr(x, sort_by),
        reverse=reverse
    )

    data = non_null_items + null_items

    return [to_persian_dict(d) for d in data]
# uvicorn app.main:app --reload




from fastapi import WebSocket
from app.socket_client import tsetmc_stream


@app.websocket("/ws")
async def market_stream(websocket: WebSocket, ins_code: str):
    await websocket.accept()
    
    async for update in tsetmc_stream(ins_code):
        await websocket.send_json(update)