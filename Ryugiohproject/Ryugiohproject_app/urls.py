from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_cards, name='main_cards'),
    path('mainPage/', views.main_cards, name='main_cards'),
    path('eachCharacter/', views.eachCharacter, name='eachCharacter'),
    path('allCards/', views.all_cards, name='all_cards'),
    path('api/main-cards/', views.main_cards, name='main_cards'),
]
