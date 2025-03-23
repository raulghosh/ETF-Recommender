# llm/schemas/etf_schema.py
from pydantic import BaseModel, confloat, conint

class ETFBase(BaseModel):
    ticker: str
    aum: confloat(gt=100)  # > $100M
    expense_ratio: confloat(ge=0, le=1)  # 0-1%
    holdings: list[dict]

def validate_etf(json_path):
    data = json.load(open(json_path))
    try:
        ETFBase(**data)
        return True
    except ValidationError as e:
        logger.error(f"Validation failed: {e}")
        return False