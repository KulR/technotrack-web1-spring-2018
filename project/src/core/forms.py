from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model as user

from django.contrib.auth.forms import UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = user()
        fields = UserCreationForm.Meta.fields + ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserCreationForm.Meta):
        model = user()
        fields = UserCreationForm.Meta.fields + ('avatar',)
