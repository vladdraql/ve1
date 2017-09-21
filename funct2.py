import funct1

a = funct1.citire('a = ')
b = funct1.citire('b = ')

if funct1.compare(a, b):
   a = funct1.citire('inlocuim a cu: ')
else:
   a = funct1.primul_impar(a)

print(a, b)