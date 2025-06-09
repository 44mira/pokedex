from django.db import models


class Move(models.Model):
    name = models.CharField(max_length=30)
    poketype = models.ForeignKey(
        "pokedex.Poketype",
        on_delete=models.CASCADE,
        related_name="moves",
    )
