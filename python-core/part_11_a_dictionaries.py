# dictionaries store data as key-value pair

d = {'tom': 77777777, 'rob': 76767676, 'joe': 75747345}
print(d)
print(d['tom'])

# add a new value

d['sam'] = 79787776
d['fred'] = 79787776
print(d)
# delete a value
del d['sam']
print(d)

for key in d:
    print('Key:', key, 'Value:', d[key])

for k, v in d.items():
    print("Key:", k, "Value:", v)

print('tom' in d)
print('sam' in d)

d.clear()  # clears all the values in a dictionary
print(d)
