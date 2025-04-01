from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    posts = Post.objects.all()
    form = CommentForm()

    context = {
        'posts': posts,
        'form': form,
    }
    return render(request, 'index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) # 사진 데이터도 같이 넣기 위해서 두번째 인자 작성
        if form.is_valid():
            post = form.save(commit=False) # 이 게시물을 누가 저장했는지의 유저정보가 빠져있음음
            post.user = request.user
            form.save()
            return redirect('posts:index')

    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)