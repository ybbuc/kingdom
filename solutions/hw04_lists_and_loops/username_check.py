current_users = ['cubby', 'parzival', 'art3mis', 'bo55man', 'easy_peasy']
new_users = ['Cubby', 'parzival', 'c00lstudent', 'u5ern@me', 'lemon_squeezy']

for user in new_users:
    if user.lower() in current_users:
        print('%s is already taken. Enter a new username.' % user.lower())
    else:
        print('%s is available.' % user.lower())
