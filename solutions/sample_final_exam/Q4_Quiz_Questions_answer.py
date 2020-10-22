'''
Quiz questions
'''
question=['4 - 16','5 + 11','3 x 21','8 / 2','3 ^ 2']
answer=[-12,16,63,4,9]

question_number=0
correct_answers=0

while question_number<5 and correct_answers<3:
    the_question=str(question_number+1)+'. What is '+question[question_number]\
              +'? '
    user_answer=input(the_question)
    try:
        if int(user_answer)==answer[question_number]:
            correct_answers+=1
            print('Correct')
        else:
            print('Not correct')
    except:
        print('The answer is a number.')
    question_number+=1

print('Thank you for doing the quiz.')
print('You answered %d questions and got %d correct answers.' \
      %(question_number, correct_answers))
                                                               
