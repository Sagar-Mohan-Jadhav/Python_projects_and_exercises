#for dictionaries

friends = {"martin": 40, "happy": 30, "bob": 35}

for friend in friends:  #this will only print keys
    print(friend)

for age in friends.values(): #this will only print values
    print(age)

for friend, age in friends.items(): #this will create tuple out of dictionarys key-value pairs
    print(f"{friend} is {age} years old")

print(friends.items())