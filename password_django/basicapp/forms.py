from django import forms
from django.contrib.auth.models import User
from basicapp.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
