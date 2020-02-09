from .base import *
import dj_database_url

# https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['mentorpaired.herokuapp.com', 'mentorpaired-staging.herokuapp.com']

DEBUG = os.getenv('DEBUG')


# https://help.heroku.com/J2R1S4T8/can-heroku-force-an-application-to-use-ssl-tls
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# https://devcenter.heroku.com/articles/python-concurrency-and-database-connections
DATABASES = {
    'default' : dj_database_url.config(conn_max_age=600, ssl_require=True)
}
