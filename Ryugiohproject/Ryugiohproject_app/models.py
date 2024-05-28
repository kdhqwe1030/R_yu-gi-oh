from django.db import models

class CardSet(models.Model):
    set_name = models.CharField(max_length=100)

    def __str__(self):
        return self.set_name

class Card(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    frameType = models.CharField(max_length=100, null=True, blank=True)
    desc = models.TextField()
    atk = models.IntegerField(null=True, blank=True)
    defense = models.IntegerField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    race = models.CharField(max_length=100)
    attribute = models.CharField(max_length=100, null=True, blank=True)
    card_images = models.URLField(null=True, blank=True)
    card_prices = models.JSONField(null=True, blank=True)
    sets = models.ManyToManyField(CardSet, related_name='cards')

    def __str__(self):
        return self.name
