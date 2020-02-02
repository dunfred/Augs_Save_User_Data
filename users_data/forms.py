from django import forms
from .models import UserDetails

class CreateUserForm(forms.ModelForm):

    class Meta:
        model = UserDetails
        fields = '__all__'

