from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),

    path('like-toggle/', views.like_toggle, name='like_toggle'),
    path('like-status/<int:card_id>/', views.like_status, name='like_status'),

    path('my_page/', views.mypage, name='my_page'),
]
