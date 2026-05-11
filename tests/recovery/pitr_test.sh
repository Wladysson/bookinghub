#!/bin/bash

echo "creating recovery restore point..."

psql -h localhost -U booking -d bookinghub -c \
"SELECT pg_create_restore_point('before_massive_payment');"

echo "restore point created"

echo "executing transactional changes..."

psql -h localhost -U booking -d bookinghub <<EOF

UPDATE flights
SET available_seats = available_seats - 5
WHERE id = 1;

EOF

echo "PITR simulation completed"