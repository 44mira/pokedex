from rest_framework.viewsets import ModelViewSet
from pokedex.models import EvolutionNode, EvolutionTree
from pokedex.serializers import EvolutionTreeSerializer, EvolutionNodeSerializer


class EvolutionNodeViewset(ModelViewSet):
    queryset = EvolutionNode.objects.all()
    serializer_class = EvolutionNodeSerializer


class EvolutionTreeViewset(ModelViewSet):
    queryset = EvolutionTree.objects.all()
    serializer_class = EvolutionTreeSerializer
