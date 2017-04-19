# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.forms import ModelForm
from .forms import UserCreateForm, SecretCreateForm, LoginForm 

# Import authenticate and login to use
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.


def index(request):
    print "routed to index"
    loginForm = LoginForm()
    registerForm = UserCreateForm()
    context= {
        "registerForm":registerForm,
        "loginForm":loginForm
    }
    return render(request, 'Dojo_Secrets/index.html', context)

def renderSecrets(request):
    secretFormToRender = SecretCreateForm()


def register(request):
    print "routed to register"
    newUser = UserCreationForm(request.POST)
    if newUser.is_valid():
        user = newUser.save(commit=False)
        user.save()
        print "Valid"
        return redirect('/renderSecrets')
    else:
        print "Not valid"
        return redirect('/index')


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





