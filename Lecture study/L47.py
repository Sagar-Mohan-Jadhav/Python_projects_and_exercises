# input arguments overruling: the default value of the function can be over-ruled
# by calling the function and giving it an input arugument value

def add(x, y=3):
    return x + y


print(add(2))  # the output is 5 as x assumes value of 2

print(add(2, 6))  # here default value of y = 3 is over-ruled by input argument of y = 6 and answer is 8

print(add(x=3, y=3))  # is also valid answer is 6

print(add(2, y=7))  # is valid answer is 9

# print(add(x=2, 5)) # is not valid, if a previous variable is named then all the later variables must also be named

# def add(x=2, y): # this is invalid because default value argument must be at the last position
#     return x + y

#ex,
print(1, 2, 3, 4, 5, 6, sep=' - ', end=' $')


