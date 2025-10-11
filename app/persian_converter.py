from app.models import MarketSymbol  # your Pydantic model


# this is for converting data keys to persian and using it returning with "market-data"
KEY_MAP = {
    "lvc": "نام",
    "lva": "نماد",
    "eps": "EPS",
    "pe": "P/E",
    "pmn": "کمترین",
    "pmx": "بیشترین",
    "pc": "تغییر",
    "pcpc": "درصد",
    "pcl": "پایانی",
    "pdv": "آخرین",
    "pf": "اولین",
    "py": "دیروز",
    "pDrCotVal": "ارزش",
    "ztd": "حجم",
    "ztt": "تعداد",
    "pmd": "خرید",
    "pmo": "فروش"
}

def to_persian_dict(model: MarketSymbol) -> dict:
    original = model.model_dump()
    return {KEY_MAP.get(k, k): v for k, v in original.items()}