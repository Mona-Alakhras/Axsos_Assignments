from django.shortcuts import render , redirect
from .models import User

# Create your views here.

def index(request):
    context = {
        "all_users" : User.objects.all()
    }
    return render(request, "index.html",context)

def add_user(request):
    if request.method == "POST":
       first = request.POST.get('first_name')
       last = request.POST.get('last_name')
       email = request.POST.get('email')
       age = request.POST.get('age')

       User.objects.create(
        first_name = first,
        last_name = last,
        email_address = email,
        age = age
       )
    return redirect('/')   