# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

#If I extend User, do I have to import my models/class that extends User or does importing django / User grab it all?

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Reviews(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Books)
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
