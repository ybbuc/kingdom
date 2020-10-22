'''
A file that rolls three dice many times
and counts the totals
'''

from random import randint

# make a list
totals=[]
for i in range(0,19):
    totals.append(0)

max_rolls=100

for i in range(0,max_rolls):
    r1=randint(1,6)
    r2=randint(1,6)
    r3=randint(1,6)
    total=r1+r2+r3
    totals[total]+=1

print('Totals for %d rolls of 3 dice' %max_rolls)

for i in range(3,19):
    print('%d: %d' %(i,totals[i]))
    


