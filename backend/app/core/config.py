from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    MPESA_CONSUMER_KEY: str
    MPESA_CONSUMER_SECRET: str
    MPESA_SHORTCODE: str
    MPESA_PASSKEY: str
    MPESA_CALLBACK_URL: str
    MPESA_ENV: str = "sandbox"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()