'''
A file to calculate student grades,
highest mark, average mark
and display this data effectively
'''
# student details
# The first element is the name of the student,
# the second is their English mark, the third is their maths mark
# and the fourth is their computing mark
John=['John',14,45,62]
Cynthia=['Cynthia',58,78,91]
Osman=['Osman',74,81,60]
Karen=['Karen',94,94,88]
Jason=['Jason',48,56,56]
students=[John,Cynthia,Osman,Karen,Jason]

# a function that returns the average mark
# takes student as a parameter
def av_mark(student):
    return (student[1]+student[2]+student[3])/3

# a function that lists student marks over four lines
# ready to print
def print_marks(student):
    statement='Student Name: ' + student[0] + '\n'
    statement+='English Mark: ' + str(student[1]) + '\n'
    statement+='Maths Mark: ' + str(student[2]) + '\n'
    statement+='Computing Mark: ' + str(student[3])
    return statement

# a function that calculates a student's grade
def calc_grade(student):
    average_mark=av_mark(student)
    if average_mark<50:
        grade='Fail'
    elif student[1]<60:
        grade='Technical Fail'
    elif average_mark<70:
        grade='C'
    elif average_mark<85:
        grade='B'
    else:
        grade='A'
    return grade

# a funcion that finds a student's best mark
# returns the mark
def best_mark(student):
    top_mark=0
    for i in range(1,4):
        if student[i]>top_mark:
            top_mark=student[i]
    return top_mark

# a function that works out a student's best subject(s)
def best_subject(student):
    top_mark=best_mark(student)
    # put and empty string in zero position so name correponds to mark
    subjects=['','English','Maths','Computing']
    best_subjects=''
    for i in range(1,4):
        if student[i]==top_mark:
            if best_subjects>'':
                best_subjects+=', '
            best_subjects+=subjects[i]
    return best_subjects


for s in students:
    print(print_marks(s))
    print('Average mark: %.1f' %av_mark(s))
    print('Grade: %s' %calc_grade(s))
    print('Best mark: %d' %best_mark(s))
    print('Best subject: %s' %best_subject(s))
    print()