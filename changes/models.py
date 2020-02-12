from django.db import models
from django.conf import settings

user = settings.AUTH_USER_MODEL


class Log(models.Model):
    name = models.CharField(verbose_name="Changelog Name", max_length=100)
    user = models.ForeignKey(user, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class LogItem(models.Model):
    title = models.CharField(verbose_name="Log ", max_length=100)
    content = models.CharField(verbose_name="Content", max_length=5000)
    status = models.CharField(verbose_name="Status", max_length=10)
    is_active = models.BooleanField(verbose_name="Active l", default=False)

    def __str__(self):
        return self.title
    