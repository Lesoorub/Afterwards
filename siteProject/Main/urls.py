from django.urls import path
from . import views

urlpatterns = [
    path('auth', views.auth, name='auth'),
    path('index', views.index, name='index'),
    path('', views.index, name='home')
]
