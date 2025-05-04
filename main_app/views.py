from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LanguageForm, WordForm ,CountryForm
from .models import Language, Word,Country
# Import HttpResponse to send text-based responses
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView , ListView
from django.shortcuts import get_object_or_404

# Define the home view function
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

def language_index(request):
    languages = Language.objects.all()  # Get all Languages
    return render(request, 'languages/index.html', {'languages': languages})

def language_detail(request, code):
    language = Language.objects.get(code=code)
    return render(request, 'languages/detail.html', {'language': language})

def word_index(request):
    words = Word.objects.all().select_related('language') 
    return render(request, 'words/index.html', {'words': words})

# In main_app/views.py
def add_country(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('language_index')  # Or your preferred redirect
    else:
        form = CountryForm()
    
    return render(request, 'main_app/add_country.html', {'form': form})

class WordList(LoginRequiredMixin, ListView):
    model = Word
    template_name = 'words/index.html'
    context_object_name = 'words'
    
    def get_queryset(self):
        return Word.objects.all().select_related('language').order_by('language__code', 'text')
#language CRUD
class LanguageCreate(LoginRequiredMixin, CreateView):
    model = Language
    form_class = LanguageForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('language_detail', kwargs={'code': self.object.code})

class LanguageUpdate(LoginRequiredMixin, UpdateView):
    model = Language
    form_class = LanguageForm
    slug_field = 'code'  # Use 'code' as the identifier instead of pk
    slug_url_kwarg = 'code'  # The URL parameter name
    
    def get_success_url(self):
        return reverse('language_detail', kwargs={'code': self.object.code})

class LanguageDelete(LoginRequiredMixin, DeleteView):
    model = Language
    slug_field = 'code'
    slug_url_kwarg = 'code'
    
    def get_success_url(self):
        return reverse('language_index')
    
 #Word CRUD   
class WordCreate(LoginRequiredMixin, CreateView):
    model = Word
    form_class = WordForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        language_code = self.kwargs['code']  # Get language code from URL
        form.instance.language = get_object_or_404(Language, code=language_code)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('language_detail', kwargs={'code': self.object.language.code})

class WordUpdate(LoginRequiredMixin, UpdateView):
    model = Word
    form_class = WordForm
    
    def get_success_url(self):
        return reverse('language_detail', kwargs={'code': self.object.language.code})

class WordDelete(LoginRequiredMixin, DeleteView):
    model = Word
    
    def get_success_url(self):
        return reverse('language_detail', kwargs={'code': self.object.language.code})