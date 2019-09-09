from django.urls import path
from Level_Up_App import views

app_name = 'Level_Up_App'

urlpatterns = [
    path('', views.index, name='index'),
    path('questionaire/', views.questionaire, name='questionaire'),
    path('results/', views.result, name='results'),
    path('personalityquestionaire1/', views.personalityquestionaire1, name='personalityquestionaire1'),
    path('personalityquestionaire2/', views.personalityquestionaire2, name='personalityquestionaire2'),
    path('chooseendpoint/', views.chooseendpoint, name='chooseendpoint'),
    path('usercareergoal/', views.usercareergoal, name='usercareergoal'),
    path('userskill/', views.userSkill, name='userskill')
]
