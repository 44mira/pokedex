from rest_framework import serializers
from pokedex.models import Poketype


class PoketypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poketype
        fields = "__all__"
