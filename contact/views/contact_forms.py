from django.contrib import messages
from contact.decorators import login_required_with_message
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from contact.forms import ContactForm    
from contact.models import Contact

@login_required_with_message('You need to be logged in to create a contact')  
def create(request):
    form_action = reverse('contact:create')
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        
        context = {
        'form': form ,
        'form_action': form_action,
        'title': 'Create Contact',
        }  
        
        # Caso o formulário seja válido, então será redirecionado para a página update
        if form.is_valid():
            contact = form.save(commit=False)     # Salva os dados na base de dados
            contact.owner = request.user
            contact.save()
            messages.success(request, 'Contact created')
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
  
@login_required_with_message('You need to be logged in to update a contact')     
def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner=request.user)  # Busca do contato ou erro 404
    form_action = reverse('contact:update', args=(contact_id, ))
    
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        
        context = {
        'form': form ,
        'form_action': form_action,
        'title': 'Update Contact',
        }  
        
        # Caso o formulário seja válido, então será redirecionado para a página update
        if form.is_valid():
            contact = form.save()     # Salva os dados na base de dados
            messages.success(request, 'Updated contact')
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

@login_required_with_message('You need to be logged in to delete a contact')        
def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner=request.user)  # Busca do contato ou erro 404
    confirmation = request.POST.get('confirmation', 'no')


    if confirmation == 'yes':
        contact.delete()
        messages.success(request, 'Contact deleted')
        return redirect('contact:index')
        
    return render (
        request,
        'contact/delete.html',
        {
            'contact':contact,
            'confirmation': confirmation
        }
    )