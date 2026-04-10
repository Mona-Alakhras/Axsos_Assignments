#Basic
for i in range(0, 150,1):
    print(i)


#Multiples of 5
for i in range(5, 1000, 5):
    print(i)

#Counting, the Dojo way
for i in range(1,101):
    if i % 5 == 0:
        print("Coding instead")
    elif i % 10 == 0:
        print("Coding Dojo") 
    else:
        print(i)

#Whoa. That Sucker's Huge
sum = 0
for i in range(500000):
    if i%2 != 0:
        sum += i
print(sum) 

#Countdown by Fours
for i in range(2018,0,-4):
    print(i)

#Flexible Counter
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum , highNum+1):
    if i % mult == 0:
        print(i)