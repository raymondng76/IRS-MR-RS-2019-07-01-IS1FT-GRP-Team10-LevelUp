from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Level_Up_App/index.html')
