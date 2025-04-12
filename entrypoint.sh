#!/bin/bash

# Exit the script if any command fails
set -e

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Collect static files (optional, useful if using staticfiles in production)
# echo "Collecting static files..."
# python manage.py collectstatic --noinput

# Start the Django development server
echo "Starting server..."
exec "$@"
