#!/bin/sh

echo "starting app"
sleep 10

echo "start migration"
poetry run flask db upgrade

echo "migration done"

gunicorn wsgi:app