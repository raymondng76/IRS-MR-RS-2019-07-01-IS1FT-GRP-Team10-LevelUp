from django.shortcuts import render
from Level_Up_App.forms import NewUserForm
from Level_Up_App.models import User
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
    user_dict = {'username': User.name}
    return render(request, 'Level_Up_App/userdetails.html', context=user_dict)
