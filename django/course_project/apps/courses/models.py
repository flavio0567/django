from __future__ import unicode_literals

from django.db import models

import re

name_regex = re.compile(r'^(?=.*\S).+$')

class CourseManager(models.Manager):
    def basic_validator(self, postData):
            errors = {}
            if len(postData['name']) < 5 or not name_regex.match(postData['name']):
                errors["name"] = "Please enter a valid course name"
            if len(postData['desc']) < 15 or not name_regex.match(postData['desc']):
                errors["desc"] = "Please enter a valid description"
            return errors

class CommentManager(models.Manager):
    def comment_validator(self, postData):
            errors = {}
            if len(postData['comment']) < 5 or not name_regex.match(postData['comment']):
                errors["comment"] = "Please enter a valid comment"
            return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "{} {}".format(self.name, self.created_at)
    objects = CourseManager()

class Description(models.Model):
    desc_course = models.TextField()
    course = models.OneToOneField(
        Course,
        related_name = 'desc',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "{}".format(self.desc_course)
    objects = CourseManager()

class Comment(models.Model):
    comment = models.TextField()
    course = models.ForeignKey(Course, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
       	return "{}".format(self.comment)
    objects = CommentManager()
