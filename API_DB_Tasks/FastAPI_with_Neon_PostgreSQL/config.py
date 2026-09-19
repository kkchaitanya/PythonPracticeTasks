from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn, field_validator

class Settings(BaseSettings):
    # 1. Keep this as PostgresDsn for strict URL structure validation
    DATABASE_URL: PostgresDsn

    # 2. Add a computed property to force the async prefix string
    @property
    def ASYNC_DATABASE_URL(self) -> str:
        url = self.DATABASE_URL.unicode_string()
        # Force asyncpg if Pydantic accidentally stripped it out
        if url.startswith("postgresql://"):
            return url.replace("postgresql://", "postgresql+asyncpg://", 1)
        elif url.startswith("postgres://"):
            return url.replace("postgres://", "postgresql+asyncpg://", 1)
        return url

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
