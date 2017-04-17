# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

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

    return render(request, 'The_Wall/index.html')

# Extra notes:
# .filter returns a queryset list
# .exclude, ooposite of filter
#  conditions: __startswith="S", __contains="E"
# queries can be changed
# same query can accept multiple arguments
# | or can be used

def register(request):

    # Django models
    query = "Select * FROM users WHERE email = :email;"

    # validation of form

    return redirect('The_Wall/wall.html')

def login(request):
    # Django models to query user/email

    # validate password from form/POST

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

