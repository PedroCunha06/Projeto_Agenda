from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from contact.forms import ContactForm    
from contact.models import Contact

def create(request):
    form_action = reverse('contact:create')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        context = {
        'form': form ,
        'form_action': form_action,
        'title': 'Create Contact',
        }  
        
        # Caso o formulário seja válido, então será redirecionado para a página update
        if form.is_valid():
            contact = form.save()     # Salva os dados na base de dados
            return redirect('contact:update', contact_id=contact.pk)
    
        return render(
        request,
        'contact/create.html',
        context
        )
    
    context = {
        'form': ContactForm(),
        'title': 'Create Contact',
    }  
    
    return render(
        request,
        'contact/create.html',
        context
    )
    
def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)  # Busca do contato ou erro 404
    form_action = reverse('contact:update', args=(contact_id, ))
    
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        
        context = {
        'form': form ,
        'form_action': form_action,
        'title': 'Update Contact',
        }  
        
        # Caso o formulário seja válido, então será redirecionado para a página update
        if form.is_valid():
            contact = form.save()     # Salva os dados na base de dados
            return redirect('contact:update', contact_id=contact.pk)
    
        return render(
        request,
        'contact/create.html',
        context
        )
    
    context = {
        'form': ContactForm(instance=contact),
        'title': 'Update Contact',
    }  
    
    return render(
        request,
        'contact/create.html',
        context
    )