from __future__ import unicode_literals
from django.shortcuts import render, redirect
from datetime import datetime
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = []

    return render(request, 'ninjagold/index.html')

def process_money(request):
    timestamp = datetime.now().strftime("%Y/%m/%d %I:%M %p")
    if  request.POST['action'] == 'farm':
        earns = random.randrange(10, 21)
        request.session['gold'] += earns 
        request.session['activity'].append(['earn', 'Earned {} golds from the {}! ({})'.format(earns, 'farm', timestamp)])
        # return render(request, 'ninjagold/index.html')
    elif request.POST['action'] == 'cave':
        print 'entrei na cave'
        earns = random.randrange(5, 11)
        request.session['gold'] += earns 
        request.session['activity'].append(['earn', 'Earned {} golds from the {}! ({})'.format(earns, 'cave', timestamp)])
    elif  request.POST['action'] == 'house':
        earns = random.randrange(2, 6)
        request.session['gold'] += earns 
        request.session['activity'].append(['earn', 'Earned {} golds from the {}! ({})'.format(earns, 'house', timestamp)])
    elif  request.POST['action'] == 'casino':
        earns = random.randrange(-50, 50)
        if earns > 0:
            request.session['gold'] += earns 
            request.session['activity'].append(['earn', 'Earned {} golds from the {}! ({})'.format(earns, 'casino', timestamp)])
        else:
            request.session['gold'] += earns 
            request.session['activity'].append(['lost', 'Entered a casino and lost {} golds... Ouch! ({})'.format(earns , timestamp)])     
    return redirect('/')

def clear(request): 
    request.session['gold'] = 0
    request.session['activity'] = []
    return redirect('/')
