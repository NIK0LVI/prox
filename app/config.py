from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_HOSTNAME: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    DB_NAME_TEST: str
    USE_TEST_DB: bool

    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_FROM: str

    class Config:
        env_file = "./.env"


settings = Settings()
