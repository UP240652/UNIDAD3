
import math


first_name = 'Fernanda'
last_name = 'Rodriguez'
full_name = first_name + ' ' + last_name
country = 'USA'
city = 'Snohomish'
age = 20
year = 2025
is_married = True
is_true = True
is_light_on = False


x, y, z = 10, 20, 30


skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname': first_name,
   'lastname': last_name,
   'country': country,
   'city': city
}


print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(skills))
print(type(person_info))


first_name_len = len(first_name)
last_name_len = len(last_name)
print(first_name_len > last_name_len)  


num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two  
prod = num_two * num_one
div = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two


radius = 30
area_of_circle = math.pi * radius**2
circum_of_circle = 2 * math.pi * radius


radius = int(input("Ingresa el radio: "))
area_of_circle = math.pi * radius**2
circum_of_circle = 2 * math.pi * radius

first_name = input("Ingresa tu primer nombre: ")
last_name = input("Ingresa tu apellido: ")
country = input("Ingresa tu país: ")
age = int(input("Ingresa tu edad: "))


help('keywords')
