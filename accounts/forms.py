from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('username', 'profile_image', ) # 이건 어디서 왔는가

class CustomAuthenticationForm(AuthenticationForm):
    pass # 커스텀해줄 것 없기 때문에