from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from contact.models import Contact

def create(request):
    
    context = {

    }  
    
    return render(
        request,
        'contact/create.html',
        context
    )