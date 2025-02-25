from functools import lru_cache
from pathlib import Path

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


# class ServiceConfig(BaseModel):
#     host: str
#     port: int


class TgConfig(BaseModel):
    bot_token: str


class PostgresConfig(BaseModel):
    user: str
    password: str
    host: str
    port: int
    database: str
    schema_: str = Field(alias="schema")
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    @property
    def async_url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

    @property
    def sync_url(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


class Settings(BaseSettings):
    tg: TgConfig
    postgres: PostgresConfig

    model_config = SettingsConfigDict(
        env_file=(
            Path(__file__).resolve().parent.parent.parent / ".env",
            Path(__file__).resolve().parent.parent.parent / ".env.template",
        ),
        case_sensitive=False,
        env_nested_delimiter="__",
        extra="allow",
    )


app_settings = Settings()


@lru_cache
def get_settings():
    return app_settings
