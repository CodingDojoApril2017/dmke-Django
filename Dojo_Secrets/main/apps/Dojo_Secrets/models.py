# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

# Using Django User model

#
class Secret(models.Model):
    userWhoPosted = models.ForeignKey(User)
    userWhoLiked = models.ManyToManyField(User, related_name="likers")
    secretMessage = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    # call method in template (to test for fun)
    # def testThisMethod(self):
        
class Like(models.Model):
    user = models.ForeignKey(User)
    secretMessage = models.ManyToManyField(Secret, related_name="secret_for_like")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create Like, add user_id
# links like 
# Like.secretMessage(secrets_id)
# Like.user_id(request.user.id)
# Adds current user_id to the clicked secret message

## Django notes
## Dictionary lookup. Example: foo["bar"]
## Attribute lookup. Example: foo.bar
## List-index lookup. Example: foo[bar]
## 

# Row is a new object
# Columns are the attributes of each object
#
# Django templating is powerful

# <ul>
# {% for athlete in athlete_list %}
#     <li>{{ athlete.name }}</li>
# {% endfor %}
# </ul>
# You can loop over a list in reverse by using {% for obj in list reversed %}.

# If you need to loop over a list of lists, you can unpack the values in each sublist into individual variables. For example, if your context contains a list of (x,y) coordinates called points, you could use the following to output the list of points:

# {% for x, y in points %}
#     There is a point at {{ x }},{{ y }}
# {% endfor %}
# This can also be useful if you need to access the items in a dictionary. For example, if your context contained a dictionary data, the following would display the keys and values of the dictionary:

# {% for key, value in data.items %}
#     {{ key }}: {{ value }}
# {% endfor %}