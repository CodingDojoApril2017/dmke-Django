from django import forms
# does import forms grab ModelForm?
from django.forms import ModelForm
from .models import Secret
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Forms ---

## Model Forms

# UserCreateForm extends Django class UserCreationForm
class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1","password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

class SecretCreateForm(forms.ModelForm):
    secretMessage = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Secret
        fields = ('secretMessage',)

    def save(self, id, commit=True):
        newSecretMessage = super(SecretCreateForm, self).save(commit=False)
        Secret.secretMessage = self.cleaned_data["secretMessage"]
        newSecretMessage.userWhoPosted_id = id
        if commit:
            newSecretMessage.save()
        return newSecretMessage

## Just Forms 

# Class to describe Login form object
class LoginForm(forms.Form):
    username = forms.CharField(label=
    'username', max_length=45)
    password = forms.CharField(max_length=100,widget=forms.PasswordInput)
    



            