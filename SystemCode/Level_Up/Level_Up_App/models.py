from django.db import models

EDU_CHOICES = [
    ('SECONDARY', 'Secondary'),
    ('DIPLOMA', 'Diploma'),
    ('ASSODEG', 'Associate Degree'),
    ('BACHDEG', 'Bachelor Degree'),
    ('MASTDEG', 'Master Degree'),
    ('DOCTDEG', 'Doctoral Degree'),
]

CAREER_POSITION_CHOICES = [
    ('ASSTSOFTENG', 'Assistant Software Engineer'),
    ('ASSOSOFTENG', 'Associate Software Engineer'),
    ('SOFTENG', 'Software Engineer'),
    ('SENISOFTENG', 'Senior Software Engineer'),
    ('STAFSOFTENG', 'Staff Software Engineer'),
    ('PRINSOFTENG', 'Principle Software Engineer'),
    ('SOFTMAN', 'Software Manager'),
    ('SENISOFTMAN', 'Senior Software Manager'),
    ('SOFTDIR', 'Software Director'),
    ('SENSOFTDIR', 'Senior Software Director'),
    ('SOFTVP', 'Vice President, Software'),
    ('SENSOFTVP', 'Senior Vice President, Software'),
    ('CTO', 'Chief Technology Officer'),
]

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Questionaire(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    eduLevel = models.CharField(max_length=200, choices=EDU_CHOICES, default=EDU_CHOICES[3][1])
    yearsExp = models.IntegerField(default=0)
    currPosition = models.CharField(max_length=200, choices=CAREER_POSITION_CHOICES, default=CAREER_POSITION_CHOICES[2][1])
    careerGoal = models.CharField(max_length=200, choices=CAREER_POSITION_CHOICES, default=str(CAREER_POSITION_CHOICES[-1][1]))

    def __str__(self):
        return """User: {}, Highest Edu Level: {}, Years of working exp: {},
                Current position: {}, Have career goal: {}""".format(str(User.name), eduLevel, str(yearsExp), currPosition, careerGoal)
