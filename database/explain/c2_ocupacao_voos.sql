EXPLAIN ANALYZE
SELECT
    f.flight_number,

    f.total_seats,

    SUM(fr.seats_reserved) AS occupied_seats,

    (
        SUM(fr.seats_reserved)::DECIMAL
        / f.total_seats
    ) * 100 AS occupancy_rate

FROM flights f

INNER JOIN flight_reservations fr
    ON fr.flight_id = f.id

GROUP BY
    f.id,
    f.flight_number,
    f.total_seats

ORDER BY occupancy_rate DESC;