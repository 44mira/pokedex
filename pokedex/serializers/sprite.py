from rest_framework import serializers
from pokedex.models import Sprite


class SpriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprite
        fields = "__all__"
