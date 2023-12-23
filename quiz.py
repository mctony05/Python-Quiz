import random
from quiztools import Quiz
from qna import questions

print('Welcome to the Quiz!')
num = int(input('How many questions? '))

while num > 0:
	randQuestion = random.randint(0, len(questions) - 1)
	quiz = Quiz(randQuestion)
	quiz.ask()
	num -= 1
		
print('Quiz over!')
