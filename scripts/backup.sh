#!/bin/bash

BACKUP_DIR="database/backups/logical"

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

FILE_NAME="bookinghub_$TIMESTAMP.sql"

echo "creating backup..."

pg_dump \
-U postgres \
bookinghub \
> $BACKUP_DIR/$FILE_NAME

echo "backup completed:"
echo "$BACKUP_DIR/$FILE_NAME"