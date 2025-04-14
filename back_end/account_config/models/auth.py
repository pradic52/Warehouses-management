from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # On supprime le champ username
    username = None

    # Email obligatoire et unique
    email = models.EmailField('email address', unique=True)

    # Téléphone optionnel mais unique
    phone_number = models.CharField('numéro de téléphone',
                                    max_length=20,
                                    unique=True,
                                    null=True,
                                    blank=True)

    # On utilisera l’email comme identifiant principal
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # pas d’autre champ requis
