#sum() and len() function can be used for lists or tuples or sets

grade = [90, 36, 89, 40, 100]
total = sum(grade)
no_of_subjects = len(grade)
average = total/no_of_subjects

print(f'the subject average is {average}')