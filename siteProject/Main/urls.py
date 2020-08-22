from django.urls import path
from . import views

urlpatterns = [
    path('auth', views.auth, name='auth'),
    path('index', views.index, name='index'),
    path('more-about-us', views.moreaboutus, name='more-about-us'),
    path('TransparentVotingSystem', views.TransparentVotingSystem, name='TransparentVotingSystem'),
    path('ConvenienceAndSimplicity', views.ConvenienceAndSimplicity, name='ConvenienceAndSimplicity'),
    path('UniversalNotification', views.UniversalNotification, name='UniversalNotification'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout_view, name='logout'),
    path('', views.index, name='home')
]
