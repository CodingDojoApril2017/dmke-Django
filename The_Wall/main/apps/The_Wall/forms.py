from django import forms
# does import forms grab ModelForm?
from django.forms import ModelForm
#from .models import Users

from django.contrib.auth.models import User

# import UserCreationForm from django
from django.contrib.auth.forms import UserCreationForm

# import Message from .models file
from .models import Message

# Unique case for model/form due to inclusion and use of Django defined 'User'
class UserCreateForm(UserCreationForm):
    # Validations, required fields
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30,required=True)
    last_name = forms.CharField(max_length=30,required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        # create and save user
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

# class for message form, pulls from message model
class MessageCreateForm(forms.ModelForm):
    messageText = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Message
        fields = ('messageText',)
    # create and save message?

    # def save(self, commit=True):
    #     message = super(MessageCreateForm, self).save(commit=False)
    #     message.message = self.cleaned_data["message"]


# form notes
# A Form instance has an is_valid() method
# returns True or False
# form's data is placed in cleaned_data attribute
class LoginForm(forms.Form):
    username= forms.CharField(label=
    'username', max_length=45)
    password = forms.CharField(max_length=100,widget=forms.PasswordInput)

class MessageForm(forms.Form):
    messageText = forms.CharField(widget=forms.Textarea)


# contact me form example
# class ContactForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
#     sender = forms.EmailField()


# class RegisterForm(forms.ModelForm):
#     # create form from model ...
#     password = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = User
#         fields =

    # first_name = forms.CharField(max_length=45)
    # last_name = forms.CharField(max_length=45)
    # email = forms.EmailField()
    # password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    # confirm_password = forms.CharField(max_length=100,widget=forms.PasswordInput)


# in views.py, form data is sent back to Django site (generally) using the same view which published the form.

#Working form process:
# Described by Django 'Form', processed by a view, rendered as an HTML <form>

# cleaned_data will be Python typed
