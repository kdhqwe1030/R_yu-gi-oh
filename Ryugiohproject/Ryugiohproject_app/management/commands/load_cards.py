# Ryugiohproject_app/management/commands/load_cards.py

from django.core.management.base import BaseCommand
from Ryugiohproject_app.services import CardService
from Ryugiohproject_app.models import Card

class Command(BaseCommand):
    help = 'Load cards from external API and save to database'

    def handle(self, *args, **kwargs):
        # 기존 데이터를 삭제
        self.stdout.write('Deleting existing card data...')
        Card.objects.all().delete()

        # 새로운 데이터를 가져와서 저장
        result = CardService.fetch_and_save_card_data()
        if 'message' in result:
            self.stdout.write(self.style.SUCCESS(result['message']))
        else:
            self.stdout.write(self.style.ERROR(result['error']))
