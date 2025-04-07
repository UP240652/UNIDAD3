#1
dog = {}

#2
dog = {'name':'Cocacola',
       'color':'cafesito',
       'breed':'Chihuahua',
       'legs':4,
       'age':1}

#3
student = {
    'first_name':'Fernanda',
    'last_name':'Rodriguez',
    'gender':'Female',
    'age':20,
    'marital_status':'single',
    'skills':['Python','SQL','HTML','CSS','JS'],
    'country':'England',
    'city':'London',
    'addres':{
        'street':'Baker Street',
        'zipcode':'NW1 6XE',
    }
}

#4
print(f'The lenght of the student dictionary is {len(student)}')

#5
print(f'The data type of student skills is {type(student["skills"])}')

#6
student['skills'].append('PHP')
print(student['skills'])

#7
keyList = list(student.keys())
print(keyList)

#8
valList = list(student.values())
print(valList)

#9
studentTuple = student.items()
print(studentTuple)

#10
student.pop('gender')
print(student)

#11
del dog
