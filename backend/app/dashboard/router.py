from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.dependencies import  get_current_user
from app.database.session import get_db
from app.models.user import User

from app.dashboard.service import get_dashboard
from app.dashboard.schema import DashboardResponse

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)

@router.get(
    "",
    response_model=DashboardResponse,
)
def dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    dashboard = get_dashboard(
        db,
        current_user,
    )

    if dashboard is None:
        raise HTTPException(
            status_code=404,
            detail="Merchant not found",
        )
    return dashboard