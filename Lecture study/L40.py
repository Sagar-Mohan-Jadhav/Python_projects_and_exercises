friends = ('bob','marley','sameer')
last_seen = [2, 3, 5]

long_time_no_see = {friends[i].title(): last_seen[i] for i in range(len(friends)) if last_seen[i] > 2.5}

print(long_time_no_see)