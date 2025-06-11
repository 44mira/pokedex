from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def type_color(typename):
    COLORS = {
        "normal": "#A8A77A",
        "fire": "#EE8130",
        "water": "#6390F0",
        "electric": "#F7D02C",
        "grass": "#7AC74C",
        "ice": "#96D9D6",
        "fighting": "#C22E28",
        "poison": "#A33EA1",
        "ground": "#E2BF65",
        "flying": "#A98FF3",
        "psychic": "#F95587",
        "bug": "#A6B91A",
        "rock": "#B6A136",
        "ghost": "#735797",
        "dragon": "#6F35FC",
        "dark": "#705746",
        "steel": "#B7B7CE",
        "fairy": "#D685AD",
    }

    return COLORS[typename]


@register.simple_tag
def sprite(sprite):
    if sprite is None:
        return ""

    return mark_safe(f'<img src="{sprite}" class="pokemon-sprite__img" height=150 />')


@register.simple_tag
def evolutions(evolution_tree):
    layers = [[], [], [], []]
    output = '<div class="evolution-tree">'

    for pokemon, layer in evolution_tree.get_tree():
        layers[layer].append(pokemon)

    for layer in layers:
        layer_output = '<div class="evolution-layer">'

        for pokemon in layer:
            layer_output += f"""
            <a href={reverse("pokemon-detail", args=[pokemon.pk])}>
                <div class="evolution-node">
                    <img src={pokemon.sprite.front_default} height=100 />
                    <div class='evolution-name'>
                        {pokemon.name.title()}
                    </div>
                </div>
            </a>
            """

        layer_output += "</div>"
        output += layer_output

    output += "</div>"
    return mark_safe(output)
