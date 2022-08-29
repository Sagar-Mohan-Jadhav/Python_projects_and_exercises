'''
We challenge you to build a simple Artificial Intelligence (AI). Our AI is disguised as a function called interact() which works as follows:

It first asks the user for an integer input.

Then it tells the user whether that integer is even or odd.

Then it asks the user whether she wants to play this game again.

If the user inputs y for yes, then the function repeats.

If the user inputs anything other than y, then it prints out Goodbye. and quits.
since users can input things other than an integer, such as a string. Our AI will break with a ValueError if that happens. The ValueError would be raised in the first line: user_input = int(input('Please input an integer:')), when the user inputs something other than an integer.

Now that we've located the failure point, we ask you to build our AI which can recover from the invalid user input. If the user enters an invalid input at first, it will print out a message Please input integers only., and then it can still proceed to ask the user if she wants to play again.

Here are some sample in inputs and expectations:

Valid inputs:

  AI: Please input an integer:
User: 17
  AI: 17 is odd.
  AI: Do you want to play again? (y/N):
User: y
  AI: Please input an integer:
User: 11
  AI: 11 is odd.
  AI: Do you want to play again? (y/N):
User: n
  AI: Goodbye.
Invalid inputs:

  AI: Please input an integer:
User: a
  AI: Please input integers only.
  AI: Do you want to play again? (y/N):
User: n
  AI: Goodbye.
Hint: insert your try, except, else and finally key words in the appropriate places and change/add some code if you find necessary.
'''


def interact():
    while True:  # keep looping until user reach break statement
        try:
            user_input = int(input('Please input an integer: '))  # turn the user input into an integer
        except ValueError:
            print("Please input integers only.")
        else:
            is_even = user_input % 2 == 0
            print('{} is {}.'.format(user_input,
                                     'even' if is_even else 'odd'))  # print out the message '{user_input} is {even/odd}.'
        finally:
            user_input = input('Do you want to play again? (y/N): ')
            if user_input != 'y':  # quit if the user didn't input `y`
                print('Goodbye.')
                break  # break the while loop to quit

