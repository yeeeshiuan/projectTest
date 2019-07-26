from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.sessions.models import Session


class User(AbstractUser):
    pass

class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session = models.OneToOneField(Session, on_delete=models.CASCADE)
