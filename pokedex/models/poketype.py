from django.db import models


class Poketype(models.Model):
    name = models.CharField(max_length=10)
