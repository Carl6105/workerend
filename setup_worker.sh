#!/bin/bash

# Ensure script runs with one argument (Main Server IP)
if [ $# -ne 1 ]; then
    echo "❌ Usage: bash setup_worker.sh <MAIN_SERVER_IP>"
    exit 1
fi

MAIN_SERVER_IP=$1

echo "📡 Connecting to Ray Cluster at $MAIN_SERVER_IP..."
export MAIN_SERVER_IP

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Start worker node
echo "🚀 Starting Worker Node..."
python workers/worker.py