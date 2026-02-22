#settings/settings.py
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    BOT_TOKEN: str
    GOOGLE_CREDENTIALS_PATH: str
    GOOGLE_SHEET_NAME: str

settings = Settings()