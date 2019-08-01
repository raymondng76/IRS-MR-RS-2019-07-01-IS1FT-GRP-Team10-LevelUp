import os
import django
from django_xlspopulator.populator import Populator
os.environ.setdefault('DJANGO_SETTING_MODULE','Level_Up.settings')
django.setup()
from Level_Up_App.models import Course

pop = Populator("D:/OneDriveNUS/OneDrive - National University of Singapore/MR_RS_Project/Course Recommendation Rules_Formatted.xlsx", Course)
pop.populate()
