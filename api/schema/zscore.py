from typing import Optional, List
from pydantic import BaseModel


class ZScore(BaseModel):
    year: int
    ebit: float
    equity: float
    retained_earnings: float
    sales: float
    total_assets: float
    total_liabilities: float


class ZScoreList(BaseModel):
    financials: List[ZScore]


class ZScoreResponse(BaseModel):
    scores: List
