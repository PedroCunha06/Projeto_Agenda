from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# ID (primary key - gerado automaticamente) -> Valor que busca na base de dados
# first_name(string) - last_name(string) -  phone(string) - email(email) - created_date(date) - description(text)
# category(foreing key) - show(boolean) - picture(image)
# DEPOIS 
# - owner(foreing key) 

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'   # O que mostrar quando houver uma categoria
        verbose_name_plural = 'Categories'  # O que mostrar quando estiver no plural
    
    name = models.CharField(max_length=30)
    
    def __str__(self) -> str:   # O  que será mostrado na admin do model
        return f'{self.name}'

class Contact(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=25)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)   # Django registra automaticamente a hora de criação.
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
    category = models.ForeignKey(   # Relacão com classe Categoria
        Category, 
        on_delete=models.SET_NULL,
        blank=True, null=True)
    owner = models.ForeignKey(   # Relacão com classe Categoria
        User, 
        on_delete=models.CASCADE,   # Apaga tudo quando o usuario é deletado
        blank=True, null=True)
    
    def __str__(self) -> str:   # O  que será mostrado na admin do model
        return f'{self.first_name} {self.last_name}'
    
    