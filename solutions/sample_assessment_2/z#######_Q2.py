
def ask_about_king():
    king = input('Who is the current king? ')
    if king.lower() == 'jakob':
        print('That is right!')
    else:
        print('%s is not the king.' % king)
        ask_about_king()


ask_about_king()
