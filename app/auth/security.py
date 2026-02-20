from passlib.context import CryptContext

from app.core.config import settings

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def hash_password(password: str) -> str:
    peppered = password + settings.PASSWORD_PEPPER
    return pwd_context.hash(peppered)


def verify_password(password: str, hashed_password: str) -> bool:
    peppered = password + settings.PASSWORD_PEPPER
    return pwd_context.verify(peppered, hashed_password)
