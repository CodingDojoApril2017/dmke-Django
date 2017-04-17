# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import RegisterForm

# Imports Users class/object from models file
from .models import Users

# Create your views here.
def index(request):
    # login / register page

    # query to Users, objects.login method passing in POST DATA 
    # query example (getter):
    # user = User.objects.get(id=6)
    # context = {"users": user}

    # user = Users.objects.login( POST DATA)
    # if 'error in user:
    #   pass
    # if 'theuser' in user:
    #   pass

    # Create form from forms class, pass to index through context
    form = RegisterForm()
    context = { "regForm": form}

    return render(request, 'The_Wall/index.html', context)

# Extra notes:
# .filter returns a queryset list
# .exclude, ooposite of filter
#  conditions: __startswith="S", __contains="E"
# queries can be changed
# same query can accept multiple arguments
# | or can be used

def register(request):
    ## Check for POST and bind form
    # if request.method == "POST":
    #     bound_form = RegisterForm(request.POST)




    # Django models
    ## returns user object or none
    # isUser=authenticate(username=request.POST['username'], password='request.POST['password']')
    ## if isUser proceed with login


    # form = RegisterForm()


    # validation of form

    return redirect('The_Wall/wall.html')

def login(request):
    ##Django models to query user/email
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
    return redirect('/')

def wall(request):
    context = {

    }
    # Request message and comment data and send to client/display on the wall

    return render('The_Wall/wall.html', context)

def message(request):
    # Add message to database using models
    return redirect('The_Wall/wall.html')

def comment(request):
    # add id to arguments
    # / message id 

    # query Message object for id
    # comment = Message.objects.get(id=id)

    # add comment to comment model
    # Comment.objects.create(comment=request.POST['comment'],message=message)
    return redirect('The_Wall/wall.html')

# Some Django notes
# ... When rendering an object in Django:
# 1. Get a hod of it in the view (fetch from DB, ie.)
#2. pass it to the template context (data structure)
#3. expand it to HTML markup using template variables

