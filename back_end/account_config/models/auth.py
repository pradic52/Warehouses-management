from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    # Add custom fields or methods here
    phone = PhoneNumberField()

