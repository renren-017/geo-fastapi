from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGO_INITDB_DATABASE: str
    MONGO_INITDB_USERNAME: str
    MONGO_INITDB_PASSWORD: str
    MONGO_HOST: str
    MONGO_PORT: str

    class Config:
        env_file = '.env'


settings = Settings()
