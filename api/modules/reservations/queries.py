CREATE_FLIGHT_RESERVATION = """
INSERT INTO flight_reservations (
    customer_id,
    flight_id,
    status
)
VALUES (
    %s,
    %s,
    'confirmed'
)
RETURNING *;
"""


CREATE_HOTEL_RESERVATION = """
INSERT INTO hotel_reservations (
    customer_id,
    hotel_id,
    room_id,
    check_in,
    check_out,
    status
)
VALUES (
    %s,
    %s,
    %s,
    %s,
    %s,
    'confirmed'
)
RETURNING *;
"""


CREATE_PACKAGE_RESERVATION = """
INSERT INTO package_reservations (
    customer_id,
    flight_reservation_id,
    hotel_reservation_id,
    status
)
VALUES (
    %s,
    %s,
    %s,
    'confirmed'
)
RETURNING *;
"""


CREATE_SAVEPOINT = """
SAVEPOINT reservation_savepoint;
"""


ROLLBACK_TO_SAVEPOINT = """
ROLLBACK TO SAVEPOINT reservation_savepoint;
"""