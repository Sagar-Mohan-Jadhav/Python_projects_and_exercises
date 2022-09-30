# else statement can be used in for loop as well as in while loop

cars = ['ok', 'ok', 'ok', 'ok', 'ok']

for index in cars:
    if index == 'faulty':
        print('The car is faulty stopping the production.')
        break
    else:
        print("The car is okay, shipping to customer")
else:                                 #this else statement will only run when the loop does not encounter any errors or break statements.
    print('All the cars were okay.')
