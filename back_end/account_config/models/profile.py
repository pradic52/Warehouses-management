from django.db import models

class Profile(models.Model):
    user = models.OneToOneField("account_config.User", on_delete=models.CASCADE)
    bio = models.TextField()