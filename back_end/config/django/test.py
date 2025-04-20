from .base import *

DEBUG = False

# DB in-memory
DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
}

# Emails capturés en mémoire
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# Speed up les hashers
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# Désactiver la durée d’attente SMS pour tests
ACCOUNT_PHONE_VERIFICATION_TIMEOUT = 1
