# Ryugiohproject_app/views.py

from django.http import JsonResponse
from django.shortcuts import render
from .models import Card
from .services import CardService

# Main page view
def index(request):
    cards = Card.objects.all()
    return render(request, 'index.html', {'cards': cards})

# API data fetching and saving to database view
def cardinfo(request):
    result = CardService.fetch_and_save_card_data()
    if 'message' in result:
        return JsonResponse(result, status=200)
    else:
        return JsonResponse(result, status=500)
