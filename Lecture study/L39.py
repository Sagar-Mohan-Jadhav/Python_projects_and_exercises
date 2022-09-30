friends = ['bob', 'marley', 'Anthony', 'SAMEER']
guests = ['MARLEY', 'saMeer', 'tony', 'happy']

friends = [_.upper() for _ in friends]
guest_and_friend = [
    f"my friend {guest.title()} is also my guest" for guest in guests if guest.upper() in friends
]
print(guest_and_friend)

# this same is applicable for tuple/set as well