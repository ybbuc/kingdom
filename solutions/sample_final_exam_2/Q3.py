#    ['state name', electoral votes, Biden votes, Trump votes]
MN = ['Minnesota', 10, 1671129, 1436422]
ME = ['Maine', 4, 327878, 254049]
FL = ['Florida', 29, 5269926, 5646949]
OH = ['Ohio', 18, 2576590, 3038247]
TX = ['Texas', 38, 5145367, 5810522]
NC = ['North Carolina', 15, 2655383, 2732120]
GA = ['Georgia', 16, 2279736, 2381870]
WI = ['Wisconsin', 10, 1420855, 1529223]
AZ = ['Arizona', 11, 1367211, 1236546]
NV = ['Nevada', 6, 553484, 528442]
MI = ['Michigan', 16, 1956696, 2198132]
PA = ['Pennsylvania', 20, 2286865, 2964853]

key_states = [MN, ME, FL, OH, TX, NC, GA, WI, AZ, NV, MI, PA]

# Sorting the key states by electoral votes, descending
for i in range(len(key_states)-1):
    for j in range(i+1, len(key_states)):
        if key_states[i][1] <= key_states[j][1]:
            temp = key_states[i]
            key_states[i] = key_states[j]
            key_states[j] = temp


print('STATE             ELECTORAL VOTES   BIDEN VOTES   TRUMP VOTES   PROJECTED')

trump_electoral = 0
biden_electoral = 0

for s in key_states:
    output = ' '
    output += s[0]  # State name
    while len(output) < 19:
        output += ' '
    output += str(s[1])  # Electoral votes
    while len(output) < 37:
        output += ' '
    output += str(s[2])  # Biden votes
    while len(output) < 51:
        output += ' '
    output += str(s[3])  # Trump votes
    while len(output) < 65:
        output += ' '
    if s[2] > s[3]:  # Biden is the projected winner
        output += 'Biden'
        biden_electoral += s[1]
    elif s[3] > s[2]:  # Trump is the projected winner
        output += 'Trump'
        trump_electoral += s[1]
    else:  # Tie in votes
        output += 'tie'
    print(output)

print()  # Just putting in a space

if biden_electoral > trump_electoral:
    print('It is projected that Biden has %d more electoral votes than Trump.'
          % (biden_electoral-trump_electoral))
elif trump_electoral > biden_electoral:
    print('It is projected that Trump has %d more electoral votes than Biden.'
          % (trump_electoral-biden_electoral))
else:
    print('Trump and Biden both have a projected %d electoral votes'
          % biden_electoral)
