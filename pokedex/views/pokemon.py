from django.db.models import Q, Count
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    DetailView,
    UpdateView,
)
from pokedex.models import Pokemon, Poketype


class PokemonList(ListView):
    model = Pokemon
    ordering = "pk"

    context_object_name = "pokemon"
    extra_context = {"types": Poketype.objects.all()}
    template_name = "pokemon_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name", None)
        types = self.request.GET.getlist("type", None)

        if types:
            # make sure pokemon's number of types matches the number of types
            # selected
            queryset = queryset.annotate(
                matched_types=Count(
                    "types", filter=Q(types__name__in=types), distinct=True
                )
            ).filter(matched_types=len(types))
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


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
