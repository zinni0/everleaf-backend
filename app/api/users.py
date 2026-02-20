from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.auth.jwt import create_access_token
from app.core.database import SESSION_LOCAL
from app.crud.user import create_user, get_current_user, oauth2_scheme
from app.models.user import User
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
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists"
        )
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Email already exists")

    new_user = create_user(db, user)

    access_token = create_access_token(data={"sub": str(new_user.id)})

    return {
        "id": new_user.id,
        "username": new_user.username,
        "email": new_user.email,
        "is_admin": new_user.is_admin,
        "access_token": access_token,
        "token_type": "bearer",
    }


@router.get("/me", response_model=UserRead)
def read_users_me(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return get_current_user(db, token)
