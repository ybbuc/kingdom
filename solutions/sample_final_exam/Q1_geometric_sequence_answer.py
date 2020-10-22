'''
Code to produce 1 2 4 8 16 etc
12 elements long
'''

num=1
for i in range(9):
    print(num, end='')
    if i<8:
        print(', ', end='')
    else:
        print('.')
    num*=2

print()
# alternative answer
for i in range(8):
    print('%d, ' %2**i, end='')
print(str(2**8)+'.')
