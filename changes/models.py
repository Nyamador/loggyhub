from django.db import models
from django.conf import settings

user = settings.AUTH_USER_MODEL


class Log(models.Model):
    name = models.CharField(vebose_name="ChangeLog", max_length=100)
    user= models.ForeignKey(user, on_delete=models.CASCADE)