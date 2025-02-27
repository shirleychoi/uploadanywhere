from django.db import models

# Create your models here.
from datetime import datetime


class MyModel(models.Model):
    asdf = models.TextField(null=True)


class FileModel(models.Model):
    objects = None
    key = models.IntegerField(null=False)
    time = models.DateTimeField(null=False, default=datetime.now)
    file = models.FileField(null=False, upload_to='media')
