# write a python program that will ask user three names of friends and then the program will check whether the people
# enterd by user are in the city or not. The people in the city are already present in the people.txt file. The people
# present in the city and who are also user's friends will be stored in the nearby_friends.txt file.

def nearby_or_not(people_content):
    friends = input("Enter the names of friends separated by white space: ")
    friends = (friends.title()).split()
    people_content = (people_content.title()).split()
    nearby = ""
    nearby_friends = open("nearby_friends.txt", 'w')
    for i in range(len(people_content)):
        if people_content[i - 1] in friends:
            nearby = f"{people_content[i - 1]}\n{nearby}"
    nearby_friends.write(nearby)
    nearby_friends.close()


people = open("people.txt", 'r')
people_content = people.read()
people.close()
nearby_or_not(people_content)
