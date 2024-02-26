#!/bin/bash
lsof -t -i tcp:8000 | xargs kill -9
PYTHONUNBUFFERED='1'
DJANGO_SETTINGS_MODULE='django_les_portes_sombres.settings'
source venv/bin/activate
python3 -m pip install -r config/requirements.txt
cp -f config/test/settings.py .
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000 --noreload &

