from django.db import models


class Sprite(models.Model):
    front_default = models.URLField(null=True)
    front_shiny = models.URLField(null=True)
    front_female = models.URLField(null=True)
    front_shiny_female = models.URLField(null=True)
    back_default = models.URLField(null=True)
    back_shiny = models.URLField(null=True)
    back_female = models.URLField(null=True)
    back_shiny_female = models.URLField(null=True)
