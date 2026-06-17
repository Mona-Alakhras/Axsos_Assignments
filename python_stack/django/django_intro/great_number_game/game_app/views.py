from django.shortcuts import render , redirect
import random 

# Create your views here.
def index(request):
    if 'target_number' not in request.session:
        request.session['target_number'] = random.randint(1, 100)
        request.session['attempts'] = 0
        request.session['status'] = None
    return render(request, 'index.html')


def guess(request):
    if request.method == "POST": 
        user_guess = request.POST.get('user_guess') 
        
        if user_guess and user_guess.isdigit(): 
            request.session['attempts'] += 1   
            
            guess_num = int(user_guess) 
            target = request.session['target_number'] 
            if guess_num < target:
                request.session['status'] = 'low'   
            elif guess_num > target:
                request.session['status'] = 'high'  
            else:
                request.session['status'] = 'correct' 
            if request.session['attempts'] >= 5 and request.session['status'] != 'correct':
                request.session['status'] = 'lose'

    return redirect('/') 
            

def reset(request):
    request.session.flush() 
    return redirect('/')   