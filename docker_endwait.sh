#!/bin/bash

# Static files
echo "Collect static files"
#python manage.py collectstatic --noinput

# Apliquem les migracions corresponents
echo "Apply database migrations"
python manage.py makemigrations

python manage.py migrate

# Inciem el servidor
echo "Starting server"
gunicorn offerscraping.wsgi:application --bind 0.0.0.0:8000