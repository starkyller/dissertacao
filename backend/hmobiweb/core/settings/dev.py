from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^^(oi_x-*%o-w4d!gbb=@6741#&jft&p-)b$zqcc2b5+6x9r9k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DEV_APPS = [
    'django_extensions',
]

INSTALLED_APPS += DEV_APPS


GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}