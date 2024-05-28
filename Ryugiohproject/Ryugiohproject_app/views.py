# Ryugiohproject_app/views.py

from django.http import JsonResponse
from django.shortcuts import render
from .models import Card
from .services import CardService

# Main page view
def index(request):
    if 'ids' in request.GET:
        card_ids = request.GET.getlist('ids')
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
    else:
        return render(request, 'index.html')


