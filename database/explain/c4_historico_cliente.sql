EXPLAIN ANALYZE
SELECT
    c.first_name,
    c.last_name,

    fr.id AS reservation_id,

    f.flight_number,

    p.amount,
    p.status

FROM customers c

INNER JOIN flight_reservations fr
    ON fr.customer_id = c.id

INNER JOIN flights f
    ON f.id = fr.flight_id

INNER JOIN payments p
    ON p.customer_id = c.id

WHERE c.id = 1

ORDER BY fr.created_at DESC;