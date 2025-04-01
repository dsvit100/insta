from django.forms import ModelForm
from .models import Post, Comment

class PostForm(ModelForm):
    class Meta():
        model = Post
        fields = ('content', 'image', )


class CommentForm(ModelForm):
    class Meta():
        model = Comment
        fields = ('content', ) # user와 post는 우리가 작성해 줄 것