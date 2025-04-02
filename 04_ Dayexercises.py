#1
space = ' '
a = 'thirty'
b= 'days'
c='of'
d='Python'
print(a,space,b,space,c,space,d)

#2
a = 'Coding
b = 'for'
c = 'all'
print(a,space,b,space,c)

#3
company = a+space+b+space+c
#4
print(company)
#5
print(len(company))

#6
print(company.upper())
#7
print(company.lower())

#8
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9
cut = company[0:6]
print(cut)

#10
print(company.index('Coding'))
#11
company2 = company.replace('Coding', 'Python')
print(company2)
#12
company2 = company2.replace('all', 'Everyone')
print(company2)

#13
sp = company.split(' ')
print(sp)

#14
web = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(web.split(','))

#15
com_index1 = company[0]
#16
com_index2 = company[10]
#17
print(com_index1,' - ', com_index2)

#18
acronym = ''.join(word[0].upper() for word in company2.split())
print(acronym)

#19
acronym = ''.join(word[0].upper() for word in company.split ())
print(acronym)
word1 = "Coding For All"

#20
print(word1.index("C"))
#21
print(word1.index("F"))

#22
word2 = "Coding For All People"
print(word2.rindex("l"))

#23
sentence = "You cannot end a sentence with because because because is a conjunction"
start = sentence.index("because")
#24
end = sentence.rindex("because")
#25
print(start, " ", end)
print(sentence[start:end+7])

#28
#Does ''Coding For All' start with a substring Coding?
if (word1.index("Coding") == 0):
    print("YES")
else:
    print("NO")
#29
#Does 'Coding For All' end with a substring coding?
if (word1.rindex("Coding") == len(word1)):
    print("YES")
else:
    print("NO")

#30
word3 = "   Coding For All      "
print("|",word3.strip(" "),"|")

#31
var1 = "30DaysOfPython"
var2 = "thirty_days_of_python"
print(var1.isidentifier())
print(var2.isidentifier())

#32
#The following list contains the names of some of python 
# libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'].
#  Join the list with a hash with space string.

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
list = ""
for i in libraries:
    lista =lista + " " + i
print(list)

#34
print("I am enjoying this challenge.\nI just wonder what is next.")
#35
print("Name\tAge\tCountry\tCity")
print("Fernanda\t20\tMexico\tAguascalientes")
