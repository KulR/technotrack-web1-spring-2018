from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model as user


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = user()
        fields = UserCreationForm.Meta.fields + ('email',)
