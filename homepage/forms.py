from django.forms import ModelForm, Form, ChoiceField, CharField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Store
import datetime


class StoreForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'


# class LoginForm(forms.Form):
#     email = forms.CharField(max_length=100)
#     password = forms.CharField(widget=forms.PasswordInput)
#     remember_me = forms.BooleanField(required=False)

# class LoginUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['email', 'password', 'remember_me']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class FilterForm(Form):
    search = CharField(max_length=200, required=True)


class AddStoreForm(ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'alias', 'phone', 'email',
                  'address', 'avatar_image']


class UpdateStoreForm(ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'avatar_image']
