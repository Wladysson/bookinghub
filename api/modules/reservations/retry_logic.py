from shared.utils.retry import (
    execute_with_retry
)


class ReservationRetryLogic:

    @staticmethod
    def execute(operation):

        return execute_with_retry(
            operation=operation,
            max_attempts=3
        )