# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.

def index(request):

    # creates totalGold and activity in session
    if not "totalGold" in request.session:
        request.session['totalGold'] = 0
    if not "activity" in request.session:
        request.session['activity'] = []
    context = {
        'gold':request.session['totalGold']
    }
    # store session data in context object to pass to template and limit use of session
    return render(request,'Ninja_Gold/index.html', context)

def process(request, place):
    # receive place from URL
    print "Made it to process"
    # process place by assigning gold 
    goldEarned = 0
    if place == "farm":
        goldEarned = randint(10,21)
    if place == "cave":
        goldEarned = randint(5,11)
    if place == "house":
        goldEarned = randint(2,6)
    if place == "casino":
        goldEarned = randint(-50,50)
    
    # add processed place (gold earned) to total gold in session
    request.session['totalGold'] = request.session['totalGold'] + goldEarned
    activityDate = datetime.now
    print request.session['totalGold']
    request.session['activity'].append([{'{} {} {}', place,activityDate, goldEarned])
    #redirect to root route
    return redirect('/')


