usernames = ['jakob', 'george', 'emily', 'dorothy', 'admin']

if len(usernames) == 0:
    print('We need to find some users!')
else:
    for username in usernames:
        if username == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello %s, thank you for logging in again.' % username)
