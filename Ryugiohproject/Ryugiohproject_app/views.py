from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Case, When
from django.http import HttpResponseBadRequest
from .models import Card
from django.core.paginator import Paginator
from common.models import LikeList


# Each Character page view
def eachCharacter(request):
    character = request.GET.get('character')
    
    character_decks = {
        'yugi': {
            'name': '유우기',
            'description': '"나는 이 카드에 내 모든 것을 걸겠어!"',
            'deck': 'Starter Deck: Yugi'
        },
        'kaiba': {
            'name': '카이바',
            'description': '"나의 자존심, 나의 영혼을 이어받은 충실한 심복! 나와라, 푸른 눈의 백룡!"',
            'deck': 'Starter Deck: Kaiba'
        },
        'joey': {
            'name': '조이',
            'description': '"포기하면⋯ 미래로 갈 수 없잖아!!"',
            'deck': 'Starter Deck: Joey'
        },
        'pegasus': {
            'name': '페가수스',
            'description': '"저는 당신의 패를 전부 파악하고 있습니다!"',
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

    user = request.user
    liked_cards = []

    if user.is_authenticated:
        liked_cards = LikeList.objects.filter(user=user, card_id__in=cards).values_list('card_id', flat=True)

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
    
    return render(request, 'eachCharacter.html', {'character_info': character_info, 'card_data': card_data, 'liked_cards': liked_cards})


# Main page view
def main_cards(request):
    card_ids = [70903634, 33396948, 7902349, 8124921, 44519536, 10000000, 10000010, 10000020, 23995346]
    
    user = request.user
    liked_cards = []

    if user.is_authenticated:
        liked_cards = LikeList.objects.filter(user=user, card_id__in=card_ids).values_list('card_id', flat=True)
    
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

    return render(request, 'index.html', {'exodia':exodia, 'threegod':threegod, 'liked_cards': liked_cards})


# View to get all card details
def all_cards(request):
    cards = Card.objects.all()


    user = request.user
    liked_cards = []

    if user.is_authenticated:
        liked_cards = LikeList.objects.filter(user=user, card_id__in=cards).values_list('card_id', flat=True)


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

    return render(request, 'allCard.html', {'card_data':card_data, 'liked_cards': liked_cards})



def all_cards_JSON(request):
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


def game_guide(request):
    return render(request, 'gameGuide.html')
