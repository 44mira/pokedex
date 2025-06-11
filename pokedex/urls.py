from django.urls import path

from rest_framework import routers
from pokedex.api.v1 import PokemonViewset

from pokedex.views import (
    PokemonList,
    PokemonDetail,
    PokemonCreate,
    PokemonDelete,
    PokemonUpdate,
)

router = routers.SimpleRouter()
router.register(r"pokemon/api/v1", PokemonViewset)

urlpatterns = [
    path("pokemons/", PokemonList.as_view(), name="pokemon-list"),
    path("pokemon/<int:pk>/", PokemonDetail.as_view(), name="pokemon-detail"),
    path("pokemon/", PokemonCreate.as_view(), name="pokemon-create"),
    path("pokemon/<int:pk>/delete/", PokemonDelete.as_view(), name="pokemon-delete"),
    path("pokemon/<int:pk>/update/", PokemonUpdate.as_view(), name="pokemon-update"),
]

urlpatterns += router.urls
