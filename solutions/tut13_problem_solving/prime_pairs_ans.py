'''
A program to find all the prime pairs
under a given number
'''

# check if a number is prime by dividing by known primes
def check_prime(test_number, primes):
    is_prime=True
    for p in primes:
        if test_number % p == 0:
            is_prime=False
            break
        elif p**2>test_number:
            break
        
    return is_prime


primes=[]
max_number=1000

# add the first two primes as starters
primes.append(2)
primes.append(3)
num_primes=len(primes)

number=4
num_pairs=0
print('Prime Pairs')
while number <max_number:
    if check_prime(number,primes)==True:
        # check if the new prime is two more than the previous prime
        if number-primes[len(primes)-1]==2:
            print('%d, %d' %(primes[len(primes)-1],number))
            num_pairs+=1
        primes.append(number)
    number+=1

print('The number of prime pairs under are %d is %d.' %(max_number, num_pairs))
            
    

