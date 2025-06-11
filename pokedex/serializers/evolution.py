from rest_framework import serializers
from pokedex.models import EvolutionNode, EvolutionTree


class EvolutionTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvolutionTree
        fields = "__all__"


class EvolutionNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvolutionNode
        fields = "__all__"
