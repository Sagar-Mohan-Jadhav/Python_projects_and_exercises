'''
In this problem, we've provided you with a set of lottery numbers:

lottery_numbers = {13, 21, 22, 5, 8}
You must define a list of two players, each with a name and another set of numbers.

Players in your list should be dictionaries following this format:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}
You can come up with each player name and numbers!

Printing out their luck

Then for each player, print out a nice string that contains their name and how many numbers they got right (as we've done before, you can intersect their numbers with the lottery_numbers  variable provided). You'll then need to calculate the length of the resulting set to get how many numbers they got right.

This string doesn't have to have a particular format, it just must include both the name and how many numbers they got right.
'''
lottery_numbers = {13, 21, 22, 5, 8}


"""
Define a list with two players (you can come up with their names and numbers).
"""

players = [{'name':'Sagar Jadhav', 'numbers':{21, 5, 18, 6, 9}}, {'name':'Joe Biden', 'numbers':{21, 5, 13, 0, 2}}]


"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""
print(f'Player {players[0]["name"]} got {len(lottery_numbers.intersection(players[0]["numbers"]))} numbers right.')
print(f'Player {players[1]["name"]} got {len(lottery_numbers.intersection(players[1]["numbers"]))} numbers right.')