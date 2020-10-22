currency_name = ['Euro', 'US Dollar', 'Singapore Dollar']
currency_rate = [0.62, 0.71, 0.98]

print('Welcome!\nQuick Currency Converter can convert \
the following currencies.')

for i in range(0, 3):
    print('%s. %s (%.2f)' % (str(i+1), currency_name[i], currency_rate[i]))


def is_number(poss_num):
    # Check if input is a number
    try:
        n = float(poss_num)
        is_num = True
    except:
        is_num = False
    return is_num


valid_input = False
while valid_input is False:
    user_input = input('Which currency do you wish to buy (choose a number)? ')
    if is_number(user_input) is False:
        print('You must enter a number.')
    else:
        if int(user_input) <= 0 or int(user_input) > 3:
            print('You must choose a number between 1 and 3.')
        else:
            valid_input = True


aud_amt = 'not a number'
while is_number(aud_amt) is False:
    aud_amt = input('How much Australian dollars do you wish to exchange \
to %s? ' % currency_name[int(user_input)-1])

currency_amt = float(aud_amt) * currency_rate[int(user_input)-1]

print('Your %.2f can be change to %.2f %ss.'
      % (float(aud_amt), float(currency_amt),
         currency_name[int(user_input)-1]))
