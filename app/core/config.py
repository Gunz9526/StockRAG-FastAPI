from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "StockRAG-FastAPI"
    GOOGLE_API_KEY: str
    DATABASE_URL: str

    EMBEDDING_MODEL : str = "models/text-embedding-004"
    LLM_MODEL : str = "gemini-2.5-flash"

    TRADING_SYSTEM_URL: str = "http://host.docker.internal:8000"

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    class Config:
        env_file = ".env"

settings = Settings()