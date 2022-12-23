from pydantic import BaseSettings

class Settings(BaseSettings):
    MONGO_USER: str
    MONGO_PASS: str
    MONGO_DB: str

    class Config:
        env_file = './env'



settings = Settings()