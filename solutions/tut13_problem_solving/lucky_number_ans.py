'''
A program that asks the user to choose a number from the list.
And gives the user three chances to guess the lcuky number
'''

# a function to test if input is a number
def test_number(num):
    try:
        i=int(num)
        is_number=True
    except:
        is_number=False
    return is_number
        

print('Lucky Number Guessing Game')
guesses_left=3
guess='guesses'
numbers=[2,6,19,23,30,41,54,75]
guess_right=False
lucky_number=41

while guesses_left>0 and guess_right==False:
    if guesses_left==1:
        guess='guess'
    print('\nYou have %d %s left.' %(guesses_left, guess))
    for i in range(0,len(numbers)):
        if i>0:
            print(', ', end='')
        print(numbers[i], end='')
    print()
    user_guess=input('Choose a number from the list: ')
    if test_number(user_guess)==False:
        print('%s is not a number.' %user_guess)
    elif int(user_guess)==lucky_number:
        guess_right=True
        print('Congratulations! The lucky number was %d.' % lucky_number)
    elif int(user_guess) in numbers:
        print('%d is not the lucky number.' %int(user_guess))
        numbers.remove(int(user_guess))
    else:
        print('%d is not in the list' %int(user_guess))
    guesses_left-=1

if guess_right==False:
    print('Sorry but you did not guess the lucky number.')
    print('The lucky number was %d.' %lucky_number)
    print('Game over.')


