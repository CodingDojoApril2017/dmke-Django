# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Models ---

# Class to describe Message model
class Message(models.Model):
    user = models.ForeignKey(User)
    messageText = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

# Class to describe MessageForm object, related to Message model

# Class to describe Comment model
class Comment(models.Model):
    user = models.ForeignKey(User)
    message = models.ForeignKey(Message)
    commentText = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

# Class to describe CommentForm object, related to Comment model
# !Q - shouldn't this be in forms?
    

## !R - self and super in class/methods

# Each model has at least one "Manager" and it's called 'objects' by default.
# I.E. Comment.objects
# class Manager - A "Manager" is the interface through which db query operations are provided to Django models

# Adding extra managers is the preferred way to add "table-level" functionality to your models
# For "row-level" functionality, i.e., functions that on on a single instance of a model object (One 'Comment' object vs all 'Comment' objects) use Model methods

# Method overriding in Python
# Inheritance + customization
# Inherit methods from class, override to provide new functionality

# Django uses SQL-lite
# Use postgresql to scale
# CRUD - Create Read Update Delete

# clear() to clear object list - Comment.objects.clear() would clear Comment objects
# Deprecated due to built-in Django stuff
# def validateLengthGreaterThanTwo(value):
#     if len(value) < 3:
#         raise ValidationError(
#             '{} must be longer than: 2'.format(value)
#         )

# Deprecated notes
# ----
# class UsersManager(models.Manager):
#     # login function pulls in POST data from client
#     def login(self, postData):
#         #  "run login function"
#         #  "success: return user object"
#         #  "else: return entry to errors list
#         pass
#     def register(self, postData):
#         pass
#         # register user
#         # return user object
#         # else return entry to errors list

# # ORM is like a linkedlist!

# # deprecate, using Django built-in 'User'
# class Users(models.Model):
#     #    first_name = models.CharField(max_length=255, validators = [validateLengthGreaterThanTwo])
#     first_name = models.CharField(max_length=255)
#     #     last_name = models.CharField(max_length=255, validators = [validateLengthGreaterThanTwo]
#     last_name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)

#     # Connect UsersManager to users model, objects key now has UsersManager attributes and methods
#     objects = UsersManager()

#     # magic method to apply logic if a Users object is being converted into a string
#     def __str__(self):
#         return self.first_name + " " + self.last_name

# NoSQL quick data dumping
# SQL retrievals

    
