

from fastapi import HTTPException
from api.models import User
from sqlalchemy.orm.session import Session

from db.db_schema import DBUser


def create_user(db: Session, user: User, token: str):
    new_user = DBUser(
        email=user.email,
        password=user.password,
        token=token
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)


def get_user(db: Session, email: str, token: str):
    user = db.query(DBUser).filter(DBUser.email == email).filter(
        DBUser.token == token).first()
    if not user:
        raise HTTPException(
            status_code=404, detail=f'User with email {email} not found')
    return user
