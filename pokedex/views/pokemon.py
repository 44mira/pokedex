from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    DetailView,
    UpdateView,
)
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


class PokemonCreate(CreateView):
    model = Pokemon
    fields = "__all__"

    template_name = "pokemon_form.html"
    success_url = "/pokedex/pokemons/"


class PokemonDelete(DeleteView):
    model = Pokemon

    template_name = "pokemon_delete.html"
    success_url = "/pokedex/pokemons/"


class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = "__all__"

    template_name = "pokemon_form.html"
    success_url = "/pokedex/pokemons/"
