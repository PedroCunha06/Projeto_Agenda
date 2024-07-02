from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation

from . import models


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'placeholder': 'Write the first name',
            }
        ),
        help_text="Don't write nickname.",
    )
    picture = forms.ImageField(
        widget = forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        ),
        required=False,
    )
    class Meta:
        model = models.Contact
        fields = 'first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture'
        
        
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        
        if first_name == last_name:
            self.add_error(
                'last_name',
                ValidationError(
                    "The last name cannot be the same as the first. Try again",
                    code='invalid'
                )
            )
        

        return cleaned_data
        
    def clean_first_name(self):
            first_name = self.cleaned_data.get('first_name')
            if first_name == 'ABC':
                raise ValidationError(
                    "Don't enter ABC",
                    code = 'invalid'
                )
            return first_name

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3
    )
    last_name = forms.CharField(
        required=True,
        min_length=3
    )
    email = forms.EmailField(
        required=True,  
    )
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email', 'username', 'password1', 'password2',
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                'This email already exists',
                code='invalid'
            )
        
        return email
    
class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text="Required.",
        error_messages={
            'min_length': 'Please, add more than 2 letters'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text="Required.",
        error_messages={
            'min_length': 'Please, add more than 2 letters'
        }
    )
    password1 = forms.CharField(
        label='Password',
        strip=False,
        required=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='Password 2',
        strip=False,
        required=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text= "Use the same password as before",
    )
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email', 'username', 
      
      
    def save(self, commit=False): 
        cleaned_data = self.cleaned_data
        user = super().save(commit=False) 
        
        password = cleaned_data.get('password1')
        
        if password:
            user.set_password(password)
            
        if commit:
            user.save()
            
        return user
      
    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('The passwords are diferent')
                )
                
                
        return super().clean()  
      
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_login = self.instance.email
        
        if email != email_login:
            if User.objects.filter(email=email).exists():
                raise ValidationError(
                    'This email already exists',
                    code='invalid'
                )
            
            return email
        
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        
        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(errors)
                )
        
        return password1