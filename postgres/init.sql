CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

CREATE EXTENSION IF NOT EXISTS pgcrypto;


CREATE TABLE audit_logs (

    id SERIAL PRIMARY KEY,

    event_type VARCHAR(100),

    description TEXT,

    created_at TIMESTAMP DEFAULT NOW()
);


INSERT INTO audit_logs (
    event_type,
    description
)
VALUES (
    'SYSTEM_START',
    'BookingHub database initialized'
);