from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    # Redis
    REDIS_URL:str = "redis://localhost:6379"

    # Allowed hosts
    ALLOWED_HOSTS: list[str] = [
        "localhost",
        "127.0.0.1",
    ]

    # CORS
    CORS_ORIGINS: list[AnyHttpUrl] = [
        "http://localhost",
        "http://127.0.0.1",
    ]

    # REQUESTS
    ALLOWED_REQUEST_TYPES:list[str] = ["GET"]
    ALLOWED_REQUEST_HEADERS:list[str] = ["*"]

    # IP2Location DB path
    IP2LOCATION_DB: str = str(
        pathlib.Path(BASE_DIR, "ip2location", "IP2LOCATION-LITE-DB11.IPV6.BIN", "IP2LOCATION-LITE-DB11.IPV6.BIN")
    )

    # Static files folder
    STATIC_DIR: str = str(pathlib.Path(BASE_DIR, "static"))

    # Templates folder
    TEMPLATES_DIR: str = str(pathlib.Path(BASE_DIR, "templates"))

settings = Settings()