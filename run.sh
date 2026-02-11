#!/bin/bash

# Ensure .env exists
if [ ! -f .env ]; then
    echo "Creating .env from example..."
    cp .env.example .env
    echo "Please edit .env to add your GOOGLE_API_KEY!"
    exit 1
fi

# Create and activate virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Start Backend
echo "Starting Backend..."
uvicorn backend.main:app --reload --port 8000 &
BACKEND_PID=$!

sleep 5

# Start Frontend
echo "Starting Frontend..."
streamlit run frontend/app.py --server.port 8501

# Cleanup on exit
trap "kill $BACKEND_PID" EXIT
