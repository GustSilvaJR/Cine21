from django.contrib import admin
from .models import Anime, Filme, Game, Genero, Serie


# Register your models here.
admin.site.register(Genero)
admin.site.register(Filme)
admin.site.register(Serie)
admin.site.register(Anime)
admin.site.register(Game)