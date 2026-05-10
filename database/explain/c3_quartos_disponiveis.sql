EXPLAIN ANALYZE
SELECT
    h.id,
    h.name,
    h.city,

    h.available_rooms,

    h.price_per_night

FROM hotels h

WHERE
    h.city = 'Rio de Janeiro'
    AND h.available_rooms > 0

ORDER BY h.price_per_night;