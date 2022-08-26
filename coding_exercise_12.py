'''
In the last exercise, we added a code block that checked for user input and raised a Python built-in error (ValueError)
 if we found the input to be invalid.

In this exercise, we will be using the same function count_from_zero_to_n() . However, this time, we want to raise a
custom error instead of the Python built-in error.

Defining a custom error can give us many advantages, such as containing more info in its name, uniquely identifying this
 error from other errors and allowing more flexibility to construct an error instance.

In this exercise, define an UncountableError class which inherits from ValueError. Our UncountableError should only take
 in an argument wrong_value when constructing. And if raised, our UncountableError should give the user an error message
  like this one: Invalid value for n, WRONG_VALUE. n must be greater than 0. , where WRONG_VALUE should be substituted
  by the invalid argument given.

For example, this is the code that you shall expect your UncountableError being used for.

def count_from_zero_to_n(n):
    if n < 1:
        raise UncountableError(n)
    for x in range(0, n + 1):
        print(x)
Notice that UncountableError only takes an argument wrong_value when being constructed. If the user calls the
count_from_zero_to_n() function with n being -10, your UncountableError should be raised and show this message:
Invalid value for n, -10. n must be greater than 0.
'''


class UncountableError(ValueError):
    def __init__(self, n):
        super().__init__(f'Invalid value for n, {n}. n must be greater than 0.')


def count_from_zero_to_n(n):
    if n < 1:
        raise UncountableError(n)
    for x in range(0, n + 1):
        print(x)
