list_in = input("input: ")
output = list_in.split(',')
print(type(output))

output.sort()

l = ','.join(output)
print(l.upper())

output.sort(reverse=True)

l = ','.join(output)
print(l.lower())

