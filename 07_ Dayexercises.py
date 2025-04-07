# sets Excercises: Level 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

#1
print(f"The lenght of it companies is {len(it_companies)}")

#2
it_companies.add("Twitter")
print(it_companies)

#3
it_companies.update(["Youtube","Linux","Opera"])
print(it_companies)

#4
it_companies.discard("Youtube")
print(it_companies)

#5
print("The discard() method removes the specified element from the set. Unlike the remove() method, discard() " \
"does not raise an error if the specified element is not present.")

#Exercises: Level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#1
C = A.union(B)
print(C)

#2
print(A.intersection(B))

#3
print(A.issubset(B))

#4
print(A.isdisjoint(B))

#5
AB = A.union(B)
BA = B.union(A)
print(AB,BA)

#6
print(A.symmetric_difference(B))

#7
del A,B

#Exercises: Level 3
age_list = [22, 19, 24, 25, 26, 24, 25, 24]

#1
age_set = set(age_list)

if len(age_set) == len(age_list):
    print('The set and the list are equal')

elif len(age_set) > len(age_list):
    print('Set is bigger')

else:
    print('List is bigger')

#2
'''
String: Text-based data.
List: Ordered, mutable collection of items.
Tuple: Ordered, immutable collection of items.
Set: Unordered collection of unique items.

'''
#3
sentence = 'I am a teacher and I love to inspire and teach people'
words = set(sentence.split())
print(f'The number of unique words is {len(words)}')

