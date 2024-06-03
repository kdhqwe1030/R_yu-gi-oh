from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import like_toggle

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('like-toggle/', like_toggle, name='like_toggle'),

    path('my_page/', views.mypage, name='my_page'),
]
