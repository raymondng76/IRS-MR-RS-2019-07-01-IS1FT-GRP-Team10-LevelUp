from django.db import models
from django.urls import reverse_lazy, reverse

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Questionaire(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    eduLevel = models.CharField(max_length=200)
    yearsExp = models.IntegerField(default=0)
    currPosition = models.CharField(max_length=200)
    careerGoal = models.CharField(max_length=200)

    def __str__(self):
        return """User: [{}], Highest Edu Level: [{}], Years of working exp: [{}],
                Current position: [{}], Have career goal: [{}]""".format(self.user.name, self.eduLevel, str(self.yearsExp), self.currPosition, self.careerGoal)

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
        return """Course Code: [{}], Title: [{}], URL: [{}], Skills Required: [{}]""".format(self.coursecode, self.title, str(object=self.URL), str(self.skillRequired))

class CareerSkills(models.Model):
    careerpos = models.ForeignKey(CareerPosition, on_delete=models.CASCADE)
    skillRequired = models.ManyToManyField(Skill)

    def __str__(self):
        return """Career position: """.format(self.careerpos)

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
    skillRequired = models.ForeignKey(Skill, on_delete=models.CASCADE)
    minSalary = models.FloatField(default=0.0)
    maxSalary = models.FloatField(default=0.0)
    eduLvl = models.ForeignKey(EducationLevel, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    URL = models.URLField()
    description = models.CharField(max_length=5000)
    company = models.CharField(max_length=256)

    def __str__(self):
        return """Name: [{}],
                skillRequired: [{}],
                minSalary: [{}],
                maxSalary: [{}],
                eduLvl: [{}],
                title: [{}],
                """.format(self.name, str(self.skillRequired), str(self.minSalary), str(self.maxSalary),
                    str(self.eduLvl), self.title)
