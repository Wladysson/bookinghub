TOTAL_REVENUE = """
SELECT
    COALESCE(SUM(amount), 0) AS total_revenue
FROM payments
WHERE status = 'approved';
"""


TOTAL_RESERVATIONS = """
SELECT
    COUNT(*) AS total_reservations
FROM (
    SELECT id FROM flight_reservations
    UNION ALL
    SELECT id FROM hotel_reservations
    UNION ALL
    SELECT id FROM package_reservations
) reservations;
"""


TOP_DESTINATIONS = """
SELECT
    a.city,
    a.country,
    COUNT(fr.id) AS total_reservations
FROM flight_reservations fr
INNER JOIN flights f
    ON f.id = fr.flight_id
INNER JOIN airports a
    ON a.id = f.destination_airport_id
GROUP BY a.city, a.country
ORDER BY total_reservations DESC
LIMIT 10;
"""


HOTEL_OCCUPANCY = """
SELECT
    h.name,
    COUNT(hr.id) AS occupied_rooms
FROM hotel_reservations hr
INNER JOIN hotels h
    ON h.id = hr.hotel_id
WHERE hr.status = 'confirmed'
GROUP BY h.name
ORDER BY occupied_rooms DESC;
"""


PAYMENTS_BY_METHOD = """
SELECT
    payment_method,
    COUNT(*) AS total,
    COALESCE(SUM(amount), 0) AS total_amount
FROM payments
WHERE status = 'approved'
GROUP BY payment_method
ORDER BY total_amount DESC;
"""


MONTHLY_REVENUE = """
SELECT
    DATE_TRUNC('month', created_at) AS month,
    COALESCE(SUM(amount), 0) AS revenue
FROM payments
WHERE status = 'approved'
GROUP BY month
ORDER BY month;
"""