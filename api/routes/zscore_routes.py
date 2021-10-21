import datetime
from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from api.db.session import get_db
from api.schema.zscore import ZScoreList, ZScoreResponse
from api.utils.zscore_utils import get_capital, get_zscore
from api.db.crud.reports import create_report

router = APIRouter()


@router.put('/get_zscore', response_model=ZScoreResponse)
def get_z_score(details: ZScoreList, company: str, iso_code: str, db: Session = Depends(get_db)):
    scores = ['scores']
    # Iterate through the given data and calculate scores
    for record in details.financials:
        working_capital = get_capital(record.total_assets, record.total_liabilities)
        score = get_zscore(working_capital,
                           record.retained_earnings,
                           record.ebit,
                           record.equity,
                           record.sales,
                           record.total_assets,
                           record.total_liabilities)
        score_response = {'year': record.year, 'zscore': score}
        scores.append(score_response)

        # Prepare report for DB
        report = {'company': company, 'iso_code': iso_code, 'year': record.year, 'score': score,
                  'report_date': datetime.datetime.now().date()}

        # Attempt Upload of report to the DB
        report_upload = create_report(report, db)
        if not report_upload:
            raise HTTPException(status_code=404, detail="Unable to save report, double check details.")

    scores = jsonable_encoder(scores)
    return JSONResponse(content=scores)
