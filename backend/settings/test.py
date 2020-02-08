from .base import *

# Secret Key
SECRET_KEY = ''

# Debug
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# Replace 'USER' and 'PASSWORD' if you have username and password for your database 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}