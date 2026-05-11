#!/bin/bash

echo "testing WAL generation..."

psql -h localhost -U booking -d bookinghub <<EOF

INSERT INTO payments (
    reservation_type,
    reservation_id,
    customer_id,
    amount,
    payment_method,
    status,
    transaction_id
)
VALUES (
    'flight',
    1,
    1,
    899.90,
    'pix',
    'approved',
    'wal-test-001'
);

EOF

echo "checking WAL position..."

psql -h localhost -U booking -d bookinghub -c \
"SELECT pg_current_wal_lsn();"

echo "WAL test completed"