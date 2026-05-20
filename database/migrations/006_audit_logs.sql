CREATE TABLE audit_logs (
    id SERIAL PRIMARY KEY,
    user_id INT,
    action TEXT,
    entity TEXT,
    entity_id INT,
    metadata JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);