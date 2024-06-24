from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact

def index(request):
    contacts = Contact.objects.filter(show=True).order_by('first_name')
    
    context = {
        'contacts': contacts ,
        'site_title': 'Contacts -'
    }  
    
    return render(
        request,
        'contact/index.html',
        context
    )
    
def search(request):
    search_value = request.GET.get('q', '').strip()
    
    if search_value == '':
        return redirect('contact:index')    # Quando não acha o valor, redireciona para outra página
    
    contacts = Contact.objects.\
        filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |     # Usa para fazer pesquisa OU
            Q(phone__icontains=search_value) |          # Usa para fazer pesquisa OU
            Q(email__icontains=search_value) |          # Usa para fazer pesquisa OU
            Q(last_name__icontains = search_value))\
        .order_by('first_name')
    
    context = {
        'contacts': contacts ,
        'site_title': 'Contacts -'
    }  
    
    return render(
        request,
        'contact/index.html',
        context
    )   
    
def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    
    context = {
        'contact': single_contact,
        'site_title': f'{single_contact.first_name} -'
    }  
    
    return render(
        request,
        'contact/contact.html',
        context
    )
