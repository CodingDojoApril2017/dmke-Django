## -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect

## Using Django auth, login, and user classes
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
## Class based forms derived from models
from django.forms import ModelForm
## Using Django view Classes
from django.views import generic
## To view Django to SQL queries
from django.db import connection
# from django.contrib.auth.decorators import login_required

from .forms import UserCreateForm



## Rendering views
def index(request):
    print "routed to index"
    registerFormToRender = UserCreateForm()
    context={
        "registerForm":registerFormToRender,"loginForm":loginFormToRender
    }

    return render(request, "Login_Reg/index.html", context)

def renderHome(request):
    print "routed to renderHome"
    #print connection.queries

    allUsers = User.objects.all()

    context= {
        "allUsers":allUsers
    }
    #
    for users in allUsers:
        print users.id

    return render(request, 'dmke-Django/home.html', context)

## Classes

"""
Generic class-based view for a list of Users, included for debugging purposes
"""
class UserListView(generic.ListView):
    model = User
    paginate_by = 5
    # template_name = 'dmke-Django/home.html'

## Functions, redirecting
def register(request):
    print "routed to register"
    newUser = UserCreateForm(request.POST)
    if newUser.is_valid():
        user = newUser.save(commit=False)
        user.save()
        print "Valid"
        return redirect('/renderHome')
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

    return redirect('/renderHome')


#@login_required(login_url='/')
# def login_success(request):
#     return render(request,"ourApp/show.html")
