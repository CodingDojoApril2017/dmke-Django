# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Model functions
def validateLengthGreaterThanTwo(value):
    if len(value) < 3:
        raise ValidationError(
            '{} must be longer than: 2'.format(value)
        )


# Create your models here.
class UsersManager(models.Manager):
    # login function pulls in POST data from client
    def login(self, postData):
        #  "run login function"
        #  "success: return user object"
        #  "else: return entry to errors list
        pass
    def register(self, postData):
        pass
        # register user
        # return user object
        # else return entry to errors list

# ORM is like a linkedlist!

class Users(models.Model):
    #    first_name = models.CharField(max_length=255, validators = [validateLengthGreaterThanTwo])
    first_name = models.CharField(max_length=255)
    #     last_name = models.CharField(max_length=255, validators = [validateLengthGreaterThanTwo]
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    # Connect UsersManager to users model, objects key now has UsersManager attributes and methods
    objects = UsersManager()

    # magic method to apply logic if a Users object is being converted into a string
    def __str__(self):
        return self.first_name + " " + self.last_name

class Messages(models.Model):
    user_id = models.ForeignKey(Users)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comments(models.Model):
    users_id = models.ForeignKey(Users)
    messages_id = models.ForeignKey(Messages)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    




    
