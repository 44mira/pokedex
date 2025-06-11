from rest_framework.viewsets import ModelViewSet
from pokedex.models import Poketype
from pokedex.serializers import PoketypeSerializer


class PoketypeViewSet(ModelViewSet):
    queryset = Poketype.objects.all()
    serializer_class = PoketypeSerializer
