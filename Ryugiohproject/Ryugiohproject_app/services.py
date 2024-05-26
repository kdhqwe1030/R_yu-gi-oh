# Ryugiohproject_app/services.py

import requests
from .models import Card
from django.db import transaction

class CardService:

    @staticmethod
    def fetch_and_save_card_data():
        url = 'https://db.ygoprodeck.com/api/v7/cardinfo.php?cardset=Starter%20Deck:%20Yugi'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'data' in data:
                cards = data['data']
                with transaction.atomic():
                    for card in cards:
                        Card.objects.update_or_create(
                            id=card.get('id'),
                            defaults={
                                'name': card.get('name'),
                                'type': card.get('type'),
                                'frameType': card.get('frameType'),
                                'desc': card.get('desc'),
                                'atk': card.get('atk'),
                                'defense': card.get('def'),
                                'level': card.get('level'),
                                'race': card.get('race'),
                                'attribute': card.get('attribute'),
                                'card_images': card.get('card_images'),
                                'card_prices': card.get('card_prices'),
                            }
                        )
                return {'message': 'Data successfully saved to database'}
            else:
                return {'error': 'Invalid data format'}
        else:
            return {'error': f'Failed to retrieve data: {response.status_code}'}
