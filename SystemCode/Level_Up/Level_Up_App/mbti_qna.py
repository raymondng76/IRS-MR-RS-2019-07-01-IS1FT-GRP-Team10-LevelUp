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
	# INTEGRATION DONE
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

# FOR TESTING ONLY
##print(mbti(testList_ex_in, testList_se_in, testList_th_fe, testList_ju_pe))

recommendedjob = []

### COMMENT OUT FOR TESTING ###
# def recEndGoal(personalitylist):
# 	charlist = str(''.join(personalitylist))
# 	print(charlist)
# 	engine = EndGoal()
# 	engine.reset() # Prepare the engine for the execution.
# 	engine.declare(PersonalityList(charlist = charlist))
# 	engine.run() # Run it!
# 	return recommendedjob

# FOR NEW PREFERENCE QUESTION INPUT #
def recScore(personalitylist, pref):
	recscore = 0
	prefscore = 0
	totalscore = 0
	for persona in personalitylist:
		if persona == "E":
			recscore = recscore + 3
		elif persona == "N":
			recscore = recscore + 3
		elif persona == "T":
			recscore = recscore + 3
		elif persona == "J":
			recscore = recscore
		elif persona == "I":
			recscore = recscore - 2
		elif persona == "S":
			recscore = recscore - 2
		elif persona == "F":
			recscore = recscore - 2
		else:
			recscore = recscore
	if pref == "YES":
		prefscore = prefscore + 9
	else:
		prefscore = prefscore - 6
	totalscore = 0.4 * recscore + 0.6 * prefscore
	return totalscore

class PersonalityList(Fact):
	#charlist = Field(str)
	totalscore = Field(float)
	pass

class EndGoal(KnowledgeEngine):
	# USING A RECOMMEND SCORE INSTEAD
	@Rule(PersonalityList(totalscore=P(lambda totalscore: totalscore >= 2.1)))
	def mgmt(self):
		global recommendedjob
		recommendedjob.append(["Chief Information Officer","Chief Operating Officer","Chief Technology Officer"])

	@Rule(PersonalityList(totalscore=P(lambda totalscore: totalscore < 2.1)))
	def not_mgmt(self):
		global recommendedjob
		recommendedjob.append(["Senior Director","Senior Sales Director","Senior Software Director"])

def recEndGoal(personalitylist, preference):
	recscore = float(recScore(personalitylist, preference))
	print(recscore)
	engine = EndGoal()
	engine.reset() # Prepare the engine for the execution.
	engine.declare(PersonalityList(totalscore = recscore))
	engine.run() # Run it!
	return recommendedjob
