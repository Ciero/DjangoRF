#!/usr/bin/env bash
rm -rf /frontend-build/*
cp -r /frontend/dist/* /frontend-build
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000
