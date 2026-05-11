#!/bin/bash

echo "simulating database crash..."

sudo systemctl stop postgresql

sleep 5

echo "starting PostgreSQL again..."

sudo systemctl start postgresql

echo "checking recovery status..."

psql -h localhost -U booking -d bookinghub -c \
"SELECT now();"

echo "crash recovery completed"