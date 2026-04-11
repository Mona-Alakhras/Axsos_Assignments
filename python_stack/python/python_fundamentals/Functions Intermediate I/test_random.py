import random
def rand_int(min=0  , max= 100 ):
    if min > max:
        min , max = max , min
    if max < 0:
        return "error : max must be greater than 0"    
    num = random.random() * (max - min) + min
    return round(num)
print(rand_int())   
print(rand_int(max = 50))
print(rand_int(min = 50 , max = 100))
print(rand_int(min = 50 , max = 500))
print(rand_int(min = 500 , max = 50)) 
