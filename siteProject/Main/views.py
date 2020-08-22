from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def auth(request):
    return render(request, 'main/auth.html')

def moreaboutus(request):
    return render(request, 'main/more-about-us.html')

def TransparentVotingSystem(request):
    return render(request, 'main/TransparentVotingSystem.html')

def ConvenienceAndSimplicity(request):
    return render(request, 'main/ConvenienceAndSimplicity.html')

def UniversalNotification(request):
    return render(request, 'main/UniversalNotification.html')