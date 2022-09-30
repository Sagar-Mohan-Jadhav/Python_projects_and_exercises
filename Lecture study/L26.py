# if statement example

# friends = ['jane', 'sameer', 'andy']
# family = ['mandy', 'sandy']
#
# user_name = input('Please enter your name: ')
#
# if user_name in friends: # in word checks if the user_name is in the friends
#     print('Hello, friend')
# elif user_name in family:
#     print('Hello, family member')
# else:
#     print('Hello, stranger')

# the friends and family names does not have to be in a list it can be a tuple or set too
friends = ('jane', 'sameer', 'andy')
family = {'mandy', 'sandy'}

user_name = input('Please enter your name: ')

if user_name in friends: # in word checks if the user_name is in the friends
    print('Hello, friend')
elif user_name in family:
    print('Hello, family member')
else:
    print('Hello, stranger')