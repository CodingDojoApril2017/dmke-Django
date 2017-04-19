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
            newSecretMessage = super(SecretCreateForm, self).save(commit=False)
            Secret.save(commit=False)
            Secret.secretMessage = self.cleaned_data["secretMessage"]
            newSecretMessage.user_id = id
            
            if commit:
                newSecretMessage.save()
            return newSecretMessage

class SecretCreateForm(forms.ModelForm):
    secretMessage = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Secret
        fields = ('secretMessage',)

## Just Forms 

# Class to describe Login form object
class LoginForm(forms.Form):
    username = forms.CharField(label=
    'username', max_length=45)
    password = forms.CharField(max_length=100,widget=forms.PasswordInput)
    



            