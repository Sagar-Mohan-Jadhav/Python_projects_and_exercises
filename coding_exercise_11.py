'''
A function count_from_zero_to_n() is implemented as such:

def count_from_zero_to_n(n):
    for x in range(0, n+1):
        print(x)
Function count_from_zero_to_n() takes in an integer n  as an argument, and prints out the integers from 0 to n .
 However, if someone calls this function with a negative integer, the function would print out nothing.
 This might make sense, but it can also be very confusing to the user. In order to let the user know that
 something is wrong with their input, we can raise an error that informs them that the input was invalid.
 In this way, they would know that the function should only be called with a non-negative integer.

Your task in this exercise is to check the input and raise a ValueError in the appropriate place so that the user can be well-informed that they provided an invalid argument.
'''


def count_from_zero_to_n(n):
    if n < 0:
        raise ValueError("The entered number can\'t be negative.")
    for x in range(0, n+1):
        print(x)

count_from_zero_to_n(-1)