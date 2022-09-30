def average(student):
    grades = student["grades"]
    return sum(grades)/len(grades)


my_student = {
    "name": "Rolf Smith",
    "grades": [70, 88, 90, 99]
}

print(average(my_student))
