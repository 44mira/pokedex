from django.urls import path

from pokedex.views import (
    PokemonList,
    PokemonDetail,
    PokemonCreate,
    PokemonDelete,
    PokemonUpdate,
)

urlpatterns = [
    path("pokemons/", PokemonList.as_view(), name="pokemon-list"),
    path("pokemon/<int:pk>", PokemonDetail.as_view(), name="pokemon-detail"),
    path("pokemon/", PokemonCreate.as_view(), name="pokemon-create"),
    path("pokemon/<int:pk>/delete", PokemonDelete.as_view(), name="pokemon-delete"),
    path("pokemon/<int:pk>/update", PokemonUpdate.as_view(), name="pokemon-update"),
]
