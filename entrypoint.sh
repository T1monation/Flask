#!/bin/sh

flask db upgrade

gunicorn wsgi:app