from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.auth.dependencies import get_current_user
from app.models.user import User

from app.api_keys.service import get_api_keys, regenerate_api_keys
from app.api_keys.schema import ApiKeyResponse

router = APIRouter(
    prefix="/api-keys",
    tags=["API Keys"]
)

@router.get("", response_model=ApiKeyResponse)
def my_api_keys(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    api_key = get_api_keys(db, current_user)

    if api_key is None:
        raise HTTPException(
            status_code=404,
            detail="API keys not found"
        )
    
    return api_key
@router.post(
    "/regenerate",
    response_model=ApiKeyResponse,
)
def regenerate_keys(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    api_key = regenerate_api_keys(
        db,
        current_user,
    )

    if api_key is None:
        raise HTTPException(
            status_code=404,
            detail="Merchant not found",
        )
    return api_key