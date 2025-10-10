from fastapi import FastAPI,Query
from app.fetcher import fetch_market_data
from typing import List, Optional
from app.models import MarketSymbol  # your Pydantic model
# --------------------------------------------------------

# Create tables in the database
from app.database import Base, engine
from app.models_postgres import MarketSymbolORM

# print("📦 Creating tables...")
Base.metadata.create_all(bind=engine)
# print("✅ Tables created successfully.")

# --------------------------------------------------------
app = FastAPI()

@app.get("/market-data", response_model=List[MarketSymbol])
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
    print(">>> market-data endpoint HIT")
    data = await fetch_market_data()
    print(">>> market-data endpoint DONE")
    # 🔍 Optional filter
    if ins_code:
        data = [item for item in data if item.insCode == ins_code]

    # 🔃 Optional sort
    reverse = order.lower() == "desc"
    try:
        data.sort(key=lambda x: getattr(x, sort_by), reverse=reverse)
    except AttributeError:
        pass  # ignore if field doesn't exist

    return data

# uvicorn app.main:app --reload




from fastapi import WebSocket
from app.socket_client import tsetmc_stream


@app.websocket("/ws/{ins_code}")
async def market_stream(websocket: WebSocket, ins_code: str):
    await websocket.accept()
    
    async for update in tsetmc_stream(ins_code):
        await websocket.send_json(update)