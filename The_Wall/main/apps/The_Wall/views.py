# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
# Import forms and models
from .forms import UserCreateForm, LoginForm, MessageCreateForm, MessageForm, CommentCreateForm, CommentForm
from .models import Message, Comment
# Import Django's prebuilt Users model
from django.contrib.auth.models import User
# User: username, password, email, first_name, last_name

# Views ---

# Root route, send LoginForm object and UserCreateForm object for rendering to client in index.html
def index(request):
    loginForm = LoginForm()
    registerForm = UserCreateForm()
    return render(request, 'The_Wall/index.html', {"registerForm":registerForm, "loginForm":loginForm})

# Register route, receives POST form data passed from client through UserCreateForm object
# Saves new User object in database
def register(request):
    newUser = UserCreationForm(request.POST)
    if newUser.is_valid():
        user = newUser.save(commit=False)
        user.save()
        return redirect('/wall')
    else:
        return redirect('/')

# Login route, receives POST form data passed from client through LoginForm object
# TODO__ Add error message on unauthorized
def login(request):
    authUser=authenticate(username=request.POST['username'], password=request.POST['password'])
    if authUser:
        auth_login(request, authUser)
    else:
        return redirect('/')

    return redirect('/wall')

# Wall.html render route, send MessagForm and CommentForm objects for rendering to client in wall.html
# Send all Message and Comment objects to wall.html
def wall(request):
    messageForm = MessageForm()
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

# MessageR route, receives POST form data from client through MessageCreateForm object
# Saves new Message object in database
def messageR(request):
    newMessage = MessageCreateForm(request.POST)
    if newMessage.is_valid():
        saveMessage = newMessage.save(request.user.id, commit=False)
        saveMessage.save()
    return redirect('/wall')

# CommentR route, receives POST form data from client through CommentCreateForm object
# Saves new Comment object in database
def commentR(request):
    newComment = CommentCreateForm(request.POST)
    msg_id = request.POST['msgid']
    if newComment.is_valid():
        saveComment = newComment.save(request.user.id, msg_id, commit=False)
        saveComment.save()
    return redirect('/wall')

# Some Django notes
# ... When rendering an object in Django:
# 1. Get a hold of it in the view (fetch from DB, ie.)
#2. pass it to the template context (data structure)
#3. expand it to HTML markup using template variables

# Extra notes:
# .filter returns a queryset list
# .exclude, ooposite of filter
#  conditions: __startswith="S", __contains="E"
# queries can be changed
# same query can accept multiple arguments
# | or can be used

