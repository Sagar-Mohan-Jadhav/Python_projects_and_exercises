# you can combine lists by using zip() function
#ex,
names = ['hbash', 'qwdd', 'fdqewd', 'qs2']
ages = ['12', '123', '129', '13']

comb = dict(zip(names, ages))

print(comb)

#or
comb = list(zip(names, ages))

print(comb)

#zip can have more than 2 arguments and itll combine uptill the length of the shortest list input
comb = list(zip(names, ages, [1, 2, 3, 4, 5, 6, 7])) # notice we dont have 7 elements in other lists

print(comb)