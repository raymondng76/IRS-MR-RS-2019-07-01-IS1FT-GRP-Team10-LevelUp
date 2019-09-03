from django import forms
from Level_Up_App.models import User, Questionaire, EducationLevel, CareerPosition, PersonalityQuestion, PersonalityAnswerPair, PersonalityAnswerPosition, PersonalityQuestionaire1, PersonalityQuestionaire2

def getPersonalityQuestionStr(tag):
    pq = PersonalityQuestion.objects.get(tag=tag)
    return str(pq.question)

def getPersonalityAnswerPair(tag):
    pq = PersonalityQuestion.objects.get(tag=tag)
    papair = PersonalityAnswerPair.objects.get(tag=pq)
    allAns = papair.answer.all()
    ansA = allAns.get(pos='a')
    ansB = allAns.get(pos='b')
    return ((ansA.answer, ansA.answer), (ansB.answer, ansB.answer))

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['name', 'careeraspiration']
        labels = {
            'name' : 'Your name:',
            'careeraspiration' : 'Do you have a career you aspire to? ',
        }

class QuestionaireForm(forms.ModelForm):
    eduLevel = forms.ModelChoiceField(label='Highest education level', queryset=EducationLevel.objects.all())
    currPosition = forms.ModelChoiceField(label='Current working position', queryset=CareerPosition.objects.all())
    careerGoal = forms.ModelChoiceField(label='Desired career goal', queryset=CareerPosition.objects.all())
    class Meta():
        model = Questionaire
        fields = ['eduLevel', 'yearsExp', 'currPosition', 'careerGoal']
        labels = {
            'yearsExp' : 'Years of working experience',
        }

class PersonalityQuestionaire1Form(forms.ModelForm):
    q1EI = forms.ChoiceField(label=getPersonalityQuestionStr('q1EI'), choices=getPersonalityAnswerPair('q1EI'))
    q2EI = forms.ChoiceField(label=getPersonalityQuestionStr('q2EI'), choices=getPersonalityAnswerPair('q2EI'))
    q3EI = forms.ChoiceField(label=getPersonalityQuestionStr('q3EI'), choices=getPersonalityAnswerPair('q3EI'))
    q4EI = forms.ChoiceField(label=getPersonalityQuestionStr('q4EI'), choices=getPersonalityAnswerPair('q4EI'))
    q5EI = forms.ChoiceField(label=getPersonalityQuestionStr('q5EI'), choices=getPersonalityAnswerPair('q5EI'))
    q1SN = forms.ChoiceField(label=getPersonalityQuestionStr('q1SN'), choices=getPersonalityAnswerPair('q1SN'))
    q2SN = forms.ChoiceField(label=getPersonalityQuestionStr('q2SN'), choices=getPersonalityAnswerPair('q2SN'))
    q3SN = forms.ChoiceField(label=getPersonalityQuestionStr('q3SN'), choices=getPersonalityAnswerPair('q3SN'))
    q4SN = forms.ChoiceField(label=getPersonalityQuestionStr('q4SN'), choices=getPersonalityAnswerPair('q4SN'))
    q5SN = forms.ChoiceField(label=getPersonalityQuestionStr('q5SN'), choices=getPersonalityAnswerPair('q5SN'))
    class Meta():
        model = PersonalityQuestionaire1
        fields = ['q1EI', 'q2EI', 'q3EI', 'q4EI', 'q5EI', 'q1SN', 'q2SN', 'q3SN', 'q4SN', 'q5SN']

class PersonalityQuestionaire2Form(forms.ModelForm):
    q1TF = forms.ChoiceField(label=getPersonalityQuestionStr('q1TF'), choices=getPersonalityAnswerPair('q1TF'))
    q2TF = forms.ChoiceField(label=getPersonalityQuestionStr('q2TF'), choices=getPersonalityAnswerPair('q2TF'))
    q3TF = forms.ChoiceField(label=getPersonalityQuestionStr('q3TF'), choices=getPersonalityAnswerPair('q3TF'))
    q4TF = forms.ChoiceField(label=getPersonalityQuestionStr('q4TF'), choices=getPersonalityAnswerPair('q4TF'))
    q5TF = forms.ChoiceField(label=getPersonalityQuestionStr('q5TF'), choices=getPersonalityAnswerPair('q5TF'))
    q1JP = forms.ChoiceField(label=getPersonalityQuestionStr('q1JP'), choices=getPersonalityAnswerPair('q1JP'))
    q2JP = forms.ChoiceField(label=getPersonalityQuestionStr('q2JP'), choices=getPersonalityAnswerPair('q2JP'))
    q3JP = forms.ChoiceField(label=getPersonalityQuestionStr('q3JP'), choices=getPersonalityAnswerPair('q3JP'))
    q4JP = forms.ChoiceField(label=getPersonalityQuestionStr('q4JP'), choices=getPersonalityAnswerPair('q4JP'))
    q5JP = forms.ChoiceField(label=getPersonalityQuestionStr('q5JP'), choices=getPersonalityAnswerPair('q5JP'))
    class Meta():
        model = PersonalityQuestionaire2
        fields = ['q1TF', 'q2TF', 'q3TF', 'q4TF', 'q5TF', 'q1JP', 'q2JP', 'q3JP', 'q4JP', 'q5JP']
