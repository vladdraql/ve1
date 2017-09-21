d = {'key1': 'val1',
     'key2': 'val2',
     'a': 2,
     'key3': [1, 2],
     77: 77777
     }

# print(d)
# print(d.items()) # returneaza tuple (key, value)

for k, v in d.items():
    print('{} {}'.format(k, v))