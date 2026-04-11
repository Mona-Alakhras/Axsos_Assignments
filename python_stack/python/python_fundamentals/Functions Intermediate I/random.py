import random
def rand_int(min=0  , max= 100 ):
    num = random.random() * (max - min) + min
    return num
print(rand_int())   
print(rand_int(max = 50))
print(rand_int(min = 50 , max = 100))
print(rand_int(min = 50 , max = 500)) 
