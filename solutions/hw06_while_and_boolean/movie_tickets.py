active = True
while active is True:
    print("Type 'quit' to exit")
    age_input = input('Enter age: ')
    if age_input == 'quit':
        active = False
    elif int(age_input) < 3:
        print('Free')
    elif int(age_input) > 12:
        print('$15')
    else:
        print('$10')
