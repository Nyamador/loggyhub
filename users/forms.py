from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class UserSignUpForm(SignupForm):
    """
    Overriding AllAuth's SignupForm to add an option for telephone number
    """

    def save(self, request):
        user = super(UserSignUpForm, self).save(request)
        return user



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('email',)