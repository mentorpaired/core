#!/bin/sh

cd /src

pip install -r requirements.txt
./manage.py migrate
DJANGO_SUPERUSER_PASSWORD=${SETUP_PASSWORD} python manage.py createsuperuser --username ${SETUP_USERNAME} --noinput --email ${SETUP_EMAIL}
echo "you can now log in using the username ${SETUP_USERNAME} and the password ${SETUP_PASSWORD}"

./manage.py runserver 0.0.0.0:8000
