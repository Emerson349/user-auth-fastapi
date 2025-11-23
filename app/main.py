from fastapi import FastAPI
from .db.init_db import Base, engine
from .config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi.security import OAuth2PasswordBearer

from .models.user import User
from .models.order import Order
from .models.items import Item

oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login-form")

from .routes.auth_routes import auth_route
from .routes.order_routes import order_route

app = FastAPI()

app.include_router(auth_route)
app.include_router(order_route)

Base.metadata.create_all(bind=engine)

