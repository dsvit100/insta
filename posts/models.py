from django.db import models

# Create your models here.

class Post(models.Model): # 사진 + 내용만 있으니까 title 필요없음
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='image') # upload_to는 필수옵션
    # 사진을 첨부하면 image 폴더가 생성되고 그 안에 이미지가 저장됨 (upload_to='image')
    # 이미지필드를 사용하기 위해서는 pillow가 필요