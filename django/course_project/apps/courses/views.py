from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages

from models import *

def new(request):
    course = Course.objects.all()
    context = {
        "courses": course
    }
    return render(request, 'courses/index.html', context )

def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            print error
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        Course.objects.create(name=request.POST['name'])
        c = Course.objects.last()
        d = Description(desc_course=request.POST['desc'], course = c)
        d.save()
        return redirect('/')

def comments(request, id):
    course = Course.objects.get(id=id)
    context = {
        "course": course,
        "comments": course.comments.order_by("-created_at")
    }
    return render(request,"courses/comments.html", context )

def newcomment(request, id):
    errors = Comment.objects.comment_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            print error
            messages.error(request, error, extra_tags=tag)
        return redirect('/courses/'+str(id)+'/comments')
    else:
        Comment.objects.create(comment=request.POST['comment'],
                               course=Course.objects.get(id=id))
        return redirect('/courses/'+str(id)+'/comments')

def confirmation(request, id):
    course = Course.objects.get(id=id)
    context = {
        "course": course,
        "comments": course.comments.order_by("-created_at")
    }
    return render(request, 'courses/destroy.html', context )

def destroy(request, id):
    c = Course.objects.get(id = id)
    if c:
        c.delete()
    return redirect('/')
