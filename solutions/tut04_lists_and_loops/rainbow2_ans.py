days=['Monday', 'Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
my_days = []
def week():
    if len(my_days) < len(days):
	    a_day = input('Enter a day of the week:')
	    if a_day in days:
		    if a_day in my_days:
			    print('Sorry already in our list.')
			    week()
		    else:
			    print(a_day, 'has been added to our days of the week.')
			    my_days.append(a_day)
			    print(my_days)
			    week()
	    else:
		    print('Sorry', a_day ,'is not a day of the week.')
		    week()
    else:
        print('Well done! You have populated the list.')


week()
