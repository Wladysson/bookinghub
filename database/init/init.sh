#!/bin/bash

set -e

echo "Executando migrations..."

psql -U booking -d bookinghub -f /migrations/001_initial_schema.sql
psql -U booking -d bookinghub -f /migrations/002_add_payment_indexes.sql
psql -U booking -d bookinghub -f /migrations/003_add_hotel_rating.sql
psql -U booking -d bookinghub -f /migrations/004_create_views.sql
psql -U booking -d bookinghub -f /migrations/005_add_audit_columns.sql
psql -U booking -d bookinghub -f /migrations/006_audit_logs.sql

echo "Banco configurado com sucesso."