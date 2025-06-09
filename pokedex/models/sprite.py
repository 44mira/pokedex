from django.db import models


class Sprite(models.Model):
    front_default = models.URLField()
    front_shiny = models.URLField()
    front_female = models.URLField()
    front_shiny_female = models.URLField()
    back_default = models.URLField()
    back_female = models.URLField()
    back_shiny_female = models.URLField()
