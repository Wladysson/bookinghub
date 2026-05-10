CREATE INDEX idx_payments_customer
ON payments(customer_id);


CREATE INDEX idx_payments_status
ON payments(status);


CREATE INDEX idx_payments_transaction_id
ON payments(transaction_id);


CREATE INDEX idx_payments_created_at
ON payments(created_at);


CREATE INDEX idx_flight_reservations_customer
ON flight_reservations(customer_id);


CREATE INDEX idx_hotel_reservations_customer
ON hotel_reservations(customer_id);