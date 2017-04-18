# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm

from .forms import UserCreateForm, LoginForm, MessageCreateForm, MessageForm, CommentCreateForm, CommentForm

## Imports Users class/object from models file
# from .models import Users

# Import Django's prebuilt Users model
from django.contrib.auth.models import User
# User: username, password, email, first_name, last_name
from .models import Message, Comment

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
    commentForm = CommentForm()
    messageBoard = Message.objects.all()
    commentBoard = Comment.objects.all()

    context = {
        "messageForm": messageForm,
        "messageBoard": messageBoard,
        "commentForm": commentForm,
        "commentBoard": commentBoard
    }

    return render(request, 'The_Wall/wall.html', context)

def messageR(request):
    newMessage = MessageCreateForm(request.POST)
    # validation of form
    if newMessage.is_valid():
        # call .save method to store in model
        saveMessage = newMessage.save(request.user.id, commit=False)
        saveMessage.save()
    return redirect('/wall')

def commentR(request):
    # add id to arguments
    # / message id 
    newComment = CommentCreateForm(request.POST)
    print request.POST['msgid']
    msg_id = request.POST['msgid']
    # validation of form
    if newComment.is_valid():
        # call .save method to store in model
        saveComment = newComment.save(request.user.id, msg_id, commit=False)
        saveComment.save()

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

