from typing import Any, Dict, List, Optional
from pydantic_settings import BaseSettings
from pydantic import HttpUrl, validator

class Settings(BaseSettings):

    PROJECT_NAME: str = "ESTETIKA"
    VERSION: str = "1.0.0"

    SENTRY_DSN: Optional[HttpUrl] = None

    API_PATH: str = ""

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    BACKEND_CORS_ORIGINS: List[str] = []

    FIREBASE_TYPE: Optional[str]
    FIREBASE_PROJECT_ID: Optional[str]
    FIREBASE_PRIVATE_KEY_ID: Optional[str]
    FIREBASE_PRIVATE_KEY: Optional[str]
    FIREBASE_CLIENT_EMAIL: Optional[str]
    FIREBASE_CLIENT_ID: Optional[str]
    FIREBASE_AUTH_URI: Optional[str]
    FIREBASE_TOKEN_URI: Optional[str]
    FIREBASE_AUTH_PROVIDER_X509_CERT_URL: Optional[str]
    FIREBASE_CLIENT_X509_CERT_URL: Optional[str]
    FIREBASE_UNIVERSAL_DOMAIN: Optional[str]
    FIREBASE: Optional[Dict[str, Any]]

    secret_key: str = "1AU9VD6-H8SzbknY5ORL7OCKV2pTP5RH4eWdzsM8f6k="
    algorithm: str = "HS256"

    @validator("FIREBASE", pre=True, always=True)
    def parse_firebase_json(cls, value, values):
        if isinstance(value, str):
            try:
                import json
                return json.loads(value)
            except json.JSONDecodeError:
                raise ValueError("Invalid JSON format for FIREBASE")
        return value

    class Config:
        env_file = ".env"

settings = Settings()