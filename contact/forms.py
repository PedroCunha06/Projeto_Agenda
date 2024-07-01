from django.core.exceptions import ValidationError
from django import forms

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
        )
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
