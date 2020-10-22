'''
A program to calculate each student's weight mark
homework = 10%, practial=20%, assignment = 20%, final test = 50%
'''

# student name, homework, practical, assignment, final test
Alice = ['Alice', 75, 81, 74, 75]
Xin = ['Xin', 88, 77, 74, 94]
Isabelle = ['Isabelle', 80, 84, 93, 81]
Alan = ['Alan', 45, 100, 45, 94]
Jessica = ['Jessica', 70, 81, 93, 94]
Christina = ['Christina', 93, 80, 93, 90]
Pan = ['Pan', 62, 64, 89, 47]
Ding = ['Ding', 64, 68, 2, 58]
Erica = ['Erica', 85, 97, 60, 80]
Xu = ['Xu', 56, 58, 64, 94]
Jason = ['Jason', 30, 8, 35, 26]
Yang = ['Yang', 54, 34, 64, 86]
Vincent = ['Vincent', 54, 72, 84, 16]
Emily = ['Emily', 91, 100, 79, 76]
Wang = ['Wang', 73, 57, 73, 99]

students=[Alice, Xin, Isabelle, Alan, Jessica, Christina,
         Pan, Ding, Erica, Xu, Jason, Yang, Vincent, Emily, Wang]


def calc_weighted_mark(stu):
    stu_mark=0
    weight=[0.1,0.2,0.2,0.5]
    for i in range(0,4):
        stu_mark+=weight[i]*stu[i+1]
    return stu_mark

def calc_grade(stu_mark):
    base_mark=[0,50,65,75,85]
    grade=['Fail','D','C','B','A']
    for i in range(0,5):
        if stu_mark>=base_mark[i]:
            stu_grade=grade[i]
        else:
            break
    return stu_grade

print('Student       Weighted    Final')
print('Name          Mark        Grade')
for stu in students:
    line=(stu[0])
    while len(line)<14:
        line+=' '
    weighted_mark=calc_weighted_mark(stu)
    line+=str(round(weighted_mark,1))
    student_grade=calc_grade(weighted_mark)
    while len(line)<26:
        line+=' '
    line+=student_grade
    print(line)
    
