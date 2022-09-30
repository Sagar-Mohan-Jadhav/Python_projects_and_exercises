# lists can have other lists as elements
x = [['car', 7], ['far', 8], ['mar', 0]]
#to print mar
print(x[2][0])

#adding and removing elements from string
x = [['car', 7], ['far', 8], ['mar', 0]]
x.append(['bar', 5])
print(x)

x.remove(['car', 7])
print(x)