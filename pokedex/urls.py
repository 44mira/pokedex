from django.urls import include, path

from rest_framework import routers
from pokedex.api.v1 import (
    PokemonViewSet,
    MoveViewSet,
    PoketypeViewSet,
    SpriteViewSet,
    EvolutionNodeViewSet,
    EvolutionTreeViewSet,
)

from pokedex.views import (
    PokemonList,
    PokemonDetail,
    PokemonCreate,
    PokemonDelete,
    PokemonUpdate,
)

router = routers.SimpleRouter()
router.register(r"pokemon", PokemonViewSet)
router.register(r"type", PoketypeViewSet)
router.register(r"move", MoveViewSet)
router.register(r"sprite", SpriteViewSet)
router.register(r"evolution-node", EvolutionNodeViewSet)
router.register(r"evolution-tree", EvolutionTreeViewSet)

pokemon_views = [
    path("<int:pk>/", PokemonDetail.as_view(), name="pokemon-detail"),
    path("", PokemonCreate.as_view(), name="pokemon-create"),
    path("<int:pk>/delete/", PokemonDelete.as_view(), name="pokemon-delete"),
    path("<int:pk>/update/", PokemonUpdate.as_view(), name="pokemon-update"),
]

urlpatterns = [
    path("pokemons/", PokemonList.as_view(), name="pokemon-list"),
    path("pokemon/", include(pokemon_views)),
    path("api/v1/", include((router.urls, "api"))),
]
