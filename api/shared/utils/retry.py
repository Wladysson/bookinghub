import random
import time

import psycopg2

from config.logging import logger


def execute_with_retry(
    operation,
    max_attempts=3
):

    for attempt in range(max_attempts):

        try:
            return operation()

        except psycopg2.errors.SerializationFailure as error:

            if attempt == max_attempts - 1:
                logger.error(
                    "Falha de serialização após máximo de tentativas"
                )
                raise error

            wait_time = (
                (2 ** attempt) * 0.1
                + random.uniform(0, 0.05)
            )

            logger.warning(
                f"Serialization failure. "
                f"Tentando novamente em {wait_time:.2f}s"
            )

            time.sleep(wait_time)