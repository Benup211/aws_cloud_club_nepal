from django.forms import ModelForm, PasswordInput, CharField
from django.core.exceptions import ValidationError
import re
from .models import User
from django import forms

class AWSMembershipRegisterForm(ModelForm):
    confirm_password = CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class':'w-full input input-purple-900'}),
        required=True
    )

    class Meta:
        model = User
        fields = ['email', 'password', 'confirm_password', 'first_name', 'last_name', 'phone_number', 'address', 'resume']
        widgets = {
            'email': forms.TextInput(attrs={'class':'w-full input input-purple-900'}),
            'password': forms.PasswordInput(attrs={'class':'w-full input input-purple-900'}),
            'first_name': forms.TextInput(attrs={'class':'w-full input input-purple-900'}),
            'last_name': forms.TextInput(attrs={'class':'w-full input input-purple-900'}),
            'phone_number': forms.TextInput(attrs={'class':'w-full input input-purple-900'}),
            'address': forms.TextInput(attrs={'class':'w-full input input-purple-900'}),
            'resume': forms.FileInput(attrs={'class':'w-full file-input input-purple-900 '}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['password'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['phone_number'].required = True
        self.fields['address'].required = True
        self.fields['resume'].required = True
        self.fields['password'].validators = [password_validator]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

def password_validator(value):
    if len(value) < 8:
        raise ValidationError("Password must be at least 8 characters long.")
    special_chars = r'[!@#$%^&*(),.?":{}|<>]'
    if not re.search(special_chars, value):
        raise ValidationError("Password must contain at least one special character.")
    
class AWSMembershipLoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'w-full input input-purple-900'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'w-full input input-purple-900'})
    )