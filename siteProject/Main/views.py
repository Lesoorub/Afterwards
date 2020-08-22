from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'main/index.html')


def auth(request):
    form = UserForm()
    error_login = False
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            #form.save()
            return redirect('home')
        else:
            error_login = True

    context = {
        'form': form,
        'error_login': error_login
    }
    return render(request, 'main/auth.html', context)


def moreaboutus(request):
    return render(request, 'main/more-about-us.html')


def TransparentVotingSystem(request):
    return render(request, 'main/TransparentVotingSystem.html')


def ConvenienceAndSimplicity(request):
    return render(request, 'main/ConvenienceAndSimplicity.html')


def UniversalNotification(request):
    return render(request, 'main/UniversalNotification.html')


@login_required()
def profile(request):

    return render(request, 'main/profile.html')