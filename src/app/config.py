from dotenv import load_dotenv
import os
from pathlib import Path

ENV_PATH = Path.cwd() / ".env"

load_dotenv(ENV_PATH)

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))