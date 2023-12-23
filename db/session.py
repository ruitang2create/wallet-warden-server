from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = (
    os.getenv("DB_SYSTEM") + "+"
    + os.getenv("DB_DRIVER") + "://"
    + os.getenv("DB_USER") + ":"
    + os.getenv("DB_PASSWORD") + "@"
    + os.getenv("DB_HOST") + ":"
    + os.getenv("DB_PORT") + "/"
    + os.getenv("DB_NAME")
)
engine = create_engine(DB_URL, echo=True)
LocalSession = sessionmaker(bind=engine)

