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
    userWhoPosted = models.ManyToManyField(User, related_name="publishers")
    secretMessage = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
