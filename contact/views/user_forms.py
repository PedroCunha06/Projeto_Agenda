from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.shortcuts import render, redirect

from contact.forms import RegisterForm, RegisterUpdateForm

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Registered user')
            return redirect('contact:index')

    return render(
        request,
        'contact/register.html',
        {
            'form': form,
            'title': 'Register User'
        }
    )
    
def login_views(request):
    form = AuthenticationForm(request)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('contact:login')
        
        messages.error(request, 'Loggin failed')
    
    return render(
        request,
        'contact/login.html',
        {
            'form': form,
            'title': 'Login User'
        }
    )
    
   
def logout_views(request):
    confirmation = request.POST.get('confirmation', 'no')
     
    if confirmation == 'yes':
        auth.logout(request)
        messages.success(request, 'User logged out')
        return redirect('contact:login')
    
    return render(
        request,
        'contact/logout.html',
        {
            'title': 'Logout User'
        }
    )
    
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)
    
    if request.method == 'POST':
        form = RegisterUpdateForm(instance=request.user, data=request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated')
            return redirect('contact:index')
            
        messages.error(request, 'Update failed')
        
    return render(
        request,
        'contact/register.html',
        {
            'form': form,
            'title': 'Update User'
        }
    )