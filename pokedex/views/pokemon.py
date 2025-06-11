from django.views.generic import ListView, DetailView
from pokedex.models import Pokemon


class PokemonList(ListView):
    model = Pokemon
    ordering = "pk"

    context_object_name = "pokemon"
    template_name = "pokemon_list.html"


class PokemonDetail(DetailView):
    model = Pokemon

    context_object_name = "pokemon"
    template_name = "pokemon_detail.html"
