from django import forms
from .models import Language ,Word,Country

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