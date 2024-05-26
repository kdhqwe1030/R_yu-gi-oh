from django.db import models

# Create your models here.

class Card(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    attack_points = models.IntegerField()
    defense_points = models.IntegerField()

    def __str__(self):
        return self.name