# Ryugiohproject_app/views.py

from django.http import JsonResponse
from django.shortcuts import render
from .models import Card
from .services import CardService

# Main page view
def index(request):
    cards = Card.objects.all()
    return render(request, 'index.html', {'cards': cards})


