from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Vote
from .forms import UserForm, VoteForm, ChangeVoteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from datetime import datetime


def index(request):
    return render(request, 'Main/index.html')


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
    return render(request, 'Main/auth.html', context)


def moreaboutus(request):
    return render(request, 'Main/more-about-us.html')


def TransparentVotingSystem(request):
    return render(request, 'Main/TransparentVotingSystem.html')


def ConvenienceAndSimplicity(request):
    return render(request, 'Main/ConvenienceAndSimplicity.html')


def UniversalNotification(request):
    return render(request, 'Main/UniversalNotification.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request):
    if not request.user.is_authenticated:
        return redirect('auth')
    return render(request, 'Main/profile.html')


@login_required
def profile_Discussions(request):
    if not request.user.is_authenticated:
        return redirect('auth')
    return render(request, 'Main/Discussions.html')


@login_required
def profile_Votes(request):
    if not request.user.is_authenticated:
        return redirect('auth')
    votes = Vote.objects.all()
    totalusers = 300
    form2 = ChangeVoteForm()
    if request.method == 'POST':
        vote = votes[int(request.POST['id']) - 1]
        if request.POST['vote'] == 'yes':
            vote.accepts += 1
            vote.canvote = False
            vote.save()
        else:
            vote.de_accepts += 1
            vote.canvote = False
            vote.save()
    context = {
        'votes': votes,
        'form': form2,
        'totalusers': totalusers
    }
    return render(request, 'Main/Votes.html', context)


@login_required
def profile_Setting(request):
    if not request.user.is_authenticated:
        return redirect('auth')
    return render(request, 'Main/Setting.html')


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

    return render(request, 'Main/NewVote.html', context)