# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import UserCreateForm, LoginForm, MessageCreateForm, MessageForm

## Imports Users class/object from models file
# from .models import Users

# Import Django's prebuilt Users model
from django.contrib.auth.models import User
# User: username, password, email, first_name, last_name

# Create your views here.
def index(request):

    loginForm = LoginForm()
    registerForm = UserCreateForm()

    return render(request, 'The_Wall/index.html', {"registerForm":registerForm, "loginForm":loginForm})

def register(request):

    newUser = UserCreateForm(request.POST)
    # validation of form
    if newUser.is_valid():
        # creation of user/registration
        user = newUser.save(commit=False)
        user.save()

    return redirect('/wall')

def login(request):
    authUser=authenticate(username=request.POST['username'], password=request.POST['password'])
    # if request.method == 'POST':
        ##create a form instance with POST data
        ## binds data to form, form is now 'binded'
        # form = LoginForm(request.POST)
        ##check for validity
        # if form.is_valid():
            # process the data in form.cleaned_data
            # return redirect('/The_Wall/wall.html')
    # else:
        ## creates blank form
        #for =LoginForm()
    ## renders index.html with form context
    # return render(request, 'index.html', {'form': form})
    return redirect('/wall')

def wall(request):
    #context = {}
    # Request message and comment data and send to client/display on the wall

    # 1. render message form
    messageForm = MessageForm()

    return render(request, 'The_Wall/wall.html', {"messageForm":messageForm})

def message(request):
    # Add message to database using models
    return redirect('/wall')

def comment(request):
    # add id to arguments
    # / message id 

    # add comment to comment model
    # Comment.objects.create(comment=request.POST['comment'],message=message)
    return redirect('/wall')

# Some Django notes
# ... When rendering an object in Django:
# 1. Get a hod of it in the view (fetch from DB, ie.)
#2. pass it to the template context (data structure)
#3. expand it to HTML markup using template variables

# Extra notes:
# .filter returns a queryset list
# .exclude, ooposite of filter
#  conditions: __startswith="S", __contains="E"
# queries can be changed
# same query can accept multiple arguments
# | or can be used

