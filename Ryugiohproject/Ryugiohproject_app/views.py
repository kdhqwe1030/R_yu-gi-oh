from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Case, When
from django.http import HttpResponseBadRequest
from .models import Card

# Each Character page view
def eachCharacter(request):
    character = request.GET.get('character')
    character_decks = {
        'yugi': {
            'name': 'Yugi',
            'description': 'The main protagonist of the series.',
            'deck': 'Starter Deck: Yugi'
        },
        'kaiba': {
            'name': 'Kaiba',
            'description': 'Yugi\'s main rival.',
            'deck': 'Starter Deck: Kaiba'
        },
        'joey': {
            'name': 'Joey',
            'description': 'Yugi\'s best friend.',
            'deck': 'Starter Deck: Joey'
        },
        'pegasus': {
            'name': 'Pegasus',
            'description': 'The creator of Duel Monsters.',
            'deck': 'Starter Deck: Pegasus'
        }
    }

    if not character:
        return HttpResponseBadRequest("Character parameter is missing")
    
    if character not in character_decks:
        return HttpResponseBadRequest("Invalid character parameter")
    
    character_info = character_decks[character]
    deck_name = character_info['deck']
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
    
    return render(request, 'eachCharacter.html', {'character_info': character_info, 'card_data': card_data})



# Main page view
def main_cards(request):
    card_ids = [70903634, 33396948, 7902349, 8124921, 44519536, 10000000, 10000010, 10000020, 23995346]
    
    preserved_order = Case(
        *[When(id=card_id, then=pos) for pos, card_id in enumerate(card_ids)]
    )
    
    cards = Card.objects.filter(id__in=card_ids).order_by(preserved_order)
    
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
    exodia = card_data[:5]
    threegod= card_data[5:]

    return render(request, 'index.html', {'exodia':exodia, 'threegod':threegod})


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

    return render(request, 'allCard.html', {'card_data':card_data})


# View to get character deck card details
def character_deck(request):
    character = request.GET.get('character', '').lower()
    character_decks = {
        'yugi': 'Starter Deck: Yugi',
        'kaiba': 'Starter Deck: Kaiba',
        'joey': 'Starter Deck: Joey',
        'pegasus': 'Starter Deck: Pegasus',
    }

    if character in character_decks:
        deck_name = character_decks[character]
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

# FrameType-based views
def character_deck_effect(request):
    character = request.GET.get('character', '').lower()
    cards = Card.objects.filter(sets__set_name__icontains=character, frameType='effect')
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

def character_deck_normal(request):
    character = request.GET.get('character', '').lower()
    cards = Card.objects.filter(sets__set_name__icontains=character, frameType='normal')
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

def character_deck_spell(request):
    character = request.GET.get('character', '').lower()
    cards = Card.objects.filter(sets__set_name__icontains=character, frameType='spell')
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

def character_deck_trap(request):
    character = request.GET.get('character', '').lower()
    cards = Card.objects.filter(sets__set_name__icontains=character, frameType='trap')
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
