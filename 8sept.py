# open('path_nume_fisier', 'mode')
# f = open('bla.txt', 'r+')
# content = f.read()
# f.write('\naaaaaaaaaaa')
# f.seek(0)
# f.close()

# print(content)

# recommended method:
with open('bla.txt', 'r+') as f:  # with also closes the file at the end
    content = f.readlines()

print(content)

# print('f inchis', f.closed)  # verifica daca f a fost inchis
#
# f2 = open('output.txt', 'r+')
# f2.write(content)
# f2.seek(0)
# print(f2.read())
# f2.close()
#
#
# print('f2 inchis', f2.closed)
