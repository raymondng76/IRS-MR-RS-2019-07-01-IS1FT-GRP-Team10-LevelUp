from django import forms
from Level_Up_App.models import User, Questionaire, EducationLevel, CareerPosition

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'


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
