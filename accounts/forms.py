from datetime import datetime

from django import forms

from .models import User, Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class ProfileForm(forms.ModelForm):
    today = datetime.now().strftime("%m-%d-%Y")

    birth_date = forms.CharField(
        widget=forms.TextInput(
            attrs={'data-format': 'YYYY-MM-DD',
                   'data-template': 'D MMM YYYY',
                   'value': today,
                   }))

    class Meta:
        model = Profile
        fields = ('birth_date', 'bio', 'avatar')
