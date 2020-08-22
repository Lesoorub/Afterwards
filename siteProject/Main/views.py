from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Vote
from .forms import UserForm, VoteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from datetime import datetime


def index(request):
    return render(request, 'main/index.html')


def auth(request):
    form = UserForm()
    error_login = False

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
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


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request):
    if not request.user.is_authenticated:
        return redirect('auth')
    return render(request, 'main/profile.html')


@login_required
def profile_Discussions(request):
    if not request.user.is_authenticated:
        return redirect('auth')
    return render(request, 'main/Discussions.html')


@login_required
def profile_Votes(request):
    if not request.user.is_authenticated:
        return redirect('auth')
    votes = Vote.objects.all()

    if request.method == 'post':
        print('post')
        pass

    context = {
        'votes': votes
    }

    return render(request, 'main/Votes.html', context)


@login_required
def profile_Setting(request):
    if not request.user.is_authenticated:
        return redirect('auth')
    return render(request, 'main/Setting.html')


@login_required
def profile_NewVote(request):
    if not request.user.is_authenticated:
        return redirect('auth')
    msg = 'none'
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            t = form.save(commit=False)
            t.start_user = User.objects.get(pk=request.user.id)
            t.save()
            msg = 'OK'
        else:
            msg = 'NO'
    else:
        form = VoteForm()

    context = {
        'form': form,
        'msg': msg
    }

    return render(request, 'main/NewVote.html', context)