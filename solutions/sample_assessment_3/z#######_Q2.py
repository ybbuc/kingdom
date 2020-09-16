def easy_peasy():
    response = input('Easy peasy... ')
    if response.lower() != 'lemon squeezy':
        easy_peasy()


def get_king_name():
    king_name = input('Enter the name of the King: ')
    if king_name.lower() != 'jakob':
        print('%s is a false king!' % king_name)
        get_king_name()


easy_peasy()
user_name = input('Enter your name: ')
get_king_name()
print('%s, you can be of good service to King Jakob.' % user_name)
