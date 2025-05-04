from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('languages/', views.language_index, name='language_index'),  # Changed from 'language-index'
    path('language/<str:code>/', views.language_detail, name='language_detail'),
    path('languages/add/', views.LanguageCreate.as_view(), name='language_create'),
    path('languages/<str:code>/', views.language_detail, name='language_detail'),
    path('languages/<str:code>/edit/', views.LanguageUpdate.as_view(), name='language_update'),
    path('languages/<str:code>/delete/', views.LanguageDelete.as_view(), name='language_delete'),
    path('language/<str:code>/word/add/', views.WordCreate.as_view(), name='word_create'),
    path('word/<int:pk>/update/', views.WordUpdate.as_view(), name='word_update'),
    path('word/<int:pk>/delete/', views.WordDelete.as_view(), name='word_delete'),
    path('words/', views.word_index, name='word_index'),
    path('words/', views.WordList.as_view(), name='word_list'),
    path('country/add/', views.add_country, name='add_country'),

]