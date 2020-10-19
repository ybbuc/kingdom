i=0
# [] is an empty list
six_largest_countries = ['Russia', 'Canada', 'United States', 'China', 'Brazil', 'Australia']
three_largest_countries = []

while len(three_largest_countries) < 3:  
    new_list = six_largest_countries.pop(0)
    print('Transferring %s' % new_list)
    print(six_largest_countries)    
    three_largest_countries.append(new_list)
    
print('The three largest countries are:')
for country in three_largest_countries:
        i=i +1
        print(i, country)
