from rest_framework.viewsets import ModelViewSet
from pokedex.models import EvolutionNode, EvolutionTree
from pokedex.serializers import EvolutionTreeSerializer, EvolutionNodeSerializer


class EvolutionNodeViewSet(ModelViewSet):
    queryset = EvolutionNode.objects.all()
    serializer_class = EvolutionNodeSerializer


class EvolutionTreeViewSet(ModelViewSet):
    queryset = EvolutionTree.objects.all()
    serializer_class = EvolutionTreeSerializer
