age = 20
height = 1.67 
comple = 1+ 9j

a = int(input())
b = int(input())
area = (a*b)/2
print(area)

c = int(input())
d = int(input())
e = int(input())
perimeter = c+d+e

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print(f"Rectangle Area: {area_rectangle}")
print(f"Rectangle Perimeter: {perimeter_rectangle}")

radius = float(input("Enter the radius of the circle: "))
pi = 3.14
area_circle = pi * radius * radius
circumference_circle = 2 * pi * radius
print(f"Circle Area: {area_circle}")
print(f"Circle Circumference: {circumference_circle}")

slope = 2
y_intercept = -2
x_intercept = -y_intercept / slope
print(f"Slope: {slope}")
print(f"Y-intercept: {y_intercept}")
print(f"X-intercept: {x_intercept}")

x1, y1 = 2, 2
x2, y2 = 6, 10
slope_points = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(f"Slope between points (2, 2) and (6, 10): {slope_points}")
print(f"Euclidean distance between points (2, 2) and (6, 10): {distance}")

print(f"Comparing slopes: {slope == slope_points}")

def find_y(x):
    return x**2 + 6*x + 9

x_values = [-3, -2, -1, 0, 1, 2, 3]
for x in x_values:
    y = find_y(x)
    print(f"For x = {x}, y = {y}")
    if y == 0:
        print(f"y becomes 0 when x = {x}")
        break

python_len = len('python')
dragon_len = len('dragon')
print(f"Length of 'python': {python_len}, Length of 'dragon': {dragon_len}")
print(f"Are the lengths of 'python' and 'dragon' the same? {python_len == dragon_len}")

is_on_in_both = 'on' in 'python' and 'on' in 'dragon'
print(f"Is 'on' found in both 'python' and 'dragon'? {is_on_in_both}")

sentence = "I hope this course is not full of jargon."
is_jargon_in_sentence = "jargon" in sentence
print(f"Is 'jargon' in the sentence? {is_jargon_in_sentence}")

is_equal = (7 // 3) == int(2.7)
print(f"Is floor division of 7 by 3 equal to int(2.7)? {is_equal}")

is_same_type = type('10') == type(10)
print(f"Is type of '10' equal to type of 10? {is_same_type}")

try:
    is_int_equal_10 = int(float('9.8')) == 10
except ValueError:
    is_int_equal_10 = False
print(f"Is int('9.8') equal to 10? {is_int_equal_10}")

hours = float(input("Enter the number of hours worked: "))
rate_per_hour = float(input("Enter the rate per hour: "))
pay = hours * rate_per_hour
print(f"The total pay is: {pay}")


years = float(input("Enter the number of years: "))
seconds_in_a_year = 365 * 24 * 60 * 60 
seconds_lived = years * seconds_in_a_year
print(f"If you live for {years} years, you can live approximately {seconds_lived} seconds.")


print("Number  Power  Power^2  Power^3  Power^4")
for i in range(1, 6):
    power_1 = i
    power_2 = i ** 2
    power_3 = i ** 3
    power_4 = i ** 4
    print(f"{i}       {power_1}       {power_2}       {power_3}       {power_4}")
