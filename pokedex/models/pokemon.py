from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=30)
    height = models.FloatField()
    weight = models.FloatField()
    types = models.ManyToManyField("pokedex.Poketype", related_name="pokemon")
    moves = models.ManyToManyField("pokedex.Move", related_name="pokemon")
    sprite = models.OneToOneField(
        "pokedex.Sprite",
        on_delete=models.SET_NULL,
        related_name="pokemon",
        null=True,
    )
    evolution_tree = models.ForeignKey(
        "pokedex.EvolutionTree",
        on_delete=models.RESTRICT,
        related_name="pokemon",
        null=True,
    )
