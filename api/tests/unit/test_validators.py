from shared.utils.validators import (
    validate_email
)


def test_should_validate_valid_email():

    email = "cliente@email.com"

    result = validate_email(email)

    assert result is True


def test_should_reject_invalid_email():

    email = "cliente-email.com"

    result = validate_email(email)

    assert result is False