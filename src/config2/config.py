import os

from config2.statics import static

# from .statics import static


class AppConfig:
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = static
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "fidelito6080@gmail.com"
    MAIL_DEFAULT_SENDER = "fidelito6080@gmail.com"
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    JWT_SECRET_KEY = os.getenv("auth_secret_key")
