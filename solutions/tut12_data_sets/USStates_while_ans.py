'''
Ask the user to name a state of the US
then search a list to see if they are correct.
Ignores case
'''

USStates=['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
         'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
         'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
         'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
         'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
         'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma',
         'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
         'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
         'West Virginia', 'Wisconsin', 'Wyoming']


search_state=input('Type in the name of a US state to search for: ')

i=0
state_found=False

while state_found==False and i<len(USStates):
    if search_state.lower()==USStates[i].lower():
        state_found=True
    else:
        i+=1

if state_found==True:
    print('%s is a US state.' %USStates[i])
else:
    print('%s is not a US state.' %search_state)

    

