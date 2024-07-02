from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

def login_required_with_message(message):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.warning(request, message)
                return redirect(reverse('contact:login'))
            return view_func(request, *args, **kwargs)
        
        return _wrapped_view
    return decorator