import requests
from .models import Card, CardSet
from django.db import transaction
import logging

logger = logging.getLogger(__name__)

class CardService:

    @staticmethod
    def fetch_and_save_card_data():
        urls = [
            'https://db.ygoprodeck.com/api/v7/cardinfo.php?cardset=Starter%20Deck:%20Yugi',
            'https://db.ygoprodeck.com/api/v7/cardinfo.php?cardset=Starter%20Deck:%20Kaiba',
            'https://db.ygoprodeck.com/api/v7/cardinfo.php?cardset=Starter%20Deck:%20Joey',
            'https://db.ygoprodeck.com/api/v7/cardinfo.php?cardset=Starter%20Deck:%20Pegasus',
            'https://db.ygoprodeck.com/api/v7/cardinfo.php?name=Obelisk%20the%20Tormentor',
            'https://db.ygoprodeck.com/api/v7/cardinfo.php?name=Slifer%20the%20Sky%20Dragon',
            'https://db.ygoprodeck.com/api/v7/cardinfo.php?name=The%20Winged%20Dragon%20of%20Ra',
            'https://db.ygoprodeck.com/api/v7/cardinfo.php?name=Exodia%20the%20Forbidden%20One',
            'https://db.ygoprodeck.com/api/v7/cardinfo.php?name=Right%20Arm%20of%20the%20Forbidden%20One',
            'https://db.ygoprodeck.com/api/v7/cardinfo.php?name=Left%20Arm%20of%20the%20Forbidden%20One',
            'https://db.ygoprodeck.com/api/v7/cardinfo.php?name=Left%20Leg%20of%20the%20Forbidden%20One',
            'https://db.ygoprodeck.com/api/v7/cardinfo.php?name=Right%20Leg%20of%20the%20Forbidden%20One',
            'https://db.ygoprodeck.com/api/v7/cardinfo.php?name=Blue-Eyes%20Ultimate%20Dragon'
        ]

        all_cards = []

        # Fetch data from all URLs
        for url in urls:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if 'data' in data:
                    all_cards.extend(data['data'])
                else:
                    error_message = f'Invalid data format from {url}'
                    logger.error(error_message)
                    return {'error': error_message}
            else:
                error_message = f'Failed to retrieve data from {url}: {response.status_code}'
                logger.error(error_message)
                return {'error': error_message}

        # Sort the cards by id and remove duplicates
        all_cards.sort(key=lambda card: card['id'])
        unique_cards = []
        last_id = None
        for card in all_cards:
            if card['id'] != last_id:
                unique_cards.append(card)
                last_id = card['id']

        # Save all unique card data to the database
        try:
            with transaction.atomic():
                for card in unique_cards:
                    # Get the first image URL
                    image_url = card['card_images'][0]['image_url'] if card['card_images'] else None

                    # Create or update the card
                    card_obj, created = Card.objects.update_or_create(
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
                            'card_images': image_url,
                            'card_prices': card.get('card_prices'),
                        }
                    )

                    # Check for specific set names in card_sets and create or update the sets
                    for card_set in card.get('card_sets', []):
                        if card_set['set_name'] in ['Starter Deck: Yugi', 'Starter Deck: Kaiba', 'Starter Deck: Joey', 'Starter Deck: Pegasus']:
                            set_obj, set_created = CardSet.objects.update_or_create(
                                set_name=card_set['set_name'],
                            )
                            card_obj.sets.add(set_obj)
            return {'message': 'Data successfully saved to database'}
        except Exception as e:
            logger.error(f'Error saving data to the database: {e}')
            return {'error': 'Error saving data to the database'}
