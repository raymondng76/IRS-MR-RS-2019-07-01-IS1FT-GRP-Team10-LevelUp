from django.urls import path
from Level_Up_App import views

app_name = 'Level_Up_App'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('questionaire/', views.QuestionaireView.as_view(), name='questionaire')
]
