#!/bin/bash

echo "starting BookingHub API..."

cd api

source ~/venv/bin/activate

uvicorn main:app \
--host 0.0.0.0 \
--port 8000 \
--reload