from config.database import get_cursor

from modules.reservations import queries


class ReservationSavepoints:

    @staticmethod
    def create_savepoint(connection):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.CREATE_SAVEPOINT
            )

    @staticmethod
    def rollback_to_savepoint(connection):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.ROLLBACK_TO_SAVEPOINT
            )