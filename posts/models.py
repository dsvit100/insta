from django.db import models
from django_resized import ResizedImageField
from django.conf import settings

# Create your models here.

class Post(models.Model): # 사진 + 내용만 있으니까 title 필요없음
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # 작성자를 저장하기 위한 필드
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # image = models.ImageField(upload_to='image') # upload_to는 필수옵션
    image = ResizedImageField(
        size=[500, 500], 
        crop=['middle', 'center'],
        upload_to='image/%Y/%m'
        # 폴더 하나가 만들어지고 그 안에 이미지 파일이 들어감
        # 오늘 업로드를 하면 image/2025/03 파일이 생성되고 저장될 것
    )
    # 사진을 첨부하면 image 폴더가 생성되고 그 안에 이미지가 저장됨 (upload_to='image')
    # 이미지필드를 사용하기 위해서는 pillow가 필요

    # 중간테이블 = 무엇을 연결해 줄 것인지
    # 이 글에 좋아요를 누른 사람
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name = 'like_posts'
        # 역참조에 사용할 이름을 바꾼다 = like_posts로
    )


class Comment(models.Model): # POST와 1:N, 유저와도 1:N
    content = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # foreignkey를 쓰면 on_delete는 필수인자자
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)