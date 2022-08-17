'''
For this exercise we've provided you with a list of lottery players, and also with 6 random lottery numbers.

Find out the player with the most correct numbers, and print out their winnings and their name.

The random numbers are generated like this (I know we've not looked at the import keyword yet, bear with me on that one!):

import random
lottery_numbers = set(random.sample(range(22), 6))
And the list of players we've given you are:

players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]
Your task is to find who matched the most numbers, and print out a string with their name and the amount they won. For this exercise, assume there will only be 1 winner. Don't worry about two players matching the same amount of numbers.

For example:

Jen won 1000.

The winnings are calculated with this formula:

winnings = 100 ** len(numbers_matched)
'''
import random
lottery_numbers = set(random.sample(range(22), 6))

players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

numbers_matched = []
for player in players:
    num_match = []
    for number in lottery_numbers:
        if number in player['numbers']:
            num_match.append(number)
    if len(num_match) > len(numbers_matched):
        numbers_matched = num_match
        winner = player['name']

winnings = 100 ** len(numbers_matched)

print(f'{winner} won {winnings}')