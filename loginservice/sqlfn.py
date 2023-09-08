from sqlalchemy.orm import Session
from argon2 import PasswordHasher

from models import User

def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: User):
    ph = PasswordHasher()
    hash = ph.hash(user.password)
    db_user = User(username=user.username, password=hash)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def verify_password(plain_password, hashed_password):
    ph = PasswordHasher()
    try:
        ph.verify(hashed_password, plain_password)
        return True
    except:
        return False