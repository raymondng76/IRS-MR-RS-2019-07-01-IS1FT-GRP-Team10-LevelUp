from django.urls import path
from Level_Up_App import views

app_name = 'Level_Up_App'

urlpatterns = [
    path('userdetails/', views.userdetails, name='userdetails')
]
