from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Questionaire(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    EDU_CHOICES = [
        ('SECONDARY', 'Secondary'),
        ('DIPLOMA', 'Diploma'),
        ('ASSODEG', 'Associate Degree'),
        ('BACHDEG', 'Bachelor Degree'),
        ('MASTDEG', 'Master Degree'),
        ('DOCTDEG', 'Doctoral Degree'),
    ]
    eduLevel = models.CharField(max_length=200, choices=EDU_CHOICES, default=EDU_CHOICES[3][1])
    yearsExp = models.IntegerField(default=0)
    CAREER_POSITION_CHOICES = [
        ('ASSOSOFTENG', 'Associate Software Engineer'),
        ('SOFTENG', 'Software Engineer'),
        ('SOFTSALENG', 'Software Sales Engineer'),
        ('SENISOFTENG', 'Senior Software Engineer'),
        ('PRINSOFTENG', 'Principle Software Engineer'),
        ('SOFTMAN', 'Software Manager'),
        ('SOFTSALMAN', 'Software Sales Manager'),
        ('SENISOFTMAN', 'Senior Software Manager'),
        ('SENSSOFTSALMAN', 'Senior Software Sales Manager'),
        ('SOFTDIR', 'Software Director'),
        ('SOFTSALDIR', 'Software Sales Director'),
        ('SENSOFTDIR', 'Senior Software Director'),
        ('SENSOFTSALDIR', 'Senior Software Sales Director'),
        ('SOFTVP', 'Vice President, Software'),
        ('SENSOFTVP', 'Senior Vice President, Software'),
        ('CTO', 'Chief Technology Officer'),
        ('CIO', 'Chief Information Officer'),
    ]
    currPosition = models.CharField(max_length=200, choices=CAREER_POSITION_CHOICES, default=CAREER_POSITION_CHOICES[2][1])
    careerGoal = models.CharField(max_length=200, choices=CAREER_POSITION_CHOICES, default=CAREER_POSITION_CHOICES[2][1])

    def __str__(self):
        return """User: [{}], Highest Edu Level: [{}], Years of working exp: [{}],
                Current position: [{}], Have career goal: [{}]""".format(self.user.name, self.eduLevel, str(self.yearsExp), self.currPosition, self.careerGoal)

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
