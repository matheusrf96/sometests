import psycopg2
from psycopg2 import Error


def get_connection():
    try:
        return psycopg2.connect(
            user="postgres",
            password="",
            host="localhost",
            port="5432",
            database="pytest"
        )
    except (Exception, Error) as error:
        raise error
