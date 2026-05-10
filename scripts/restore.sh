#!/bin/bash

BACKUP_FILE=$1

echo "restoring database..."

psql \
-U postgres \
-d bookinghub \
< $BACKUP_FILE

echo "restore completed"