from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "MetaForge API"
    environment: str = "development"


settings = Settings()
