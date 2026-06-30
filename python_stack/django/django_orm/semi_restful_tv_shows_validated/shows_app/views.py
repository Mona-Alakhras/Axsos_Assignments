from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Show

def index(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST)
        
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new') # إعادة التوجيه لصفحة الإضافة لإظهار الأخطاء
        
        new_show = Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            description=request.POST['description']
        )
        return redirect(f'/shows/{new_show.id}')
    return redirect('/shows')

def show_detail(request, show_id):
    context = {
        'show': get_object_or_404(Show, id=show_id)
    }
    return render(request, 'show_detail.html', context)

def edit(request, show_id):
    context = {
        'show': get_object_or_404(Show, id=show_id)
    }
    return render(request, 'edit.html', context)

def update(request, show_id):
    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST, show_id=show_id)
        
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/{show_id}/edit')
        
        show = get_object_or_404(Show, id=show_id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
        
        return redirect(f'/shows/{show.id}')
    return redirect('/shows')

def destroy(request, show_id):
    show = get_object_or_404(Show, id=show_id)
    show.delete()
    return redirect('/shows')