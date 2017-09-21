with open('bla.txt', 'r+') as f:
    content = f.readlines() #creeaza lista cu liniiile ca elemente separate cu tot cu \n la capatul elementului

out_list=[]
for i in content:
    if len(i)>=3:
           out_list.append(i[:2]+i[2:].capitalize())
    else:
        out_list.append(i)


with open('output.txt', 'w+') as f2:
    f2.writelines(out_list)

with open('output.txt', 'r+') as f3:  # with also closes the file at the end
    print(f3.read())