#Biggie Size
def biggie_size(list):
    new_val = "big"
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = new_val
    return list
print(biggie_size([-1,3,5,-5]))  

#count positives
def count_positive(list):
    num_of_positive_numbers = 0
    for i in range(len(list)):
        if list[i] > 0:
            num_of_positive_numbers += 1
    list[len(list)-1] = num_of_positive_numbers    
    return list
print(count_positive([1,6,-4,-2,-7,-2]))  

#Sum Total 
def sum_total(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum
print(sum_total([1,2,3,4]))   
print(sum_total([6,3,-2]))  

#average
def average(list):
    average = 0
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    average = sum / len(list)
    return average
print(average([1,2,3,4]))    

#length
def length(list):
    length = len(list)
    if length == 0:
        return False
    num_of_len = length
    return num_of_len
print(length([37,2,1,-9]))  
print(length([]))  

#minimum
def minimum(list):
    length = len(list)
    if length == 0:
        return False
    min_val = list[0]    
    for i in range(length):
        if list[i] < min_val:
            min_val = list[i]
    return min_val
print(minimum([37,2,1,-9]))  
print(minimum([])) 

#maximum
def maximum(list):
    length = len(list)
    if length == 0:
        return False
    max_val = list[0]    
    for i in range(length):
        if list[i] > max_val:
            max_val = list[i]
    return max_val
print(maximum([37,2,1,-9]))  
print(maximum([])) 

#ultimate analysis
def ultimate_analysis(list):
    result = {}
    sumTotal = 0
    average = 0
    length = len(list)
    max_val = list[0]
    min_val = list[0]
    for i in range(length):
        sumTotal += list[i]
        average = sumTotal/length
        if list[i] > max_val:
            max_val = list[i]
        if list[i] < min_val:
            min_val = list[i]
    result = {
        'sum Total': sumTotal ,
        'average':average ,
        'minimum': min_val ,
        'maximum': max_val ,
        'length':length
        }
    return result     

print(ultimate_analysis([37,2,1,-9]))

#reverse list
def reverse_list(list):
    length = len(list)
    for i in range(0, length // 2):
        temp = list[i]
        list[i] = list[length - 1 - i]
        list[length - 1 - i] = temp    
    return list

print(reverse_list([37, 2, 1, -9]))
      
