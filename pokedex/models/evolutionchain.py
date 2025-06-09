from django.db import models


class EvolutionChain(models.Model):
    first = models.OneToOneField(
        "pokedex.Pokemon",
        on_delete=models.CASCADE,
        related_name="evolution_chain",
    )
    second = models.OneToOneField(
        "pokedex.Pokemon",
        on_delete=models.CASCADE,
        related_name="evolution_chain",
        null=True,
    )
    third = models.OneToOneField(
        "pokedex.Pokemon",
        on_delete=models.CASCADE,
        related_name="evolution_chain",
        null=True,
    )
    fourth = models.OneToOneField(
        "pokedex.Pokemon",
        on_delete=models.CASCADE,
        related_name="evolution_chain",
        null=True,
    )
    branching = models.BooleanField(default=False)
