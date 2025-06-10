import pokebase as pb

from pokedex.models import Pokemon, Poketype, Sprite, Move, EvolutionTree, EvolutionNode

_verbose = False
_stdout = None


def import_types(types):
    """
    Requires an iterable of Pokebase types.
    """
    imported_types = set()
    for poketype in types:
        name = poketype.name

        res = Poketype.objects.filter(name=name).first()
        if res is None:
            if _verbose:
                _stdout.write(f"Successfully added type {name.capitalize()}.")

            res = Poketype.objects.create(name=name)

        imported_types.add(res)

    return imported_types


def import_sprite(sprites):
    """
    Requires a dict of Pokebase sprites.
    """
    # discard unaccessed fields
    del sprites["versions"]
    del sprites["other"]

    return Sprite.objects.create(**sprites)


def import_moves(moves):
    """
    Requires an iterable of Pokebase moves.
    """
    imported_moves = set()

    for m in moves:
        move = m.move
        name = move.name

        res = Move.objects.filter(name=move.name).first()
        if res is not None:
            imported_moves.add(res)
            continue

        poketype = import_types([move.type]).pop()
        res = Move.objects.create(name=name, poketype=poketype)

        if _verbose:
            _stdout.write(f"Successfully added move {name.capitalize()}.")

        imported_moves.add(res)

    return imported_moves


def import_evolution(evolution_chain):
    """
    Requires a Pokebase evolution chain.
    """

    ancestor = evolution_chain.species.name
    p_ancestor = Pokemon.objects.filter(name=ancestor).first()
    if p_ancestor is None:
        p_ancestor = import_pokemon(ancestor)
    stored_ancestor = EvolutionNode.objects.filter(pokemon=p_ancestor).first()

    stored_tree = EvolutionTree.objects.filter(root=stored_ancestor).first()
    if stored_tree is not None:
        return stored_tree

    # otherwise, we need to create a new EvolutionTree

    def _traverse_chain(level, parent):
        for branch in level:
            pokemon = import_pokemon(branch.species.name)

            current = EvolutionNode.objects.filter(pokemon=pokemon).first()
            if current is None:
                current = EvolutionNode.objects.create(pokemon=pokemon, parent=parent)

            _traverse_chain(branch.evolves_to, current)

    root = EvolutionNode.objects.filter(pokemon=p_ancestor).first()
    if root is None:
        root = EvolutionNode.objects.create(pokemon=p_ancestor)
    _traverse_chain(evolution_chain.evolves_to, root)

    stored_tree = EvolutionTree.objects.filter(root=root).first()
    if stored_tree is None:
        if _verbose:
            _stdout.write(
                f"Successfully added evolution tree for {ancestor.capitalize()}."
            )
        stored_tree = EvolutionTree.objects.create(root=root)

    return stored_tree


def import_pokemon(id, *, verbose=False, stdout=None) -> Pokemon:
    global _verbose, _stdout
    _verbose = verbose
    _stdout = stdout

    pokemon = pb.pokemon(id)

    # skip if it exists
    stored_pokemon = Pokemon.objects.filter(name=pokemon.name).first()
    if stored_pokemon is not None:
        return stored_pokemon

    # serialize dependency entities
    imported_types = import_types(map(lambda t: t.type, pokemon.types))
    imported_sprite = import_sprite(pokemon.sprites.__dict__)
    imported_moves = import_moves(pokemon.moves)

    # serialize pokemon
    imported = Pokemon.objects.create(
        name=pokemon.name,
        height=pokemon.height,
        weight=pokemon.weight,
        sprite=imported_sprite,
    )
    imported.types.set(imported_types)
    imported.moves.set(imported_moves)

    # An EvolutionTree requires the pokemon to exist first
    imported.evolution_tree = import_evolution(pokemon.species.evolution_chain.chain)
    imported.save()

    if _verbose:
        _stdout.write(f"Successfully added {imported.name.capitalize()}.")
    return imported
