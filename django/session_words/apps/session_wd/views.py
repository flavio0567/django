from __future__ import unicode_literals
from django.shortcuts import render, redirect
from datetime import datetime

def index(request):
    return render(request, 'session_wd/index.html')

def word(request):
    myList = {}
    for key, val in request.POST.iteritems():
        if key != "csrfmiddlewaretoken"  and key !="bigword":
            myList[key] = val
        if key == 'bigword':
            myList['size'] = 'big'
            
    myList['created_at'] = datetime.now().strftime("%I:%M %p, %B %d, %Y")

    try:
        request.session['data']
    except KeyError:
        request.session['data'] = []
    
    temp = request.session['data']
    temp.append(myList)
    request.session['data'] = temp

    return redirect('/')

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')
