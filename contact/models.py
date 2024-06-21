from django.db import models
from django.utils import timezone

# ID (primary key - gerado automaticamente) -> Valor que busca na base de dados
# first_name(string) - last_name(string) -  phone(string) - email(email) - created_date(date) - description(text)
# DEPOIS 
# category(foreing key) - show(boolean) - owner(foreing key) - picture(image)

class Contact(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=25)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)   # Django registra automaticamente a hora de criação.
    description = models.TextField(blank=True)
    
    