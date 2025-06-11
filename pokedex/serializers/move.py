from rest_framework import serializers
from pokedex.models import Move


class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = "__all__"
