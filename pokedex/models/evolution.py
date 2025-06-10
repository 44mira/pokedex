from django.db import models

"""
We represent evolution lines as trees to allow for scaleable branching.

               +--> EvolNode (possible)
               |
EvolTree -> EvolNode ---> EvolNode
"""


class EvolutionNode(models.Model):
    """
    Each Evolution node
    - will hold a reference to a pokemon
    - will hold a reference to its parent and next node.
    - can hold multiple or no next nodes

    Root nodes do not have a parent node (NULL).
    """

    pokemon = models.OneToOneField(
        "pokedex.Pokemon",
        on_delete=models.CASCADE,
        related_name="+",
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="next_nodes",
        null=True,
    )


class EvolutionTree(models.Model):
    """
    An EvolutionTree is a representation of the evolutionary lines of a
    pokemon. It will hold a reference to the root evolution node.

    It also has a method for fully traversing the tree.
    """

    root = models.OneToOneField(
        "pokedex.EvolutionNode",
        on_delete=models.CASCADE,
        related_name="+",
    )

    def get_tree(self):
        """
        Returns a list of tuples containing a Pokemon and their depth in the
        evolution tree.
        """
        results = []

        # perform breadth-first search on all the children
        def _traverse(node, depth):
            results.append((node.pokemon, depth))
            for n in node.next_nodes.all():
                _traverse(n, depth + 1)

        _traverse(self.root, 0)
        return results
