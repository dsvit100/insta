from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)


def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST) # request = cookie
        if form.is_valid():
            user = form.get_user() # form에는 html 태그뭉치를 포함하여 많은 정보가 들어있으므로, 사용자의 id/pw만 가져오게 하는 함수
            auth_login(request, user)
            # 내가 로그인하려는 user에 대한 정보 = user의 id와 pw가 들어있음 -> 폼에서 가져왔으니까
            return redirect('posts:index')
    else:
        form = CustomAuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('posts:index')


def profile(request, username):
    user_profile = User.objects.get(username=username)
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'profile.html', context)

@login_required
def follow(request, username):
    me = request.user # 로그인 한 본인
    you = User.objects.get(username=username) # 내가 들어와있는 페이지의 유저

    if me == you:
        return redirect('accounts:profile', username)

    # 너를 따르는 사람의 전체 목록에 내가 있으면 (팔로우를 했다는 것)
    if me in you.followers.all():
        you.followers.remove(me)
    else:
        you.followers.add(me) # 너의 팔로워 목록에 나를 넣어줘
    return redirect('accounts:profile', username)

