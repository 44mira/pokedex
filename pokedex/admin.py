from django.contrib import admin

from pokedex.models import Pokemon, Poketype, Move, Sprite, EvolutionNode, EvolutionTree


class EvolutionNodeAdmin(admin.ModelAdmin):
    list_display = ["pokemon", "parent"]


# Register your models here.

admin.site.register(Pokemon)
admin.site.register(Poketype)
admin.site.register(Sprite)
admin.site.register(Move)
admin.site.register(EvolutionNode, EvolutionNodeAdmin)
admin.site.register(EvolutionTree)
