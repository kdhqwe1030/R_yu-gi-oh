from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_cards, name='main_cards'),
    path('mainPage/', views.main_cards, name='main_cards'),
    path('eachCharacter/', views.eachCharacter, name='eachCharacter'),
    path('allCards/', views.all_cards, name='all_cards'),
    path('api/main-cards/', views.main_cards, name='main_cards'),
    path('api/character-deck/', views.character_deck, name='character_deck'),
    path('api/character-deck/effect/', views.character_deck_effect, name='character_deck_effect'),
    path('api/character-deck/normal/', views.character_deck_normal, name='character_deck_normal'),
    path('api/character-deck/spell/', views.character_deck_spell, name='character_deck_spell'),
    path('api/character-deck/trap/', views.character_deck_trap, name='character_deck_trap'),
]
