from django.forms.models import model_to_dict
import pytest


from . import *

SQUIRTLE_SPRITES = {
    "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/7.png",
    "back_female": None,
    "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/7.png",
    "back_shiny_female": None,
    "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png",
    "front_female": None,
    "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/7.png",
    "front_shiny_female": None,
}


@pytest.fixture
def setup(db):
    squirtle_sprite = Sprite.objects.create(**SQUIRTLE_SPRITES)
    wartortle_sprite = Sprite.objects.create()

    water_type = Poketype.objects.create(name="Water")
    normal_type = Poketype.objects.create(name="Normal")
    ice_type = Poketype.objects.create(name="Ice")

    ice_punch = Move.objects.create(name="Ice Punch", poketype=ice_type)
    headbutt = Move.objects.create(name="Headbutt", poketype=normal_type)

    squirtle = Pokemon.objects.create(
        name="Squirtle",
        sprite=squirtle_sprite,
        height=5,
        weight=9,
    )
    squirtle.types.set([water_type])
    squirtle.moves.set([ice_punch, headbutt])

    wartortle = Pokemon.objects.create(
        name="Wartortle",
        sprite=wartortle_sprite,
        height=10,
        weight=22,
    )
    wartortle.types.set([water_type])
    wartortle.moves.set([ice_punch, headbutt])

    squirtle_enode = EvolutionNode.objects.create(pokemon=squirtle, parent=None)
    wartortle_enode = EvolutionNode.objects.create(
        pokemon=wartortle, parent=squirtle_enode
    )
    squirtle_etree = EvolutionTree.objects.create(root=squirtle_enode)


@pytest.mark.django_db
def test_poketype(setup):
    water_type = Poketype.objects.get(name="Water")
    ice_type = Poketype.objects.get(name="Ice")
    squirtle = Pokemon.objects.get(name="Squirtle")
    ice_punch = Move.objects.get(name="Ice Punch")

    assert water_type
    assert Poketype.objects.count() == 3
    assert water_type.pokemon.first() == squirtle

    assert ice_punch.poketype == ice_type
    assert squirtle.types.first() == water_type


@pytest.mark.django_db
def test_sprite(setup):
    sprite = Sprite.objects.first()
    assert sprite
    assert sprite.pokemon == Pokemon.objects.get(name="Squirtle")

    sprite_dict = model_to_dict(sprite)
    del sprite_dict["id"]
    assert sprite_dict == SQUIRTLE_SPRITES


@pytest.mark.django_db
def test_move(setup):
    ice_punch = Move.objects.get(name="Ice Punch")
    headbutt = Move.objects.get(name="Headbutt")
    squirtle = Pokemon.objects.get(name="Squirtle")

    assert ice_punch
    assert headbutt
    assert Move.objects.count() == 2

    assert ice_punch.pokemon.first() == squirtle
    assert headbutt.pokemon.first() == squirtle

    assert squirtle.moves.count() == 2
    assert squirtle.moves.filter(name="Ice Punch").exists()
    assert squirtle.moves.filter(name="Headbutt").exists()


@pytest.mark.django_db
def test_pokemon(setup):
    squirtle = Pokemon.objects.get(name="Squirtle")
    assert squirtle
    assert squirtle.height == 5
    assert squirtle.weight == 9
    assert squirtle.sprite == Sprite.objects.first()
    assert squirtle.types.count() == 1
    assert squirtle.moves.count() == 2

    water_type = Poketype.objects.get(name="Water")
    assert squirtle.types.first() == water_type

    ice_punch = Move.objects.get(name="Ice Punch")
    headbutt = Move.objects.get(name="Headbutt")
    assert ice_punch in squirtle.moves.all()
    assert headbutt in squirtle.moves.all()


@pytest.mark.django_db
def test_evolution(setup):
    squirtle_enode = EvolutionNode.objects.get(pokemon__name="Squirtle")
    wartortle_enode = EvolutionNode.objects.get(pokemon__name="Wartortle")
    squirtle_etree = EvolutionTree.objects.get(root=squirtle_enode)

    assert squirtle_enode.pokemon.name == "Squirtle"
    assert wartortle_enode.pokemon.name == "Wartortle"
    assert squirtle_etree.root == squirtle_enode

    assert squirtle_enode.next_nodes.count() == 1
    assert wartortle_enode.parent == squirtle_enode
    assert squirtle_etree.get_tree() == [
        (squirtle_enode.pokemon, 0),
        (wartortle_enode.pokemon, 1),
    ]
