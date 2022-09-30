# you can use for loop in lists/tuples/set as follows without using too many lines of code

friends = ['John', 'Mann', 'Anthony', 'Sameer']

list_sentences = [f'{friend} is my friend' for friend in friends]
print(list_sentences)

# you can use lower() or title() functions to avoid mistakes due to capitalization of letters

name = input("Enter the name of your friend: ") # this can be capital or lower case
friends = [_.lower() for _ in friends]
if name.lower() in friends:
    name = name.title()              # to get first letter capital in output
    print(f"{name} is your friend")

friends = [_.upper() for _ in friends] # similarily there is upper() function for all capital letters.
print(friends)