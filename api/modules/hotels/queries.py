GET_ALL_HOTELS = """
SELECT
    id,
    name,
    city,
    country,
    stars,
    address
FROM hotels
ORDER BY stars DESC, name;
"""


GET_HOTEL_BY_ID = """
SELECT
    id,
    name,
    city,
    country,
    stars,
    address
FROM hotels
WHERE id = %s;
"""


CREATE_HOTEL = """
INSERT INTO hotels (
    name,
    city,
    country,
    stars,
    address
)
VALUES (
    %s,
    %s,
    %s,
    %s,
    %s
)
RETURNING *;
"""


DELETE_HOTEL = """
DELETE FROM hotels
WHERE id = %s;
"""


CREATE_ROOM = """
INSERT INTO rooms (
    hotel_id,
    room_number,
    type,
    capacity,
    price_per_night
)
VALUES (
    %s,
    %s,
    %s,
    %s,
    %s
)
RETURNING *;
"""


GET_ROOMS_BY_HOTEL = """
SELECT
    id,
    hotel_id,
    room_number,
    type,
    capacity,
    price_per_night
FROM rooms
WHERE hotel_id = %s
ORDER BY room_number;
"""


GET_AVAILABLE_ROOMS = """
SELECT
    r.id,
    r.hotel_id,
    r.room_number,
    r.type,
    r.capacity,
    r.price_per_night
FROM rooms r
WHERE r.hotel_id = %s
AND r.id NOT IN (

    SELECT hr.room_id
    FROM hotel_reservations hr

    WHERE hr.status != 'cancelled'

    AND hr.check_in < %s
    AND hr.check_out > %s
)
ORDER BY r.room_number;
"""


LOCK_ROOM_FOR_UPDATE = """
SELECT
    id,
    hotel_id,
    room_number
FROM rooms
WHERE id = %s
FOR UPDATE;
"""