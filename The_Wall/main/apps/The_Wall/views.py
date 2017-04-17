# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm

from .forms import UserCreateForm, LoginForm, MessageCreateForm, MessageForm

## Imports Users class/object from models file
# from .models import Users

# Import Django's prebuilt Users model
from django.contrib.auth.models import User
# User: username, password, email, first_name, last_name
from .models import Message

# Create your views here.
def index(request):

    loginForm = LoginForm()
    registerForm = UserCreateForm()

    return render(request, 'The_Wall/index.html', {"registerForm":registerForm, "loginForm":loginForm})

def register(request):

    # pull down request.POST form data passed from client
    newUser = UserCreationForm(request.POST)
    print newUser
    # validation of form
    if newUser.is_valid():
        # call .save method to store in model
        user = newUser.save(commit=False)
        user.save()
        return redirect('/wall')
    else:
        return redirect('/')

def login(request):
    authUser=authenticate(username=request.POST['username'], password=request.POST['password'])
    if authUser:
        auth_login(request, authUser)
    else:
        return redirect('/')
    return redirect('/wall')

def wall(request):
    messageForm = MessageForm()
    # 2. render messages

    messageBoard = Message.objects.all()

    context = {
        "messageForm": messageForm,
        "messageBoard": messageBoard
    }

    return render(request, 'The_Wall/wall.html', context)

def messageR(request):
    newMessage = MessageCreateForm(request.POST)
    # validation of form
    if newMessage.is_valid():
        
        newMessage.user_id = request.user.id
        print "got to here!"
        print request.user.id
        print newMessage.user_id
        # call .save method to store in model
        print newMessage.cleaned_data
        saveMessage = newMessage.save(commit=False)
        print saveMessage
        saveMessage.user = request.user.id
        saveMessage.save()
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

