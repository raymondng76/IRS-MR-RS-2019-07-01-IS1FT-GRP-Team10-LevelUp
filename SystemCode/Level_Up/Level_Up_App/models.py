from django.db import models
from django.urls import reverse_lazy, reverse
import json

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    careeraspiration = models.BooleanField(default=False)

    def __str__(self):
        return "Name: [{}], Have career aspiration: [{}]".format(self.name, str(self.careeraspiration))

class Questionaire(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    eduLevel = models.CharField(max_length=200)
    yearsExp = models.IntegerField(default=0)
    currPosition = models.CharField(max_length=200)
    careerGoal = models.CharField(max_length=200)

    def __str__(self):
        return """User: [{}], Highest Edu Level: [{}], Years of working exp: [{}],
                Current position: [{}], Have career goal: [{}]""".format(self.user.name, self.eduLevel, str(self.yearsExp), self.currPosition, self.careerGoal)

class PersonalityQuestionaire1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    q1EI = models.CharField(max_length=100)
    q2EI = models.CharField(max_length=100)
    q3EI = models.CharField(max_length=100)
    q4EI = models.CharField(max_length=100)
    q5EI = models.CharField(max_length=100)
    q1SN = models.CharField(max_length=100)
    q2SN = models.CharField(max_length=100)
    q3SN = models.CharField(max_length=100)
    q4SN = models.CharField(max_length=100)
    q5SN = models.CharField(max_length=100)

    def __str__(self):
        return """User: [{}]""".format(self.user)

class PersonalityQuestionaire2(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    q1TF = models.CharField(max_length=100)
    q2TF = models.CharField(max_length=100)
    q3TF = models.CharField(max_length=100)
    q4TF = models.CharField(max_length=100)
    q5TF = models.CharField(max_length=100)
    q1JP = models.CharField(max_length=100)
    q2JP = models.CharField(max_length=100)
    q3JP = models.CharField(max_length=100)
    q4JP = models.CharField(max_length=100)
    q5JP = models.CharField(max_length=100)

    def __str__(self):
        return """User: [{}]""".format(self.user)

class EducationLevel(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class CareerPosition(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name;

class Course(models.Model):
    coursecode = models.CharField(max_length=30, unique=True)
    title = models.CharField(max_length=256, unique=True)
    URL = models.URLField()
    skillRequired = models.ManyToManyField(Skill)

    def __str__(self):
        return """Course Code: [{}], Title: [{}]""".format(self.coursecode, self.title)

class CareerSkills(models.Model):
    careerpos = models.ForeignKey(CareerPosition, on_delete=models.CASCADE)
    skillRequired = models.ManyToManyField(Skill)

    def __str__(self):
        return "Career position: [{}]".format(self.careerpos)

class CareerPathMap(models.Model):
    initialpos = models.ForeignKey(CareerPosition, related_name='%(class)s_init_pos', on_delete=models.CASCADE)
    nextpos = models.ForeignKey(CareerPosition, related_name='%(class)s_next_pos', on_delete=models.CASCADE)
    yearsreq = models.IntegerField(default=0)

    def __str__(self):
        return "InitialPos: [{}], NextPos: [{}], YearsRequired: [{}]".format(self.initialpos, self.nextpos, self.yearsreq)

class CareerPathHeuristic(models.Model):
    careerpos = models.ForeignKey(CareerPosition, on_delete=models.CASCADE)
    heuristiccost = models.IntegerField(default=0)

    def __str__(self):
        return "Career Position: [{}], Heuristic Mean Cost: [{}]".format(self.careerpos, str(self.heuristiccost))

class Job(models.Model):
    name = models.ForeignKey(CareerPosition, on_delete=models.CASCADE)
    skillRequired = models.ManyToManyField(Skill)
    minSalary = models.FloatField(default=0.0)
    maxSalary = models.FloatField(default=0.0)
    eduLvl = models.ForeignKey(EducationLevel, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    URL = models.URLField()
    company = models.CharField(max_length=256)

    def __str__(self):
        return """Name: [{}],
                title: [{}],
                """.format(self.name, self.title)

class GenericInfo(models.Model):
    title = models.ForeignKey(CareerPosition, on_delete=models.CASCADE)
    eduLvl = models.ForeignKey(EducationLevel, on_delete=models.CASCADE)
    salaryRange = models.CharField(max_length=256)
    minYears = models.IntegerField(default=0)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return """Title: [{}], eduLvl: [{}], salaryRange: [{}], minYears: [{}]
            """.format(self.title, self.eduLvl, self.salaryRange, self.minYears)

class ChatbotVar(models.Model):
    persona = models.CharField(max_length=256, unique=False)
    currentPosition = models.CharField(max_length=256, unique=False)
    yearsOfWorkingExperience = models.CharField(max_length=256, unique=False)
    companyName = models.CharField(max_length=256, unique=False)
    emailAddress = models.CharField(max_length=256, unique=False)
    jobInterestedIn = models.CharField(max_length=256, unique=False)
    careerEndGoalPosition = models.CharField(max_length=256, unique=False)
    currentSkillSet = models.CharField(max_length=5124, unique=False)
    careerPref = models.CharField(max_length=256, unique=False)
    courseSkillRecommend = models.CharField(max_length=10240, unique=False)
    jobSkillRecommend = models.CharField(max_length=10240, unique=False)

    def get_persona(self):
        return self.persona
    def set_persona(self, persona):
        self.persona = persona

    def get_currentPosition(self):
        return self.currentPosition
    def set_currentPosition(self, currentPosition):
        self.currentPosition = currentPosition

    def get_yearsOfWorkingExperience(self):
        return self.yearsOfWorkingExperience
    def set_yearsOfWorkingExperience(self, yearsOfWorkingExperience):
        self.yearsOfWorkingExperience = yearsOfWorkingExperience

    def get_companyName(self):
        return self.companyName
    def set_companyName(self, companyName):
        self.companyName = companyName

    def get_emailAddress(self):
        return self.emailAddress
    def set_emailAddress(self, emailAddress):
        self.emailAddress = emailAddress

    def get_jobInterestedIn(self):
        return self.jobInterestedIn
    def set_jobInterestedIn(self, jobInterestedIn):
        self.jobInterestedIn = jobInterestedIn

    def get_careerEndGoalPosition(self):
        return self.careerEndGoalPosition
    def set_careerEndGoalPosition(self, careerEndGoalPosition):
        self.careerEndGoalPosition = careerEndGoalPosition

    def get_currentSkillset(self):
        return json.loads(self.currentSkillSet)
    def set_currentSkillset(self, currentSkillset):
        self.currentSkillset = json.dumps(currentSkillset)

    def get_careerPref(self):
        return self.careerPref
    def set_careerPref(self, careerPref):
        self.careerPref = careerPref

    def get_courseSkillRecommend(self):
        return json.loads(self.courseSkillRecommend)
    def set_courseSkillRecommend(self, courseSkillRecommend):
        self.courseSkillRecommend = json.dumps(courseSkillRecommend)

    def get_jobSkillRecommend(self):
        return json.loads(self.jobSkillRecommend)
    def set_jobSkillRecommend(self, jobSkillRecommend):
        self.jobSkillRecommend = json.dumps(jobSkillRecommend)

    def __str__(self):
        return """Persona: [{}]""".format(self.persona)

class PersonalityQuestion(models.Model):
    tag = models.CharField(max_length=10)
    question = models.CharField(max_length=256)

    def __str__(self):
        return """Tag: [{}], Question: [{}]""".format(self.tag, self.question)

class PersonalityAnswerPosition(models.Model):
    pos = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return """Pos: [{}], Answer: [{}]""".format(self.pos, self.answer)
        
class PersonalityAnswerPair(models.Model):
    tag = models.ForeignKey(PersonalityQuestion, on_delete=models.CASCADE)
    answer = models.ManyToManyField(PersonalityAnswerPosition)

    def __str__(self):
        return """Tag: [{}], Answer: [{}]""".format(self.tag.tag, self.answer)
