from django.db import models
from django.urls import reverse

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Level_Up_App:questionaire', kwargs={'pk': self.pk})
        #return reverse('Level_Up_App:questionaire')

class Questionaire(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    eduLevel = models.CharField(max_length=200)
    yearsExp = models.IntegerField(default=0)
    currPosition = models.CharField(max_length=200)
    careerGoal = models.CharField(max_length=200)

    def __str__(self):
        return """User: [{}], Highest Edu Level: [{}], Years of working exp: [{}],
                Current position: [{}], Have career goal: [{}]""".format(self.user.name, self.eduLevel, str(self.yearsExp), self.currPosition, self.careerGoal)

    def get_absolute_url(self):
        return reverse('Level_Up_App:index') #TODO: Update to next view

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
        return """Course Code: [{}], Title: [{}], URL: [{}], Skills Required: [{}]""".format(self.coursecode, self.title, str(object=self.URL), self.skillRequired)
