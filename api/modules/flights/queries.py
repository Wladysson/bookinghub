GET_ALL_FLIGHTS = """
SELECT
    f.id,
    f.flight_number,
    f.origin_airport_id,
    f.destination_airport_id,
    a1.code AS origin_airport_code,
    a2.code AS destination_airport_code,
    f.departure_time,
    f.arrival_time,
    f.total_seats,
    f.available_seats,
    f.price
FROM flights f
JOIN airports a1
    ON a1.id = f.origin_airport_id
JOIN airports a2
    ON a2.id = f.destination_airport_id
ORDER BY f.departure_time;
"""


GET_FLIGHT_BY_ID = """
SELECT
    f.id,
    f.flight_number,
    f.origin_airport_id,
    f.destination_airport_id,
    a1.code AS origin_airport_code,
    a2.code AS destination_airport_code,
    f.departure_time,
    f.arrival_time,
    f.total_seats,
    f.available_seats,
    f.price
FROM flights f
JOIN airports a1
    ON a1.id = f.origin_airport_id
JOIN airports a2
    ON a2.id = f.destination_airport_id
WHERE f.id = %s;
"""


CREATE_FLIGHT = """
INSERT INTO flights (
    flight_number,
    origin_airport_id,
    destination_airport_id,
    departure_time,
    arrival_time,
    total_seats,
    available_seats,
    price
)
VALUES (
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s
)
RETURNING *;
"""


DELETE_FLIGHT = """
DELETE FROM flights
WHERE id = %s;
"""


GET_AVAILABLE_FLIGHTS = """
SELECT
    f.id,
    f.flight_number,
    a1.code AS origin_airport_code,
    a2.code AS destination_airport_code,
    f.departure_time,
    f.arrival_time,
    f.available_seats,
    f.price
FROM flights f
JOIN airports a1
    ON a1.id = f.origin_airport_id
JOIN airports a2
    ON a2.id = f.destination_airport_id
WHERE
    (%s IS NULL OR a1.city = %s)
AND (%s IS NULL OR a2.city = %s)
AND (%s IS NULL OR DATE(f.departure_time) = DATE(%s))
AND f.available_seats > 0
ORDER BY f.departure_time;
"""


LOCK_FLIGHT_FOR_UPDATE = """
SELECT
    id,
    available_seats
FROM flights
WHERE id = %s
FOR UPDATE;
"""


DECREMENT_AVAILABLE_SEATS = """
UPDATE flights
SET available_seats = available_seats - 1
WHERE id = %s;
"""