# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'Hello_World/index.html')



def projects(request):
    return render(request, 'Hello_World/projects.html')

def aboutme(request):
    return render(request, 'Hello_World/aboutme.html')

def testimonials(request):
    print "test"
    return render(request, 'Hello_World/testimonials.html')