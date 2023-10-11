from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Region

User = get_user_model()

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

class CustomUserCreationForm(UserCreationForm):
    REGION_CHOICES = [
        ('region1', '01 - Бишкек'),
        ('region2', '02 - ОШ'),
        ('region3', '03 - Баткенская область'),
        ('region4', '04 - Джалалабадская область'),
        ('region5', '05 - Нарынская область'),
        ('region6', '06 - Ошская область'),
        ('region7', '07 - Таласская область'),
        ('region8', '08 - Чуйская область'),
        ('region9', '09 - Иссык-Кульская область'),
        # Добавьте другие регионы по аналогии
    ]

    region = forms.ChoiceField(choices=REGION_CHOICES)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('region',)


class CustomUserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'region', 'password')

