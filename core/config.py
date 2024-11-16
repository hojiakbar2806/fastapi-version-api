import dotenv
import logging
from pydantic.v1 import Field
from typing import Dict, Optional
from pydantic_settings import BaseSettings

# Load .env file
dotenv.load_dotenv()

# General environment settings


class Environment(BaseSettings):
    env: str

# Database settings


class Database(BaseSettings):
    db_sqlite_filename: str
    db_host: str
    db_port: int
    db_user: str
    db_pass: str
    db_name: str

# JWT settings


class JWTAuth(BaseSettings):
    jwt_secret: str
    jwt_algo: str
    jwt_access_expire: int
    jwt_refresh_expire: int

# Centralized settings class


class Settings(BaseSettings):
    environment: Environment = Environment()
    db: Database = Database()
    jwt_auth: JWTAuth = JWTAuth()

    @property
    def sqlalchemy_url(self) -> Optional[str]:
        if self.environment.env == "development":
            return f"sqlite+aiosqlite:///{self.db.db_sqlite_filename}"
        elif self.environment.env == "production":
            return f"postgresql+asyncpg://{self.db.db_user}:{self.db.db_pass}@{self.db.db_host}:{self.db.db_port}/{self.db.db_name}"
        return None


# Create settings object
settings = Settings()

# Print SQLAlchemy URL to verify
print(settings.sqlalchemy_url)
