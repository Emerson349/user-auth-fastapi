from fastapi import APIRouter, Depends, HTTPException
from src.app.config import ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY
from sqlalchemy.orm import Session
from src.models.user import User
from src.db.dependencies import get_db, verify_token
from src.app.schemas import User_create, User_read, Login
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordRequestForm


auth_route = APIRouter(prefix="/auth", tags=["auth"])

def create_token(user_id: int, token_time = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    #jwt
    expirate_time = datetime.now(timezone.utc) + token_time

    info = {
        "sub": str(user_id),
        "exp": expirate_time
    }
    encoded_jwt = jwt.encode(info, SECRET_KEY, ALGORITHM)
    return encoded_jwt

@auth_route.post("/create")
async def create_account(user_create: User_create, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email==user_create.email).first()
    if user:
        raise HTTPException(409, "email ja cadastrado")
    
    new_user = User(user_create.name, user_create.email, user_create.password)
    db.add(new_user) 
    db.commit()
    return {"mensagem": f"usuario cadastrado com sucesso {user_create.email}"}

@auth_route.get("/", response_model=list[User_read])
async def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@auth_route.post("/login")
async def login(login_schema: Login, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == login_schema.email).first()
    if not user or user.password != login_schema.password:
        raise HTTPException(401, "Email ou senha incorretos")
    
    access_token = create_token(user.id)
    refresh_token = create_token(user.id, token_time=timedelta(days=7))
    return {
        "access_token": access_token,
        "token_type": "Bearer",
        "refresh_token": refresh_token
    }

@auth_route.post("/login-form")
async def login_form(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or user.password != form_data.password:
        raise HTTPException(401, "Email ou senha incorretos")
    
    access_token = create_token(user.id)
    return {
        "access_token": access_token,
        "token_type": "Bearer"
    }
    
@auth_route.get("/refresh")
async def use_refresh_token(user: User = Depends(verify_token)):
    # verificar o token
    access_token = create_token(user.id)
    return {
        "acess_token": access_token,
        "token_type": "Bearer"
    }