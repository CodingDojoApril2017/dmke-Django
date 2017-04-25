from django import forms
# does import forms grab ModelForm?
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Books, Reviews


"""
TODO for Book_Reviews: forms.py
-
"""
## Model-based forms
## Extending the Django UserCreationForm class
## UserCreateForm is a subclass of UserCreationForm
class BookCreateForm(forms.ModelForm):
    # title = forms.CharField(max_length=256, required=True)
    # author = forms.CharField(max_length=128, required=True)
    prefix = 'book'
    class Meta:
        model = Books
        fields = ['title', 'author']

    def save(self, commit=True):
        book = super(BookCreateForm, self).save(commit=False)
        book.title = self.cleaned_data["title"]
        book.author = self.cleaned_data["author"]
        if commit:
            book.save()
        return book

## Forms
## Extending the Django AuthenticationForm class
## LoginForm is a subclass of AuthenticationForm
class ReviewCreateForm(forms.ModelForm):
    prefix = 'review'

    class Meta:
        model = Reviews
        fields = ['review_text',]
        exclude = ['user','book',]

    def save(self, book_id, user_id, commit=True):
        review = super(ReviewCreateForm, self).save(commit=False)
        review.review_text = self.cleaned_data["review_text"]
        review.book_id = book_id
        review.user_id = user_id
        if commit:
            review.save()
        return review
