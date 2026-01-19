from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # API Config
    API_TITLE: str = "Calorie Tracker API"
    API_VERSION: str = "1.0.0"

    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:8080"
    ]

settings = Settings()