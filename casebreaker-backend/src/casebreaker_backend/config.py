from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./casebreaker.db"
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "CaseBreaker"
    CLAUDE_API_KEY: str
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()
