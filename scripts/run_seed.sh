#!/bin/bash

echo "running database seed..."

cd database/seed

python seed.py

echo "seed completed successfully"