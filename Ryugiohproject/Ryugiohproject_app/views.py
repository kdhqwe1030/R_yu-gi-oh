# Ryugiohproject_app/views.py

from django.http import JsonResponse
from django.shortcuts import render
from .models import Card

# Main page view
def index(request):
    return render(request, 'test.html')

# View to get specific card details
def main_cards(request):
    card_ids = [10000000, 10000010, 10000020, 33396948, 7902349, 44519536, 23995346, 8124921]
    cards = Card.objects.filter(id__in=card_ids)
    card_data = [{
        'id': card.id,
        'name': card.name,
        'type': card.type,
        'frameType': card.frameType,
        'desc': card.desc,
        'atk': card.atk,
        'defense': card.defense,
        'level': card.level,
        'race': card.race,
        'attribute': card.attribute,
        'card_images': card.card_images,
        'card_prices': card.card_prices,
    } for card in cards]
    return JsonResponse(card_data, safe=False)

# View to get all card details
def all_cards(request):
    cards = Card.objects.all()
    card_data = [{
        'id': card.id,
        'name': card.name,
        'type': card.type,
        'frameType': card.frameType,
        'desc': card.desc,
        'atk': card.atk,
        'defense': card.defense,
        'level': card.level,
        'race': card.race,
        'attribute': card.attribute,
        'card_images': card.card_images,
        'card_prices': card.card_prices,
    } for card in cards]
    return JsonResponse(card_data, safe=False)

# View to get character deck card details
def character_deck(request, character):
    character_decks = {
        'yugi': 'Starter Deck: Yugi',
        'kaiba': 'Starter Deck: Kaiba',
        'joey': 'Starter Deck: Joey',
        'pegasus': 'Starter Deck: Pegasus',
    }

    if character.lower() in character_decks:
        deck_name = character_decks[character.lower()]
        cards = Card.objects.filter(sets__set_name=deck_name)
        card_data = [{
            'id': card.id,
            'name': card.name,
            'type': card.type,
            'frameType': card.frameType,
            'desc': card.desc,
            'atk': card.atk,
            'defense': card.defense,
            'level': card.level,
            'race': card.race,
            'attribute': card.attribute,
            'card_images': card.card_images,
            'card_prices': card.card_prices,
        } for card in cards]
        return JsonResponse(card_data, safe=False)
    else:
        return JsonResponse({'error': 'Character not found'}, status=404)
