from pathlib import Path
from typing import Tuple, Type

from pydantic import BaseModel, Field
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
)
from pydanticutils import read_yaml
from typerutils import LogLevel

default_config = Path("haulsrv.yaml")


class ApiSettings(BaseModel):
    host: str = Field(default="0.0.0.0")
    port: int = Field(default=8080)
    enabled: bool = Field(default=True)


class UiSettings(BaseModel):
    host: str = Field(default="0.0.0.0")
    port: int = Field(default=8081)
    enabled: bool = Field(default=True)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="HAULSRV_", env_nested_delimiter="__")

    api: ApiSettings = Field(default_factory=ApiSettings)
    ui: UiSettings = Field(default_factory=UiSettings)
    log_level: LogLevel = Field(default=LogLevel.INFO)

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return env_settings, dotenv_settings, file_secret_settings, init_settings


def read_settings(config_path: Path) -> Settings:
    return read_yaml(config_path, Settings)
