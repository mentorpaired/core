import os

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG")

ALLOWED_HOSTS = ["0.0.0.0", "localhost", "127.0.0.1"]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "DB_NAME"),
        "USER": os.getenv("POSTGRES_USER", "DB_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "DB_PASSWORD"),
        "HOST": os.getenv("DATABASE_HOST", "DB_HOST"),
        "PORT": os.getenv("DATABASE_PORT", "DB_PORT"),
    }
}
