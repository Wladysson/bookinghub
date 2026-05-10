CREATE VIEW vw_monthly_revenue AS
SELECT
    DATE_TRUNC('month', created_at) AS month,
    SUM(amount) AS revenue
FROM payments
WHERE status = 'approved'
GROUP BY month;

CREATE VIEW vw_top_destinations AS
SELECT
    a.city,
    a.country,
    COUNT(fr.id) AS reservations
FROM flight_reservations fr
INNER JOIN flights f
    ON f.id = fr.flight_id
INNER JOIN airports a
    ON a.id = f.destination_airport_id
GROUP BY a.city, a.country;

CREATE VIEW vw_hotel_occupancy AS
SELECT
    h.name,
    COUNT(hr.id) AS occupied_rooms
FROM hotel_reservations hr
INNER JOIN hotels h
    ON h.id = hr.hotel_id
GROUP BY h.name;

