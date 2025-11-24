from fastapi import Depends, HTTPException
from .init_db import SessionLocal
from sqlalchemy.orm import Session, sessionmaker
from ..models.user import User
from jose import jwt, JWTError
from src.app.main import SECRET_KEY, ALGORITHM
from src.app.main import oauth2_schema

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_token(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    try:
        info = jwt.decode(token, SECRET_KEY, ALGORITHM)
        user_id = int(info.get("sub"))
    except JWTError:
        raise HTTPException(401, "acesso negado, verifique a validade do token")
    user = db.query(User).filter(User.id==user_id).first()
    if not user:
        raise HTTPException(401, "acesso negado")
    return user
    
    