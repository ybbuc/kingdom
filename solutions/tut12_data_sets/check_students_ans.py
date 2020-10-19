
def add_students():

    # a function to create a list of students
    # with GID, zNumber and computer mark

    st=[]
    for i in range(1,10):
        st.append(i)

    st[0]=['G04O976', 'z6313834', 57]
    st[1]=['G0432a1', 'z0261481', 97]
    st[2]=['GO49620', 'z611168', 94]
    st[3]=['G045824', 'z6247809', 99]
    st[4]=['g045469', 'z638155507', 54]
    st[5]=['G04130', 'Z6232395', 28]
    st[6]=['G047353', 'z6360ab9', 38]
    st[7]=['G0491191', 'x0183659', 98]
    st[8]=['G044761', 'z6125160', 62]

    return st

# check that the student GID is correct
# 7 characters, starts with G, followed by 0, then 5 numbers
def check_GID(student_GID):
    if len(student_GID)!=7:
        return 'Wrong length'
    if student_GID[0]!='G':
        return 'Does not start with G'
    if student_GID[1]!='0':
        return 'Second character is not 0'
    for i in range(2,7):
        try:
            temp=int(student_GID[i])+1
        except:
            return 'Not numeric'
    return True
            
def sort_by_comp_mark(student_list):
    # perform a selection sort on student list
    for i in range(0,len(student_list)-1):
        for j in range(i+1, len(student_list)):
            if student_list[i][2]<student_list[j][2]:
                temp=student_list[i]
                student_list[i]=student_list[j]
                student_list[j]=temp
    return student_list


student_list=add_students()

for student in student_list:
    print(student[0], end='')
    if check_GID(student[0])==True:
        print()
    else:
        print('. %s' %check_GID(student[0]))

student_list=sort_by_comp_mark(student_list)
for student in student_list:
    print(student)

