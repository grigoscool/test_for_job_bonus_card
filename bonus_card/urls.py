from django.urls import path

from . import views


app_name = 'bonus_card'

urlpatterns = [
    path('', views.home, name='home'),
    path('card-detail/<int:pk>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('activate/<int:pk>/', views.activate, name='activate'),
    path('deactivate/<int:pk>/', views.deactivate, name='deactivate'),
    path('delete/<int:pk>/', views.delete, name='delete'),

]
