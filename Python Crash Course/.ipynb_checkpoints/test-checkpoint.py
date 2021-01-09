numbers = 0
sum_numbers = 0

while numbers != 2:
    prompt = 'Please provide a number:'
    number = input(prompt)

    try:
        number = int(number)
    except ValueError:
        print('Please provide numbers instead of strings.')
    else:
        sum_numbers += number
        numbers += 1
        
print(f'Sum of your numbers: {sum_numbers}')