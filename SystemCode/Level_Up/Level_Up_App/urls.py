from django.urls import path
from Level_Up_App import views

app_name = 'Level_Up_App'

urlpatterns = [
    path('', views.index, name='index'),
    path('questionaire/', views.questionaire, name='questionaire'),
    path('results/', views.result, name='results'),
]
