'''
In this exercise, we challenge you to build something useful: a quiz system, using what we've just learnt.
Our quiz system will load data from a text file named questions.txt, whose format is like this:

1+1=2
2+2=4
7-4=3
As you can tell, each line represents a Q&A, where questions and answer are separated by a =.
Your application must:
Load the Q&As from questions.txt.
For each Q&A, prompt the user with the question and expect an input from the user as the answer before moving to the next question.
For example, for the sample file provided above, it should print out 1+1=, and then wait for the user input their answer.
You need to keep track of the answers, and after the user answers all the questions, you need to store their grade into a file named result.txt.
The format of the grade should be Your final score is {n}/{m}., where {n} and {m} should be replaced by the number of correct answers and total number of questions respectively.
Please try to run your script in your IDE or via terminal to see if it works before submitting the code—we have provided a sample questions.txt  for you to look at.
'''

file = open("questions.txt", 'r')
questions = file.read()
file.close()
questions = questions.split()
count = 0
for index1 in range(len(questions)):
    for index2 in range(len(questions[index1])):
        if questions[index1][index2] == '=':
            print(questions[index1][0: index2 + 1])
            answer = input()
            if answer == questions[index1][index2 + 1]:
                count = count + 1

answer_file = open("result.txt", 'w')
answer_file.write(f'Your final score is {count}/{len(questions)}.')
answer_file.close()
