from django.shortcuts import render , redirect
import random
from datetime import datetime


# Create your views here.
def index(request):
    if 'number_gold' not in request.session:
        request.session['number_gold'] = 0
        request.session['activities'] = []
    return render(request, 'index.html')   

def process_money(request): 
    if 'number_gold' not in request.session:
        request.session['number_gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = [] 
    if request.method == "POST":
        building = request.POST.get('building')
        now_str = datetime.now().strftime("%Y/%m/%d %I:%M %p")
        gold_change = 0
        
        if building == 'farm':
            gold_change = random.randint(10, 20)
        elif building == 'cave':
            gold_change = random.randint(10, 20)
        elif building == 'house':
            gold_change = random.randint(10, 20)
        elif building == 'quest':
            gold_change = random.randint(-50, 50) 

        request.session['number_gold'] += gold_change
        if gold_change >= 0:
            activity_text = f"You entered a {building} and earned {gold_change} gold. ({now_str})" 
            color = "green"
        else:
            activity_text = f"You failed a {building} and lost {gold_change}. Ouch ({now_str})" 
            color = "red"
        activities = request.session.get('activities' , [])    
        activities.insert(0,
        {'text':activity_text, 'color': color}) 
        request.session['activities'] = activities
        request.session.modified = True
    return redirect('/') 

def reset(request):
    request.session.flush() 
    return redirect('/')   

