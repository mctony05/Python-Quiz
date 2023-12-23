from qna import questions

class Quiz():
	
	def __init__(self, q):
		self.q = questions[q]
		
	def ask(self):
		print(self.q[:4])
		a = input('')
		if a.lower() == self.q[4]:
			print('Correct!')
		else:
			print(f"Wrong!\nCorrect answer was '{self.q[4]}'")
