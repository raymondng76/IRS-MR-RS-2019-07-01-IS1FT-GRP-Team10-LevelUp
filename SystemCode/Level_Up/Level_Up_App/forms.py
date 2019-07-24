from django import forms
from Level_Up_App.models import User, Questionaire

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'

class QuestionaireForm(forms.ModelForm):
    class Meta():
        model = Questionaire
        fields = ['eduLevel', 'yearsExp', 'currPosition', 'careerGoal']
