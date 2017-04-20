# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.forms import ModelForm
from .forms import UserCreateForm, SecretCreateForm, LikeCreateForm, LoginForm
from .models import Secret
# Import authenticate and login to use
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.db import connections

## Views that render HTML pages ---

def index(request):
    print "routed to index"
    loginFormToRender = LoginForm()
    registerFormToRender = UserCreateForm()
    context= {
        "registerForm":registerFormToRender,
        "loginForm":loginFormToRender
    }
    return render(request, 'Dojo_Secrets/index.html', context)

def renderSecrets(request):
    print "routed to renderSecrets"
    secretFormToRender = SecretCreateForm()
    allSecrets = Secret.objects.all()
    # allLikes = Like.

    context= {
        "secretForm":secretFormToRender,
        "allSecrets":allSecrets
    }
    #
    for secrets in allSecrets:
        print secrets.secretMessage
        print secrets.userWhoLiked
        #print secrets.userWhoPosted

    #testC = connections.queries
    #print testC
    return render(request, 'Dojo_Secrets/Secret.html', context)

## Functional views

def addSecret(request):
    print "routed to addSecret"
    newSecret = SecretCreateForm(request.POST)
    print newSecret
    if newSecret.is_valid():
        saveSecret = newSecret.save(request.user.id, commit=False)
        saveSecret.save()
    return redirect('/renderSecrets')

def like_secrets(request, secrets_id):
    print "routed to likeSecret"
    print "secrets id:", secrets_id
    # Create Like
    newLike = LikeCreateForm(secrets_id, request.user.id,)


    return redirect('/renderSecrets')

def register(request):
    print "routed to register"
    newUser = UserCreateForm(request.POST)
    if newUser.is_valid():
        user = newUser.save(commit=False)
        user.save()
        print "Valid"
        return redirect('/renderSecrets')
    else:
        print "Not valid"
        return redirect('/')

def login(request):
    print "routed to login"
    authUser=authenticate(username=request.POST['username'], password=request.POST['password'])
    if authUser:
        print "User authenticated"
        auth_login(request, authUser)
    else:
        print "Unauth"
        return redirect('/')

    return redirect('/renderSecrets')


# Get an object,
# getLike = Like.objects.get(pk=1)
# Change an existing Like
# form = ArticleForm(instance=article)

