countries =['China', 'Vietnam','Mongolia','New Zealand']    
new_country = input('Add a country:')

if new_country not in countries:
    countries.append(new_country)
    print(countries)
else:
    print('%s is already in the list' % new_country)


