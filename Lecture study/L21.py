#unlike tuples dictionaries have an order and elements and they appear in the same order as they were added

friends = {'tim':39, 'jim':78, 'bim':20}
print(friends['tim'])

#to add element or to assign new value to keys
friends['tim'] = 40
friends['bhim'] = 18
print(friends)

#to make a dictionary of list of tuples
friends = [('hello', 3), ('world', 4)]
friends = dict(friends)
print(friends)