# enumerate function is same as zip() function in some ways

names = ['hbash', 'qwdd', 'fdqewd', 'qs2']

enu_list = list(enumerate(names))
enu_dict = dict(enumerate(names))

print(enu_list)
print(enu_dict)

#you make it start from any number
enu_list = list(enumerate(names, start = 5))

print(enu_list)

for count, name in enumerate(names, start = 1):
    print(count)
    print(name)