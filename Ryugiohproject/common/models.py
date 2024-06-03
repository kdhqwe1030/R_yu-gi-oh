from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LikeList(models.Model):
    class Meta:
        db_table = 'like_list'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey('Ryugiohproject_app.Card', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
