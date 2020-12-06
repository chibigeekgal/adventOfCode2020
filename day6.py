import math
f = open("day6Input.txt")
lines = f.readlines()
cleanLines = [line.strip() for line in lines]

questions = []
all_questions = set()
total = 0
for line in cleanLines:
	if line == '': 
		for question_set in questions:
			all_questions = all_questions.intersection(question_set)
		total += len(all_questions)
		questions = []
		all_questions = set()
	else:
		question_set = set()
		for question in line:
			question_set.add(question)
			all_questions.add(question)
		questions.append(question_set)
print total