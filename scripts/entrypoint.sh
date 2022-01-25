#!/bin/sh

set -e

python manage.py collectstatic --noinput

gunicorn --workers=2 --bind=0.0.0.0:8000 tapp.wsgi