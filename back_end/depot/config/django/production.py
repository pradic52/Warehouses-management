from .base import *
from config.env import env

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG", default=False)

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=[])
print("je suis là")
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("POSTGRES_DB", default="postgres"),
        'USER': env("POSTGRES_USER", default="postgres"),
        'PASSWORD': env("POSTGRES_PASSWORD", default="postgres"),
        'HOST': env("POSTGRES_HOST", default="localhost"),
        'PORT': env("POSTGRES_PORT", default="5432"),
    }

}