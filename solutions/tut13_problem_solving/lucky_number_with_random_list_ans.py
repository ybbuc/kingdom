'''
A program that asks the user to choose a number from the list.
And gives the user three chances to guess the lucky number
'''

from random import randint

# makes a list of 8 random numbers
def make_number_list():
    num_list=[]
    i=0
    while i<8:
        r=randint(1,99)
        if i==0:
            num_list.append(r)
            i+=1
        elif r not in num_list:
            num_list.append(r)
            i+=1
    return num_list
            
# a function to sort a list
def sort_list(the_list):
    for i in range(0,len(the_list)-1):
        for j in range(i+1,len(the_list)):
            if the_list[i]>the_list[j]:
                temp=the_list[i]
                the_list[i]=the_list[j]
                the_list[j]=temp
    return the_list
    

# a function to test if input is a number
def test_number(num):
    try:
        i=int(num)
        is_number=True
    except:
        is_number=False
    return is_number
        

print('Lucky Number Guessing Game')
# number of guesses left
guesses_left=3
guess='guesses'
numbers=make_number_list()


guess_right=False
# assign the lucky number before sorting the list
lucky_number=numbers[0]
numbers=sort_list(numbers)

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
        print('%d is not on the list' %int(user_guess))
    guesses_left-=1

if guess_right==False:
    print('Sorry but you did not guess the lucky number.')
    print('The lucky number was %d.' %lucky_number)
    print('Game over.')

