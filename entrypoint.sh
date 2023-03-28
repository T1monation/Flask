#!/bin/sh

echo "starting app"
sleep 20

echo "start migration"
poetry run flask db upgrade

echo "migration done"

gunicorn wsgi:app