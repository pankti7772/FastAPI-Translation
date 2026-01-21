#!/bin/bash

# Ensure we are in the project directory
cd "$(dirname "$0")"

# Check if .venv exists
if [ -d ".venv" ]; then
    echo "Activating virtual environment..."
    source .venv/bin/activate
else
    echo "Virtual environment not found. Please install dependencies first."
    exit 1
fi

echo "Starting Translation API locally..."
echo "You can access the Swagger UI at: http://localhost:8000/docs"
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
