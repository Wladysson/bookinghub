import psycopg2
from psycopg2.pool import SimpleConnectionPool
from psycopg2.extras import RealDictCursor

from config.settings import settings

connection_pool = SimpleConnectionPool(
    minconn=1,
    maxconn=20,
    host=settings.DATABASE_HOST,
    port=settings.DATABASE_PORT,
    dbname=settings.DATABASE_NAME,
    user=settings.DATABASE_USER,
    password=settings.DATABASE_PASSWORD
)


def get_connection():
    return connection_pool.getconn()


def release_connection(connection):
    connection_pool.putconn(connection)


def get_cursor(connection):
    return connection.cursor(cursor_factory=RealDictCursor)