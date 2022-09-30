#tuples are useful when we dont want to modify the data in it but lists are useful when the data is getting modified

#tuples can be defined as
x = ('hello', 'world')
print(x)
#or
x = 'hello', 'world'
print(x)

#single element tuple
x = ('hello',)
print(x)

#adding elements in tuple
x = ('hello', 'world')
x = x + ('how',)
print(x)