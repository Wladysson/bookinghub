from contextlib import contextmanager

from config.database import (
    get_connection,
    release_connection
)


@contextmanager
def transaction():

    connection = get_connection()

    try:

        yield connection

        connection.commit()

    except Exception:

        connection.rollback()
        raise

    finally:

        release_connection(connection)