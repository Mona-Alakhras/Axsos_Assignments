from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Course, Description, Comment

def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST)
        
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        
        desc_obj = Description.objects.create(content=request.POST['description'])
        
        Course.objects.create(
            name=request.POST['name'],
            description=desc_obj
        )
        return redirect('/')
    return redirect('/')

def confirm_delete(request, course_id):
    context = {
        'course': get_object_or_404(Course, id=course_id)
    }
    return render(request, 'delete.html', context)

def delete(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.delete() 
    return redirect('/')

def add_comment(request, course_id):
    if request.method == "POST":
        course_obj = get_object_or_404(Course, id=course_id)
        Comment.objects.create(
            content=request.POST['comment_text'],
            course=course_obj
        )
    return redirect('/')
