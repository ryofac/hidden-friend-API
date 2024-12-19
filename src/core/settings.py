from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite+aiosqlite:///database.db"
    HASH_ALGORITHM: str = "H256"
    ACESS_TOKEN_EXPIRES_SECONDS: int = 9999
    REFRESH_TOKEN_EXPIRES_SECONDS: int = 99999


settings = Settings()
