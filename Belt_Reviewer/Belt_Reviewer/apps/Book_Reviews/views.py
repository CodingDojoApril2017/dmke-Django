# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse

from .forms import BookCreateForm, ReviewCreateForm

from .models import Books, Reviews


# Create your views here.
"""
View function for books page
- sends latest (3) review objects to html
- sends all book objects to html
"""
def render_home(request):
    print "routed to render_home"
    ## render home/books template
    ## get latest 3 reviews
    ## get books list
    ## logout link
    ## add book link
    ## display user name
    return render(request, "Book_Reviews/books.html")

def render_add(request):
    print "routed to render_add"
    bookForm = BookCreateForm()
    reviewForm = ReviewCreateForm()

    context={
        "bookForm":bookForm,
        "reviewForm":reviewForm,
    }

    return render(request, "Book_Reviews/add.html", context)

def process_add(request):
    print "routed to process_add"
    ## add new Book and new Review
    print(request.POST)
    newBook = BookCreateForm(request.POST, prefix='book')
    newReview = ReviewCreateForm(request.POST, prefix='review')
    print newBook
    print newReview
    if newBook.is_valid() and newReview.is_valid():
        print "Book and Review: valid"
        book = newBook.save(commit=False)
        book.save()
        book_id = book.id

        # newReview.user_id = request.user.id
        # print newReview.user_id
        review = newReview.save(book_id = book.id, user_id = request.user.id, commit=False)
        # save error doesn't see book_id as not NULL
        review.save()
    else:
        print "Not valid"

    return redirect(reverse('book-reviews:render_book', args=(book_id,)))

def render_book(request, book_id):
    print "routed to render_book"
    ## get Book ID
    displayThisBook = Books.objects.get(id=book_id)
    print displayThisBook
    allThisBookReviews = Reviews.objects.filter(book_id=book_id)
    print allThisBookReviews
    context={
        "displayThisBook":displayThisBook,
        "allThisBookReviews":allThisBookReviews
    }

    print
    return render(request, "Book_Reviews/showbook.html", context)




    #print authUser
    # registerFormToRender = UserCreateForm()
    # # Using Django AuthForm vs extended LoginForm defined in forms.py
    # loginFormToRender = AuthenticationForm()
    # context={
    #     "registerForm":registerFormToRender,"loginForm":loginFormToRender, #"forErrors":authUser
    # }

    # testing to show Django ORM/SQL queries
    #showSQL = connection.queries
    #print showSQL

    # connection.queries = []
    # Protocols.objects.filter(active=False)
    # print connection.queries
