from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    old = models.IntegerField()
    description = models.CharField(max_length=200)

