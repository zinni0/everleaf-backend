from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SESSION_LOCAL
from app.crud.user import create_user, get_users
from app.schemas.user import UserCreate, UserRead

router = APIRouter(prefix="/users", tags=["users"])


# Dependency
def get_db():
    db = SESSION_LOCAL()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=UserRead)
def api_create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.get("/", response_model=list[UserRead])
def api_get_users(db: Session = Depends(get_db)):
    return get_users(db)
