from django import forms
from .models import Language ,Word,Country
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name', 'code', 'countries']
        widgets = {
            'countries': forms.CheckboxSelectMultiple(),
        }


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word', 'meaning']
        
class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name', 'code']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')