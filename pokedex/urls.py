from django.urls import include, path

from rest_framework import routers
from pokedex.api.v1 import (
    PokemonViewset,
    MoveViewset,
    PoketypeViewset,
    SpriteViewset,
    EvolutionNodeViewset,
    EvolutionTreeViewset,
)

from pokedex.views import (
    PokemonList,
    PokemonDetail,
    PokemonCreate,
    PokemonDelete,
    PokemonUpdate,
)

router = routers.SimpleRouter()
router.register(r"pokemon", PokemonViewset)
router.register(r"type", PoketypeViewset)
router.register(r"move", MoveViewset)
router.register(r"sprite", SpriteViewset)
router.register(r"evolution-node", EvolutionNodeViewset)
router.register(r"evolution-tree", EvolutionTreeViewset)

urlpatterns = [
    path("pokemons/", PokemonList.as_view(), name="pokemon-list"),
    path("pokemon/<int:pk>/", PokemonDetail.as_view(), name="pokemon-detail"),
    path("pokemon/", PokemonCreate.as_view(), name="pokemon-create"),
    path("pokemon/<int:pk>/delete/", PokemonDelete.as_view(), name="pokemon-delete"),
    path("pokemon/<int:pk>/update/", PokemonUpdate.as_view(), name="pokemon-update"),
    path("api/v1/", include(router.urls)),
]
