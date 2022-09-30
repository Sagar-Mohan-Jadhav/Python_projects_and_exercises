#creating a string with variables inside
car = 3
print(f'i have {car} cars')

#alternate way
print('I have '+ str(car) + ' cars')

#one more way
car = 3
dialogue = 'i have {} cars'
print(dialogue.format(car))
#or
car = 3
dialogue = 'i have {number} cars'
print(dialogue.format(number = car))

#example
car = 3
name = 'mike'
dialogue = '{} has {} cars'
print(dialogue.format(name, car))