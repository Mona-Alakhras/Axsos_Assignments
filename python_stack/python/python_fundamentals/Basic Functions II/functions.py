#Countdown
def count_down(number):
    output = []
    for i in range(number,-1,-1):
        output.append(i)
    return output
print(count_down(5))  

#print and return
def print_and_return(list):
    print (list[0])
    return list[1]
print(print_and_return([1,2]))   

#first plus length
def first_plus_length(list):
    first_value = list[0]
    len_list = len(list)
    return first_value + len_list
print(first_plus_length([1,2,3,4,5]))    

#Values grater than second
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    grater_list = []
    second_val = list[1]    
        
    for i in range(0,len(list)):
            if list[i] > second_val:
                grater_list.append(list[i])
    return grater_list                            
print(values_greater_than_second([5,2,3,2,1,4]))

#this length , that value
def length_and_value(size,value):
    new_list = []
    for i in range (size):
        new_list.append(value)

    return new_list
print(length_and_value(4,7))    

