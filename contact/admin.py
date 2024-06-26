from django.contrib import admin
from contact.models import Contact, Category

@admin.register(Contact)    # Usa o decorator para registrar o model
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'show'    # Mostrar first_name, last_name e phone no display
    ordering = '-id', # Ordernar por Id decrescente
    list_filter = ('category',)  # Filtros disponíveis
    search_fields = 'first_name', 'id', 'last_name'   # Campo de pesquisa
    list_per_page = 10  # Itens por página
    list_max_show_all = 100 # Itens máximo a se mostrar na tela
    list_editable = 'phone', 'show'   # Permite ter tópicos editáveis
    list_display_links = 'first_name',   # O que está como editable, não pode estar aqui
    

@admin.register(Category)    # Usa o decorator para registrar o model
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',    # Mostrar first_name, last_name e phone no display
    ordering = '-id', # Ordernar por Id decrescente
    search_fields = 'name',   # Campo de pesquisa
    list_display_links = 'name',   # O que está como editable, não pode estar aqui