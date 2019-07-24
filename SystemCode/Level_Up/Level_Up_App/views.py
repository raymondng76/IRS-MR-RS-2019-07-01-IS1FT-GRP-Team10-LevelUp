from django.shortcuts import render
from Level_Up_App.forms import NewUserForm, QuestionaireForm
from Level_Up_App.models import User, Questionaire
# Create your views here.
def index(request):
    form = NewUserForm()
    form_dict = {'userForm': form}
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return userdetails(request)
        else:
            print("ERROR FORM INVALID!")
    return render(request, 'Level_Up_App/index.html', form_dict)

def userdetails(request):
    form = QuestionaireForm()
    # username = request.Get.get('userForm')
    # TODO: How to get username from index.html?
    form_dict = {'username': 'USER', 'questionaire': form}
    if request.method == 'POST':
        form = QuestionaireForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    return render(request, 'Level_Up_App/userdetails.html', context=form_dict)
