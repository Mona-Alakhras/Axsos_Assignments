#update values
x = [[5,2,3], [10,8,9]]
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
'basketball': ['Kobe', 'Jordan','James','Curry'],
'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

#1
x[1][0] = 15
print(x)
#2
students[0]['last_name'] = 'Bryant'
print(students)
#3
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
#4
z[0]['y']=30
print(z)

#iterate1
def iterateDictionary(some_list):
    for elements in some_list:
        output = []
        for key , value in elements.items():
            output.append(f"{key} - {value}")
        print(", ".join(output))    

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

print(iterateDictionary(students))


#iterate2
def iterateDictionary2(key_name,some_list):
    for elements in some_list:
        print(elements[key_name])
print(iterateDictionary2('first_name' , students))


#iterate3
def printInfo(some_dict):
    for key, val_list in some_dict.items():
        print(f"{len(val_list)} {key.upper()}")
        for item in val_list:
            print(item)
        print("")

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC','Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh','Devon']
}

printInfo(dojo)


