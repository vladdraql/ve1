out = ''
for x in range(2000, 3201):
    if x % 7 == 0 and x % 5 != 0:
        out += ',' + str(x)

print(out[1:])
