with open('bla.txt', 'r+') as f:
    content = f.readlines()

cursor_in = int(input("Pozitia la care adaugam: "))
while cursor_in > len(content)+1:
    print('Pozitia maxima la care putem adauga este {}. Mai incearca!'.format(len(content)+1))
    cursor_in = int(input("Pozitia la care adaugam: "))

linie_de_adaugat = input("Linia de adaugat: ")
cursor = cursor_in-1

out_list=[]
for i in content[:cursor]:
    out_list.append(i)

if cursor < len(content):
    out_list.append(linie_de_adaugat + "\n")
else:
    out_list.append("\n" + linie_de_adaugat)

for i in content[cursor:]:
    out_list.append(i)

with open('output.txt', 'w+') as f2:
    f2.writelines(out_list)

with open('output.txt', 'r+') as f3:  # with also closes the file at the end
    print(f3.read())