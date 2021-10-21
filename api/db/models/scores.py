from sqlalchemy import Column, Integer, String, Date, Float

from api.db.base_class import Base


class ScoreReport(Base):
    id = Column(Integer, primary_key=True)
    company = Column(String, max_length=255)
    iso_code = Column(String, max_length=2)
    year = Column(Integer, max_length=4)
    score = Column(Float, max_length=255)
    report_date = Column(Date)

