import logging

from config.settings import settings


def setup_logger():

    logging.basicConfig(
        level=settings.LOG_LEVEL,
        format=(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(name)s | "
            "%(message)s"
        )
    )

    return logging.getLogger("bookinghub")


logger = setup_logger()