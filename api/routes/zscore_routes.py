from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.db.session import get_db
from api.schema.zscore import ZScore, ZScoreList, ZScoreResponse

router = APIRouter()


@router.put('/get_zscore', response_model=ZScoreResponse)
def get_z_score(details: ZScoreList, db: Session = Depends(get_db)):
    details = details

    scores = {"scores": ['hello']}
    return scores




