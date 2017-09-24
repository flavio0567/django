from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from models import *

def users(request):
    return render(request, 'semirestful/index.html', { "users" : User.objects.all() })

def new(request):
    return render(request, 'semirestful/new.html')

def show(request, id):
    print 'entrei show'
    if request.method == 'POST':
        return update(request, id)
    else:
        return render(request, 'semirestful/show.html', { "user" : User.objects.get(id = id)} )

def create(request):
    print ' entrei create'
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            print error
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/new')
    else:
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_address=request.POST['email'])
        id = User.objects.last().id
    return redirect('/users/'+str(id))

def edit(request, id):
    return render(request, 'semirestful/edit.html', { "user" : User.objects.get(id = id)} )

def update(request, id):
    print 'entrei update'
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/'+id+'/edit')
    else:
        user = User.objects.get(id = id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email_address = request.POST['email']
        user.save()
        return redirect('/users/'+str(id))

def destroy(request, id):
    print 'entrei destroy'
    u = User.objects.get(id = id)
    if u:
        u.delete()
    return redirect('/')

