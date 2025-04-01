from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField

# Create your models here.

class User(AbstractUser):
    # username
    # password
    profile_image = ResizedImageField(
        size=[500, 500],
        crop=['middle', 'center'],
        upload_to='profile',
    ) # 보이지않지만 post_set, comment_set이 들어가있음(1:N)
    # post_set (FK)
    # comment_set
    # post_set => like_posts (MMF)


    # 내가 따르는 사람을 저장하는 칼럼
    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    # 유저와 유저를 N:N으로 연결할거양, related_name=반대쪽에서 부를 컬럼 설정)
    # 나를 따르는 사람 = followers
    # 대칭구조를 하지 않기 위해 symmetrical을 False로. True인 경우 오로지 맞팔만 나옴