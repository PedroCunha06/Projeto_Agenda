import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 500

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'   # Configura o settings do Django, visto que vai rodar um código externo
settings.USE_TZ = False     # Desativar o timezone

django.setup()

if __name__ == '__main__':
    import faker    # Módulo que gera dados fake, para testes
    
    from contact.models import Contact, Category
    
    Contact.objects.all().delete()
    Category.objects.all().delete()
    
    fake = faker.Faker('pt_BR')
    categories = ['Amigos', 'Família', 'Conhecidos', 'Trabalho']
    
    django_categories = [Category(name=name) for name in categories]    # Cria categorias
    
    for category in django_categories:  # Salva as categorias criadas
        category.save()
        
    django_contact = []
    
    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile['mail']
        first_name, last_name = profile['name'].split(' ', 1)
        phone = fake.phone_number()
        created_data: datetime = fake.date_this_year()
        description = random_text = fake.text(max_nb_chars=100)
        category = choice(django_categories)
        
        django_contact.append(
            Contact(
                first_name = first_name,
                last_name = last_name,
                email = email,
                phone = phone,
                created_date = created_data,
                description = description,
                category = category,
            )
            
        )
        
    if len(django_contact) > 0:
        Contact.objects.bulk_create(django_contact)
        
    
    

