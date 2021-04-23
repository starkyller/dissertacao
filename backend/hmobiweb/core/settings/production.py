from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^^(oi_x-*%o-w4d!gbb=@6741#&jft&p-)b$zqcc2b5+6x9r9k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database_name_here',
        'USER': 'username_here',
        'PASSWORD': 'password_here',
        'HOST': 'ip_or_domain_here',     
        'PORT': 5432,
        'CONN_MAX_AGE': 50
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': True,
        },
        'django.template': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': True,
        },
        'django.django.security': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': True,
        }

    },
}