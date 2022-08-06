'''
We're getting to some more advanced coding exercises!

We have provided you with two variables:

nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set() # This is an empty set, like {}
In this exercise, ask the user for the name of a friend. Add this name to the user_friends set provided.

Finally, print out a set that contains only the name of the friend if the friend is in the nearby_people set.

You'll want to calculate the intersection between two sets, and print the result out.
'''

nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend
name_friend = input('Enter the name of your friend: ')

# Add the name to the empty set
user_friends.add(name_friend)

# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
near_friends = user_friends.intersection(nearby_people)
if near_friends == {}:
    print(None)
else:
    print(user_friends.intersection(nearby_people))

