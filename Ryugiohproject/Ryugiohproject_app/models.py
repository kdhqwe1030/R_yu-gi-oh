from django.db import models

# Create your models here.


class Card(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, default='Normal')  # 기본값 추가
    frameType = models.CharField(max_length=100, null=True, blank=True)
    desc = models.TextField()
    atk = models.IntegerField(null=True, blank=True)
    defense = models.IntegerField(null=True, blank=True)  # 'def' 대신 'defense' 사용
    level = models.IntegerField(null=True, blank=True)
    race = models.CharField(max_length=100, default='Dragon')  # 기본값 추가
    attribute = models.CharField(max_length=100, null=True, blank=True)
    card_images = models.JSONField(null=True, blank=True)
    card_prices = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name
