from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']