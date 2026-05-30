import os

from pydantic_settings import BaseSettings, SettingsConfigDict

class HaloConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="HALO_",
        env_file=f".env.{os.getenv('HALO_ENV','dev')}")

    base_url: str
    client_id: str
    client_secret: str
    scope: str = "all"
    grant_type: str = "client_credentials"

