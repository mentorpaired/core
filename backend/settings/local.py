from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = []

# Database 
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


# Replace 'USER' and 'PASSWORD' if you have username and password for your database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}
