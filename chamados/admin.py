from re import search
from django.contrib import admin

# Register your models here.
from .models import Chamado

class ListandoChamados(admin.ModelAdmin):
    list_display = ('numero_chamado','titulo','categoria','fila','estado')
    list_display_links = ('numero_chamado','titulo')
    list_editable = ('estado',)
    search_fields = ('numero_chamado','titulo')
    list_filter = ('categoria','fila','estado')
    list_per_page=5

admin.site.register(Chamado,ListandoChamados)