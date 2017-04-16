# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "Survey_Form/index.html")

def process(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comments'] = request.POST['comments']

    # request.session['data'] = {
    #     "Name": request.POST['name'],
    #     "Location": request.POST['location'],
    #     "Language": request.POST['language'],
    #     "Comments": request.POST['comments']
    # }

    return redirect('/result')

def result(request):
    print request.session
    return render(request, 'Survey_Form/result.html')


