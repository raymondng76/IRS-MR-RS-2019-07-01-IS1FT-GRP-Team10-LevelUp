from django.urls import path
from Level_Up_App import views

app_name = 'Level_Up_App'

urlpatterns = [
    path('', views.index, name='index'),
    path('questionaire/', views.questionaire, name='questionaire'),
    path('results/', views.result, name='results'),
    path('courserecommend/', views.courserecommendresult, name='courserecommend'),
    path('jobrecommend/', views.jobrecommendresult, name='jobrecommend'),
    path('signup/', views.signup, name='signup'),
    path('signupthanks/', views.signupthanks, name='signupthanks'),
    path('chatbot/', views.chatbot, name='chatbot')
]
