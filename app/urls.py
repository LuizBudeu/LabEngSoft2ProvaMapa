from django.urls import path
from . import views

urlpatterns = [
    path('', views.mapa, name='mapa'),
    path('mapa/', views.mapa, name='mapa')
]