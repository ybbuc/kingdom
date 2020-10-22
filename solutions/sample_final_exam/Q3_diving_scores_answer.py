'''
Question 3
Diving Scores
'''

name=['Kim','Algi','Ndomo','Zhang','Raj','Bemet','Lee']
score=[9.4,8.7,9.1,8.9,9.0,9.3,9.5]
medal=['Gold','Silver','Bronze']


# perform a bubble sort based on score
list_sorted=False
i=0
while list_sorted==False:
    i=0
    list_sorted=True
    while i<len(name)-1:
        if score[i]<score[i+1]:
            temp=name[i]
            name[i]=name[i+1]
            name[i+1]=temp
            temp=score[i]
            score[i]=score[i+1]
            score[i+1]=temp
            list_sorted=False
        i+=1



# print out the results
print('Diver       Dive   Medal')
for i in range(len(name)):
    printout=name[i]
    while len(printout)<12:
        printout+=' '
    printout+=str(score[i])
    if i<3:
        printout+='    '+medal[i]
    print(printout)

