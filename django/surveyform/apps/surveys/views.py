from django.shortcuts import render, redirect

def index(request):
    return render(request, 'surveys/index.html')

def process(request):
    print 222222
    try:
        request.session['attempt']
    except KeyError:
        request.session['attempt'] = 0
    request.session['name'] = request.POST['inputName']
    request.session['location'] = request.POST['selectLoc']
    request.session['language'] = request.POST['selectLang']
    request.session['comment'] = request.POST['comment']
    request.session['attempt'] += 1
    return redirect('/result')


def result(request):
    return render(request, 'surveys/result.html')
