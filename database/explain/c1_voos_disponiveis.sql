EXPLAIN ANALYZE
SELECT
    f.id,
    f.flight_number,

    ao.city AS origin_city,
    ad.city AS destination_city,

    f.departure_time,
    f.available_seats,
    f.price

FROM flights f

INNER JOIN airports ao
    ON ao.id = f.origin_airport_id

INNER JOIN airports ad
    ON ad.id = f.destination_airport_id

WHERE
    ao.city = 'Fortaleza'
    AND ad.city = 'São Paulo'
    AND f.available_seats > 0

ORDER BY f.departure_time;