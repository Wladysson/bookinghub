ALTER TABLE flights
ADD CONSTRAINT fk_flights_origin_airport
FOREIGN KEY (origin_airport_id)
REFERENCES airports(id);

ALTER TABLE flights
ADD CONSTRAINT fk_flights_destination_airport
FOREIGN KEY (destination_airport_id)
REFERENCES airports(id);

ALTER TABLE customers
ADD CONSTRAINT uq_customers_email
UNIQUE(email);

ALTER TABLE customers
ADD CONSTRAINT uq_customers_document
UNIQUE(document_number);

ALTER TABLE flights
ADD CONSTRAINT chk_available_seats
CHECK (available_seats >= 0);

ALTER TABLE hotels
ADD CONSTRAINT chk_available_rooms
CHECK (available_rooms >= 0);

