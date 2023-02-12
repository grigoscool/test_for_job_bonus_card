from django.urls import path

from . import views


app_name = 'bonus_card'

urlpatterns = [
    path('', views.home, name='home'),
    path('card-detail/<int:pk>/', views.detail, name='detail'),
]
