from django.contrib import admin
from contact.models import Contact

@admin.register(Contact)    # Usa o decorator para registrar o model
class ContactAdmin(admin.ModelAdmin):
    list_display = 'first_name', 'last_name', 'phone',    # Mostrar first_name, last_name e phone no display
    ordering = '-id', # Ordernar por Id decrescente
    # list_filter = ('id',)  # Filtros disponíveis
    search_fields = 'first_name', 'id', 'last_name'   # Campo de pesquisa
    list_per_page = 10  # Itens por página
    list_max_show_all = 100 # Itens máximo a se mostrar na tela
    list_editable = 'first_name', 'last_name',    # Permite ter tópicos editáveis
    list_display_links = 'phone',   # O que está como editable, não pode estar aqui