CREATE INDEX idx_flights_origin_destination
ON flights (
    origin_airport_id,
    destination_airport_id
);

CREATE INDEX idx_flight_reservations_customer
ON flight_reservations(customer_id);

CREATE INDEX idx_payments_status
ON payments(status);

CREATE INDEX idx_payments_created_at
ON payments(created_at);

