l = []
print(type(l))
print(len(l))

l.append('abc')
l.append([1, 2])
l.append(6)
l.append(5)
l.extend([1,2,3,4,5])

print(l)

# for item in l:
#     tipul=type(item)
#     print (f'{tipul.__name__}')

def create_list(list_input):
    list_out = []
    for item in list_input:
        if type(item) == int:
            list_out.append(item)

    return list_out

# SAU:
int_list = [i for i in l if type(i)==int]
print (int_list)

# print (create_list(l))

def invert_list(list_input):
    list_out = []
    i=len(list_input)-1
    for x in range(len(list_input)):
        list_out.append(list_input[i])
        i = i-1
    return list_out

# print (invert_list(l))


