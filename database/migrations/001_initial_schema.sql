CREATE TABLE customers (
    id BIGSERIAL PRIMARY KEY,

    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,

    email VARCHAR(255) NOT NULL UNIQUE,

    phone VARCHAR(30),

    document_number VARCHAR(50) NOT NULL UNIQUE,

    nationality VARCHAR(100),

    created_at TIMESTAMP DEFAULT NOW()
);


CREATE TABLE airports (
    id BIGSERIAL PRIMARY KEY,

    code VARCHAR(10) NOT NULL UNIQUE,

    name VARCHAR(255) NOT NULL,

    city VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,

    created_at TIMESTAMP DEFAULT NOW()
);


CREATE TABLE flights (
    id BIGSERIAL PRIMARY KEY,

    flight_number VARCHAR(20) NOT NULL UNIQUE,

    origin_airport_id BIGINT NOT NULL,
    destination_airport_id BIGINT NOT NULL,

    departure_time TIMESTAMP NOT NULL,
    arrival_time TIMESTAMP NOT NULL,

    total_seats INTEGER NOT NULL,
    available_seats INTEGER NOT NULL,

    price NUMERIC(12,2) NOT NULL,

    created_at TIMESTAMP DEFAULT NOW(),

    CONSTRAINT fk_origin_airport
        FOREIGN KEY (origin_airport_id)
        REFERENCES airports(id),

    CONSTRAINT fk_destination_airport
        FOREIGN KEY (destination_airport_id)
        REFERENCES airports(id)
);


CREATE TABLE hotels (
    id BIGSERIAL PRIMARY KEY,

    name VARCHAR(255) NOT NULL,

    city VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,

    total_rooms INTEGER NOT NULL,
    available_rooms INTEGER NOT NULL,

    price_per_night NUMERIC(12,2) NOT NULL,

    created_at TIMESTAMP DEFAULT NOW()
);


CREATE TABLE flight_reservations (
    id BIGSERIAL PRIMARY KEY,

    customer_id BIGINT NOT NULL,
    flight_id BIGINT NOT NULL,

    seats_reserved INTEGER NOT NULL,

    total_price NUMERIC(12,2) NOT NULL,

    status VARCHAR(50) NOT NULL,

    created_at TIMESTAMP DEFAULT NOW(),

    CONSTRAINT fk_flight_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(id),

    CONSTRAINT fk_flight
        FOREIGN KEY (flight_id)
        REFERENCES flights(id)
);


CREATE TABLE hotel_reservations (
    id BIGSERIAL PRIMARY KEY,

    customer_id BIGINT NOT NULL,
    hotel_id BIGINT NOT NULL,

    rooms_reserved INTEGER NOT NULL,

    check_in DATE NOT NULL,
    check_out DATE NOT NULL,

    total_price NUMERIC(12,2) NOT NULL,

    status VARCHAR(50) NOT NULL,

    created_at TIMESTAMP DEFAULT NOW(),

    CONSTRAINT fk_hotel_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(id),

    CONSTRAINT fk_hotel
        FOREIGN KEY (hotel_id)
        REFERENCES hotels(id)
);


CREATE TABLE payments (
    id BIGSERIAL PRIMARY KEY,

    reservation_type VARCHAR(50) NOT NULL,

    reservation_id BIGINT NOT NULL,

    customer_id BIGINT NOT NULL,

    amount NUMERIC(12,2) NOT NULL,

    payment_method VARCHAR(50) NOT NULL,

    status VARCHAR(50) NOT NULL,

    transaction_id UUID NOT NULL UNIQUE,

    created_at TIMESTAMP DEFAULT NOW(),

    CONSTRAINT fk_payment_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(id)
);

