from django import forms
# does import forms grab ModelForm?
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Message, Comment

# Forms ---

# Class to describe a new Django User using Django's UserCreationForm, form derived from model
# TODO__ look into UserCreationForm for more understanding
class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30,required=True)
    last_name = forms.CharField(max_length=30,required=True)
    # TODO__ look at what Meta tag is exactly
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    # modified save method
    # TODO__ understand cleaned_data more
    # Also, thorough understanding of data flow with self and save method
    # commit allows editing without saving?
    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

# Class to describe a new Message form based on Message model
# TODO__ Read into ModelForm for more understanding
class MessageCreateForm(forms.ModelForm):
    messageText = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Message
        fields = ('messageText',)
    def save(self, id, commit=True):
        messageR = super(MessageCreateForm, self).save(commit=False)
        messageR.messageText = self.cleaned_data["messageText"]
        messageR.user_id = id
        if commit:
            messageR.save()
        return messageR

# Class to describe a new Comment form based on Comment model
class CommentCreateForm(forms.ModelForm):
    commentText = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Comment
        fields = ('commentText',)
    def save(self, id, id2, commit=True):
        commentR = super(CommentCreateForm, self).save(commit=False)
        commentR.messageText = self.cleaned_data["commentText"]
        commentR.user_id = id
        commentR.message_id = id2
        if commit:
            commentR.save()
        return commentR

# Class to describe Login form object
class LoginForm(forms.Form):
    username= forms.CharField(label=
    'username', max_length=45)
    password = forms.CharField(max_length=100,widget=forms.PasswordInput)

# Class to describe Message form object
class MessageForm(forms.Form):
    messageText = forms.CharField(widget=forms.Textarea)

# Class to describe Comment form object
class CommentForm(forms.Form):
    commentText = forms.CharField(widget=forms.Textarea)


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

# form notes
# A Form instance has an is_valid() method
# returns True or False
# form's data is placed in cleaned_data attribute

# in views.py, form data is sent back to Django site (generally) using the same view which published the form.

#Working form process:
# Described by Django 'Form', processed by a view, rendered as an HTML <form>

# cleaned_data will be Python typed
