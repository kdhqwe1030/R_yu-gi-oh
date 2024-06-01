# Ryugiohproject_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/main-cards/', views.main_cards, name='main_cards'),
    path('api/all-cards/', views.all_cards, name='all_cards'),
    path('api/character-deck/<str:character>/', views.character_deck, name='character_deck'),
]
