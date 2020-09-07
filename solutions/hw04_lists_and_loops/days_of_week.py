days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
        'Saturday', 'Sunday']
new_days = []


def week():
    if len(new_days) < len(days):
        day = input('Enter a day of the week: ')
        if day.title() in days:  # Consider when day is in master list
            if day.title() in new_days:
                print('Sorry, ', day.title(), 'is already in the list.')
                week()
                # Python allows functions to call themselves to loop;
                # this is known as recursion
            else:
                print(day.title(), 'has been added to the days of the week.')
                new_days.append(day.title())
                print(new_days)
                week()
        else:  # Consider when the day is not in master list
            print('Sorry,', day, 'is not a day of the week.')
            week()
    else:
        print('Well done! You have populated the list.')


week()
