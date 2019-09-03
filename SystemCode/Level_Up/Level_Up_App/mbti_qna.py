from experta import *

def scoreInputs(listInputs):
	score = 0
	for x in listInputs:
		if x == 'a':
			score += 1
		else:
			score = score
	return score

testList_ex_in = ['a','a','b','b','a']
testList_se_in = ['b','a','b','b','a']
testList_th_fe = ['b','b','b','b','a']
testList_ju_pe = ['a','a','a','a','a']
personalitylist = []


class QuestionsInput(Fact):
	ex_in = Field(int)
	se_in = Field(int)
	th_fe = Field(int)
	ju_pe = Field(int)
	pass

class Personality(KnowledgeEngine):
	# Passing in MBTI Q&A to get Character
	@Rule(QuestionsInput(ex_in=P(lambda ex_in: ex_in >= 3)), salience = 10)
	def mbti_ex_in1(self):
		global personalitylist
		personalitylist.append('E')

	@Rule(QuestionsInput(se_in=P(lambda se_in: se_in >= 3)), salience = 9)
	def mbti_se_in1(self):
		global personalitylist
		personalitylist.append('S')

	@Rule(QuestionsInput(th_fe=P(lambda th_fe: th_fe >= 3)), salience = 8)
	def mbti_th_fe1(self):
		global personalitylist
		personalitylist.append('T')

	@Rule(QuestionsInput(ju_pe=P(lambda ju_pe: ju_pe >= 3)), salience = 7)
	def mbti_ju_pe1(self):
		global personalitylist
		personalitylist.append('P')

	@Rule(QuestionsInput(ex_in=P(lambda ex_in: ex_in < 3)), salience = 10)
	def mbti_ex_in2(self):
		global personalitylist
		personalitylist.append('I')

	@Rule(QuestionsInput(se_in=P(lambda se_in: se_in < 3)), salience = 9)
	def mbti_se_in2(self):
		global personalitylist
		personalitylist.append('N')

	@Rule(QuestionsInput(th_fe=P(lambda th_fe: th_fe < 3)), salience = 8)
	def mbti_th_fe2(self):
		global personalitylist
		personalitylist.append('F')

	@Rule(QuestionsInput(ju_pe=P(lambda ju_pe: ju_pe < 3)), salience = 7)
	def mbti_ju_pe2(self):
		global personalitylist
		personalitylist.append('J')

def mbti(aList_ex_in, aList_se_in, aList_th_fe, aList_ju_pe):
	ex_in = scoreInputs(aList_ex_in)
	se_in = scoreInputs(aList_se_in)
	th_fe = scoreInputs(aList_th_fe)
	ju_pe = scoreInputs(aList_ju_pe)
	print(ex_in)
	print(se_in)
	print(th_fe)
	print(ju_pe)
	engine = Personality()
	engine.reset()  # Prepare the engine for the execution.
	engine.declare(QuestionsInput(ex_in=ex_in, se_in=se_in, th_fe=th_fe, ju_pe=ju_pe))
	engine.run()  # Run it!
	return personalitylist

# print(mbti(testList_ex_in, testList_se_in, testList_th_fe, testList_ju_pe))

recommendedjob = []

def recEndGoal(personalitylist):
	charlist = str(''.join(personalitylist))
	print(charlist)
	engine = EndGoal()
	engine.reset() # Prepare the engine for the execution.
	engine.declare(PersonalityList(charlist = charlist))
	engine.run() # Run it!
	return recommendedjob


class PersonalityList(Fact):
	charlist = Field(str)
	pass

class EndGoal(KnowledgeEngine):
	# Passing Personality List to get Job Recommendation
	@Rule(PersonalityList(charlist = 'ENTJ'))
	def ENTJ(self):
		global recommendedjob
		recommendedjob.append("CEO")

	@Rule(PersonalityList(charlist = 'ENTP'))
	def ENTP(self):
		global recommendedjob
		recommendedjob.append("Chief Information Officer")

	@Rule(PersonalityList(charlist = 'INTP'))
	def INTP(self):
		global recommendedjob
		recommendedjob.append("Chief Operating Officer")

	@Rule(PersonalityList(charlist = 'INTJ'))
	def INTJ(self):
		global recommendedjob
		recommendedjob.append("Chief Technology Officer")

	@Rule(PersonalityList(charlist = 'ENFJ'))
	def ENFJ(self):
		global recommendedjob
		recommendedjob.append("Senior Director")

	@Rule(PersonalityList(charlist = 'ENFP'))
	def ENFP(self):
		global recommendedjob
		recommendedjob.append("Senior Sales Director")

	@Rule(PersonalityList(charlist = 'INFP'))
	def INFP(self):
		global recommendedjob
		recommendedjob.append("Senior Software Director")

	@Rule(PersonalityList(charlist = 'INFJ'))
	def INFJ(self):
		global recommendedjob
		recommendedjob.append("Director")

	@Rule(PersonalityList(charlist = 'ESFJ'))
	def ESFJ(self):
		global recommendedjob
		recommendedjob.append("President")

	@Rule(PersonalityList(charlist = 'ESFP'))
	def ESFP(self):
		global recommendedjob
		recommendedjob.append("Principal Engineer")

	@Rule(PersonalityList(charlist = 'ISFP'))
	def ISFP(self):
		global recommendedjob
		recommendedjob.append("Principal Software Engineer")

	@Rule(PersonalityList(charlist = 'ISFJ'))
	def ISFJ(self):
		global recommendedjob
		recommendedjob.append("Sales Director")

	@Rule(PersonalityList(charlist = 'ESTJ'))
	def ESTJ(self):
		global recommendedjob
		recommendedjob.append("Software Director")

	@Rule(PersonalityList(charlist = 'ESTP'))
	def ESTP(self):
		global recommendedjob
		recommendedjob.append("Vice President")

	@Rule(PersonalityList(charlist = 'ISTP'))
	def ISTP(self):
		global recommendedjob
		recommendedjob.append("Senior Solution Architect")

	@Rule(PersonalityList(charlist = 'ISTJ'))
	def ISTJ(self):
		global recommendedjob
		recommendedjob.append("Professor")

# print(recEndGoal(personalitylist))
# engine.declare(PersonalityList(charlist=charlist))
