from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette import status

from app.api.users import get_db
from app.auth.jwt import create_access_token
from app.auth.security import verify_password
from app.models.user import User
from app.schemas.user import UserLogin

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db())):
    user = None

    if user_data.username:
        user = db.query(User).filter(User.username == user_data.username).first()
    elif user_data.email:
        user = db.query(User).filter(User.email == user_data.email).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )
    if not verify_password(user_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    access_token = create_access_token(data={"sub": str(user.id)})

    return {"access_token": access_token, "token_type": "bearer"}
