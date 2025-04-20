from .base import *

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DB locale
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
}


# Emails → console ou MailHog
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# SMS → backend de dev (dummy)
# Tu peux créer un backend SMS qui écrit dans les logs