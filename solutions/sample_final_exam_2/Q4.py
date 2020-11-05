import random

random_num = random.randint(1, 100)
# print(random_num)

num_guesses = 0
user_guess = ''

while num_guesses < 5 and user_guess != random_num:

    user_input = input('Guess a number between 1 and 100: ')

    is_num = False

    try:
        user_guess = int(user_input)
        is_num = True
    except:
        print('Please enter a number.')

    if is_num is True:
        if user_guess < 1 or user_guess > 100:
            print('Please enter a number between 1 and 100.')
        elif user_guess > random_num:
            print('Your guess is too high.')
        elif random_num > user_guess:
            print('Your guess is too low.')
        else:
            print('Wow, you guessed the right number!')

    num_guesses += 1
