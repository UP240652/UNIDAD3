space = ' '
a = 'thirty'
b= 'days'
c='of'
d='Python'
print(a,space,b,space,c,space,d)

a = 'Coding'
b = 'for'
c = 'all'
print(a,space,b,space,c)

company = a+space+b+space+c
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
cut = company[0:6]
print(cut)
print(company.index('Coding'))
company2 = company.replace('Coding', 'Python')
print(company2)
company2 = company2.replace('all', 'Everyone')
print(company2)

sp = company.split(' ')
print(sp)

web = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(web.split(','))

com_index1 = company[0]
com_index2 = company[10]
print(com_index1,' - ', com_index2)

acronym = ''.join(word[0].upper() for word in company2.split())
print(acronym)
