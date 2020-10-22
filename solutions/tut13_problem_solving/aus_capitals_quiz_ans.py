'''
A program to test the user's knowledge of the
capital cities of Australian states
over 3 questions
'''
from random import randint

aus_states=['New South Wales','Queensland','South Australia','Tasmania','Victoria','Western Australia']
aus_capitals=['Sydney','Brisbane','Adelaide','Hobart','Melbourne','Perth']

# the user's score
num_right=0
for i in range(0,3):
    # choose a random number between 0 and 5, inclusive
    r=randint(0,len(aus_states)-1)
    answer=input('Q%d. What is the capital of %s? ' %(i+1,aus_states[r]))
    if answer.lower()==aus_capitals[r].lower():
        print('Correct. The capital city of %s is %s.' %(aus_states[r],aus_capitals[r]))
        num_right+=1
    else:
        print('Not correct. The capital city of %s is %s.' %(aus_states[r],aus_capitals[r]))
    # remove this state from the list
    aus_states.pop(r)
    aus_capitals.pop(r)

    if i<2:
        print('Score: %d' %num_right)
    else:
        print()
        print('Final Score: %d.' %num_right)
print('Thank you for doing the Australian Capital City Quiz')


