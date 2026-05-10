from datetime import datetime


def validate_date_range(
    check_in: datetime,
    check_out: datetime
):

    if check_in >= check_out:
        raise ValueError(
            "check_out deve ser maior que check_in"
        )


def validate_positive_number(value):

    if value <= 0:
        raise ValueError(
            "Valor deve ser positivo"
        )