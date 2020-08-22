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
    path('Discussions', views.profile_Discussions, name='Discussions'),
    path('Votes', views.profile_Votes, name='Votes'),
    path('Setting', views.profile_Setting, name='Setting'),
    path('NewVote', views.profile_NewVote, name='NewVote'),
    path('', views.index, name='home')
]
