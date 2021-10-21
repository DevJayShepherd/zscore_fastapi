from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from api.db.session import get_db
from api.schema.zscore import ZScore, ZScoreList, ZScoreResponse
from api.utils.zscore_utils import get_capital, get_zscore

router = APIRouter()


@router.put('/get_zscore', response_model=ZScoreResponse)
def get_z_score(details: ZScoreList, db: Session = Depends(get_db)):
    scores = ['scores']
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
    scores = jsonable_encoder(scores)
    return JSONResponse(content=scores)
