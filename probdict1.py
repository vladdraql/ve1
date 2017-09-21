d1 = {'a': 100,
      'b': 200,
      'c': 300
     }

d2 = {'a': 50,
      'b': 35,
      'm': 36,
      'x': 555
     }



df = d1

print(df)

for k in d2:
    if k in d1:
        df[k] = d1[k] + d2[k]
    else:
        df[k] = d2[k]

print(df)