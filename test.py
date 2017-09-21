result = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        result.append(i)

# print(result)

s=""
for x in result:
   s += str(x)+","



# print(s[:-1])

co=""
do=""
cocos=['ana', 'are', 'mere']
dodos=[1000, 5000, 2000]
co = ','.join(cocos)
do = ','.join(str(e) for e in dodos)
print(co)
print(do)