from django.contrib import admin

from .models import Autor, Carte, Categorie, Cerere

admin.site.register(Autor)
admin.site.register(Carte)
admin.site.register(Categorie)
admin.site.register(Cerere)
