import os

from dotenv.main import load_dotenv


load_dotenv()


class Config:
    PORT: str | None = os.getenv("PORT", None)
    HOST: str | None = os.getenv("HOST", None)

    NAME_DB: str | None = os.getenv("NAME_DB", None)
    USER_DB: str | None = os.getenv("USER_DB", None)
    PASSWORD_DB: str | None = os.getenv("PASSWORD_DB", None)
    HOST_DB: str | None = os.getenv("HOST_DB", None)
    PORT_DB: str | None = os.getenv("PORT_DB", None)

    DJANGO_SETTINGS_MODULE: str | None = os.getenv("projects.settings", None)
