from django.db import models


class Cats(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    old = models.IntegerField()
