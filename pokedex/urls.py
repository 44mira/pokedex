from django.urls import path

from pokedex.views import PokemonList, PokemonDetail

urlpatterns = [
    path("pokemon/", PokemonList.as_view(), name="pokemon-list"),
    path("pokemon/<int:pk>", PokemonDetail.as_view(), name="pokemon-detail"),
]
