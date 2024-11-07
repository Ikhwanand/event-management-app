from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    is_organizer = forms.BooleanField(required=False)
    is_attendee = forms.BooleanField(required=False)
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'is_organizer', 'is_attendee')