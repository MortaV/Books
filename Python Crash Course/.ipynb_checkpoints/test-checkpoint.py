import json

filename = 'user_number.json'
try:
    with open(filename, 'r') as file_object:
        user_number = json.load(file_object)
except FileNotFoundError:
    prompt = 'Let us know your favourite number: '
    number = input(prompt)
    number = int(number)
    with open(filename, 'w') as file_object:
        json.dump(number, file_object)
else:
    print(f'I know your favourite number is {user_number}.')