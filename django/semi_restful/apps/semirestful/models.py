from __future__ import unicode_literals
from django.db import models
import re

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_regex = re.compile(r'^(?=.*\S).+$')


class UserManager(models.Manager):
    def basic_validator(self, postData):
            errors = {}
            if len(postData['first_name']) == 0 or not name_regex.match(postData['first_name']):
                errors["first_name"] = "Please enter a valid first name"
            if len(postData['last_name']) == 0 or not name_regex.match(postData['last_name']):
                errors["last_name"] = "Please enter a valid last name"
            if len(postData['email']) == 0 or not email_regex.match(postData['email']):
                errors["email"] = "Please enter a valid email"
            if len(errors) == 0:
                user = User.objects.filter(email_address = postData['email'])
                if len(user) and postData['update'] != 'update':
                    errors["email"] = "Email already exists!"
            return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "<User object {} {} {} {}".format(self.first_name, self.last_namem, self.email, self.created_at)
    objects = UserManager()
