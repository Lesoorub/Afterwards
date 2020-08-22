from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def auth(request):

    return render(request, 'main/auth.html')