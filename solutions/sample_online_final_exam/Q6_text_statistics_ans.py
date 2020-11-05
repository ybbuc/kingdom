 
'''
Note that it is fine for students to use
text[i].isdigit()
text[i].isalpha() or isupper() or islower()
if they know them. 
'''

text=input('Enter some text: ')
print('Your text contains %d characters: ' %(len(text)))
letters = 0
spaces = 0
digits = 0
vowels = 0
for i in range(len(text)):
    #could use text[i].lower() and just compare to 'a' 'z'
    if(text[i] >= 'A' and text[i] <= 'Z' or
       text[i] >= 'a' and text[i] <= 'z'):
      letters += 1
    #could use try except to check for digits
    elif (text[i] >= '0' and text[i] <= '9'):
      digits += 1
    elif (text[i] == ' '):
      spaces += 1
    #could use multiple conditions instead of in and lower()
    if (text[i].lower() in 'aeiou'):
      vowels +=1
      

print('%d letters' %(letters))
print('%d vowels' %(vowels))
print('%d digits' %(digits))
print('%d spaces' %(spaces))  
