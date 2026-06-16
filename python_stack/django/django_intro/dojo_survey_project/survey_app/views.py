from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'survey_form.html')

def result(request):
    if request.method == "POST":
        print(request.POST)
        context = {
            "name": request.POST.get('name'),
            "location": request.POST.get('location'),
            "language": request.POST.get('language'),
            "comment": request.POST.get('comment'),
            "experience": request.POST.get('experience'),
            "interests": request.POST.getlist('interests')
        }
        return render(request, 'result.html',context)
    return redirect('/')
