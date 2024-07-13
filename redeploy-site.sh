#!/bin/bash

# Navigate to the project directory
echo "Navigating to the project directory..."
cd /root/mlh-portfolio || { echo "Failed to navigate to project directory"; exit 1; }

# Fetch the latest changes from the main branch on GitHub
echo "Fetching the latest changes from the main branch..."
git fetch && git reset origin/main --hard || { echo "Failed to fetch and reset git repository"; exit 1; }

# Activate the Python virtual environment and install dependencies
echo "Activating the Python virtual environment..."
source /root/mlh-portfolio/python3-virtualenv/bin/activate || { echo "Failed to activate virtual environment"; exit 1; }

echo "Installing Python dependencies..."
pip install -r requirements.txt || { echo "Failed to install Python dependencies"; exit 1; }

# Restart myportfolio service
echo "Restarting myportfolio service..."
sudo systemctl restart myportfolio.service || { echo "Failed to restart myportfolio service"; exit 1; }

echo "Deployment completed successfully."
