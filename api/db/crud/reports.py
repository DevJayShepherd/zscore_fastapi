from sqlalchemy.orm import Session
from sqlalchemy.exc import DataError

from api.db.models.scores import ScoreReport
from api.schema.report import ReportCreate


def create_report(report: ReportCreate, db: Session):
    try:
        the_report = ScoreReport(company=report['company'],
                                 iso_code=report['iso_code'],
                                 year=report['year'],
                                 score=report['score'],
                                 report_date=report['report_date'])
        db.add(the_report)
        db.commit()
        db.refresh(the_report)
    except DataError:
        return False

    return True
