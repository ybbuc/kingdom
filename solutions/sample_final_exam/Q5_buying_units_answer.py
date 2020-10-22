'''
0-1000 cost $500
1001 - 2000 cost $450
2001+ cost $420
'''


def calc_cost(number):
    if num_units>2000:
        cost=1000*500+1000*450+(num_units-2000)*420
    elif num_units>1000:
        cost=1000*500 + (num_units-1000)*450
    else:
        cost=num_units*500
    return cost
    

num_units=input('How many units do you wish to purchase? ')

try:
    num_units=int(num_units)
except:
    quit()

if num_units>0:
    cost_of_units=calc_cost(num_units)
    print('Buying %d units will cost $%d.' %(num_units,cost_of_units))
