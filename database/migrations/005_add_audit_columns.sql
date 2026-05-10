ALTER TABLE customers
ADD COLUMN updated_at TIMESTAMP;


ALTER TABLE flights
ADD COLUMN updated_at TIMESTAMP;


ALTER TABLE hotels
ADD COLUMN updated_at TIMESTAMP;


ALTER TABLE payments
ADD COLUMN updated_at TIMESTAMP;


ALTER TABLE flight_reservations
ADD COLUMN updated_at TIMESTAMP;


ALTER TABLE hotel_reservations
ADD COLUMN updated_at TIMESTAMP;