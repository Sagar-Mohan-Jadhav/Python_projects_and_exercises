group1 = {'tim', 'anna', 'tony', 'kim'}
group2 = {'jim', 'tony', 'joe'}
#group 1 but not is group 2
one_but_not_two = group1.difference(group2)
print(one_but_not_two)

#group 1 and group 2
one_and_two = group1.intersection(group2)
print(one_and_two)

#group 1 or group 2
one_or_two = group1.union(group2)
print(one_or_two)

#not in group 1 and group 2
not_in_both = group1.symmetric_difference(group2)
print(not_in_both)