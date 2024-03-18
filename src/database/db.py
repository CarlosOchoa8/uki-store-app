from flask_sqlalchemy import SQLAlchemy
import psycopg2
from psycopg2 import DatabaseError
from decouple import config


def get_connection():
    try:
        return psycopg2.connect(
            host=config("PGSQL_HOST"),
            password=config("PGSQL_PASSWORD"),
            user=config("PGSQL_USER"),
            database=config("PGSQL_NAME")
        )
    except DatabaseError as ex:
        raise ex


db = SQLAlchemy()
