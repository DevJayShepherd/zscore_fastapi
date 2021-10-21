from pydantic import BaseModel
from datetime import date


class ReportCreate(BaseModel):
    company: str
    iso_code: str
    year: int
    score: float
    report_date: date

    class Config:
        orm_mode = True
