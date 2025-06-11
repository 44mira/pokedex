from rest_framework.viewsets import ModelViewSet
from pokedex.models import Pokemon
from pokedex.serializers.pokemon import PokemonSerializer


class PokemonViewset(ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
