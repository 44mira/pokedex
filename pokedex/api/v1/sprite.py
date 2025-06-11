from rest_framework.viewsets import ModelViewSet
from pokedex.models import Sprite
from pokedex.serializers import SpriteSerializer


class SpriteViewSet(ModelViewSet):
    queryset = Sprite.objects.all()
    serializer_class = SpriteSerializer
