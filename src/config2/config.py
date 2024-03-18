import os
from config2.statics import static
# from .statics import static


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = "mysql://root:Password1!@localhost/ukituki_store_db"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    # SQLALCHEMY_DATABASE_URI = "sqlite:///ukituki_store.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = static
