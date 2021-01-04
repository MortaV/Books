prompt = 'What is your age? '

age = input(prompt)
age = int(age)

if age<3:
    print('Your ticket is free.')
elif age<=12:
    print('Your ticket costs 10$.')
elif age>12:
    print('Your ticket costs 15$.')
else:
    print('Incorect age provided.')