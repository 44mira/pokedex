from rest_framework.viewsets import ModelViewSet
from pokedex.models import Move
from pokedex.serializers import MoveSerializer


class MoveViewSet(ModelViewSet):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer
