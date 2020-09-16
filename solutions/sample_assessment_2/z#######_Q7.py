

knows_glory = input('Do you know the glory of King Jakob y/n? ')

if knows_glory.lower() == 'y':
    print('Please enter 4 words that describe the glory of King Jakob')
    words = []
    for i in range(4):
        words.append(input('Please enter a word: '))
    print('King Jakob is %s, %s, %s, and %s' % (words[0], words[1], words[2],
          words[3]))
else:
    print('I am very disappointed, but there is still time.')
