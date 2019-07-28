from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from Level_Up_App.forms import NewUserForm, QuestionaireForm
from Level_Up_App.models import User, Questionaire
# Create your views here.
def index(request):
    form = NewUserForm()
    form_dict = {'userForm': form}
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            request.session['username'] = form.cleaned_data['name']
            form.save(commit=True)
            return redirect('Level_Up_App:questionaire')
        else:
            print("ERROR: UserForm Invalid!")
            return redirect('Level_Up_App:index')
    return render(request, 'Level_Up_App/index.html', form_dict)

def questionaire(request):
    form = QuestionaireForm()
    username = request.session['username']
    user = User.objects.get(name=username)
    form_dict = {'username': username, 'questionaire': form}
    if request.method == 'POST':
        form = QuestionaireForm(request.POST)
        if form.is_valid():
            qform = form.save(commit=False)
            qform.user = user
            qform.save()
            return redirect('Level_Up_App:index')
        else:
            print(form.errors)
            print("ERROR: QuestionaireForm invalid!")
    return render(request, 'Level_Up_App/questionaire.html', context=form_dict)
