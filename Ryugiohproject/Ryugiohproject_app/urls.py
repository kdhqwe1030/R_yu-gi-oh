from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cardinfo/', views.cardinfo, name='cardinfo'),
]
