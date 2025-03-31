from django.db import models
from django_resized import ResizedImageField
from django.conf import settings

# Create your models here.

class Post(models.Model): # 사진 + 내용만 있으니까 title 필요없음
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
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