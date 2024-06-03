# Ryugiohproject/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Ryugiohproject_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Ryugiohproject_app.urls')),
    path('', include('common.urls')),
    path('', views.main_cards, name='main_cards'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
