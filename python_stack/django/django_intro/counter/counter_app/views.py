from django.shortcuts import render, redirect

def index(request):
    if 'visits' in request.session:
        request.session['visits'] += 1
    else:
        request.session['visits'] = 1

    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1

    return render(request, 'index.html')

def destroy_session(request):
    if 'counter' in request.session:
        del request.session['counter']
    if 'visits' in request.session:
        del request.session['visits']
    return redirect('/')

def plus_two(request):
    if 'counter' in request.session:
        request.session['counter'] += 1 
    return redirect('/')






