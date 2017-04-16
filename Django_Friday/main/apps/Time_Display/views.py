# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    # dictionary we can pass values through
    dateTime = datetime.now
    context = {
        "testKey" : dateTime
    }
    return render(request, "Time_Display/index.html", context)

def testform(request):
    if request.method == "POST":
        # add testSession variable equal to test_var from POST
        request.session['testSession'] = request.POST['test_var']
        print request.POST
        print request.method
        return redirect("/")
    else:
        return redirect("/")

    return render(request, "Time_Display/")

# request.session is a dictionary
# request.session['key'] : gets value in key
# request.session['key'] = 'value : set value of key
# del request.session['key'] : deletes a session key if it exists
# 'key' in request.session : returns boolean if 'key' is in session
# {{ request.session.'key'}} : access session data