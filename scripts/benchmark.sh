#!/bin/bash

echo "running benchmarks..."

cd database/benchmarks

python benchmark_queries.py

echo "benchmark completed"