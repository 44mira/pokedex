import pytest
import pokebase as pb

from ._import_functions import (
    import_evolution,
    import_pokemon,
    import_types,
    import_sprite,
    import_moves,
)
from pokedex.models import Pokemon, Sprite, Move, Poketype, EvolutionTree


@pytest.mark.integration
@pytest.mark.django_db
def test_import_pokemon():
    bulbasaur = import_pokemon(1)

    assert bulbasaur.pk == 1
    assert bulbasaur.name == "bulbasaur"
    assert bulbasaur.height == 7
    assert bulbasaur.weight == 69
    assert bulbasaur.sprite == Sprite.objects.first()
    assert bulbasaur.types.first() == Poketype.objects.get(name="grass")

    ivysaur = Pokemon.objects.get(name="ivysaur")
    venusaur = Pokemon.objects.get(name="venusaur")
    assert bulbasaur.evolution_tree.get_tree() == [
        (bulbasaur, 0),
        (ivysaur, 1),
        (venusaur, 2),
    ]

    # check if it creates a new bulbasaur
    bulbasaur = import_pokemon(1)
    assert bulbasaur.pk == 1
    assert bulbasaur.name == "bulbasaur"


@pytest.mark.skip
@pytest.mark.django_db
def test_import_types():
    venusaur = pb.pokemon(3)
    import_types(venusaur.types)

    assert Poketype.objects.count() == 2
    assert Poketype.objects.get(name="grass")
    assert Poketype.objects.get(name="poison")


@pytest.mark.skip
@pytest.mark.django_db
def test_import_sprite():
    expected = {
        "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/1.png",
        "back_female": None,
        "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/1.png",
        "back_shiny_female": None,
        "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
        "front_female": None,
        "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/1.png",
        "front_shiny_female": None,
    }

    sprite = import_sprite(pb.pokemon(1).sprites.__dict__)

    for key in expected.keys():
        assert getattr(sprite, key) == expected[key]


@pytest.mark.slow
@pytest.mark.django_db
def test_import_moves():
    pokemon = pb.pokemon(1)

    import_moves(pokemon.moves)
    move1_type = pokemon.moves[0].move.type.name

    assert Move.objects.count() == len(pokemon.moves)
    assert Move.objects.first().name == pokemon.moves[0].move.name
    assert Move.objects.first().poketype.name == move1_type


@pytest.mark.django_db
def test_import_evolution():
    pokemon = pb.pokemon(1)

    import_evolution(pokemon.evolution_chain)
