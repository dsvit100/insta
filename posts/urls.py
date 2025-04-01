from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:post_id>/comments/create/', views.comment_create, name='comment_create'),
    # 댓글을 저장할 공간을 설정해 줌, 댓글창을 보여주는 곳은 index일 것
    path('<int:post_id>/like/', views.like, name='like'),
]