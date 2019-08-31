from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import View, CreateView, TemplateView, ListView, DetailView, FormView
from django.views.decorators.csrf import csrf_exempt
from Level_Up_App.forms import NewUserForm, QuestionaireForm
from Level_Up_App.models import User, Questionaire, Course, Job, Skill, CareerPathMap, CareerSkills, ChatbotVar
from Level_Up_App.courserecommendationrules import SkillGapsFact, CourseRecommender, recommendedcourses
from Level_Up_App.jobrecommendationrules import getJobRecommendation
from Level_Up_App.careerknowledgegraph import CareerPathKnowledgeGraph
from Level_Up_App.CareerPathASTARSearch import searchCareerPath
from Level_Up_App.library.df_response_lib import *
import json
from enum import Enum
from Level_Up_App.chatbot_util import *

# Create your views here.
def index(request):
    form = NewUserForm()
    form_dict = {'userForm': form}
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            request.session['username'] = form.cleaned_data['name']
            request.session['careeraspiration'] = form.cleaned_data['careeraspiration']
            form.save()
            return redirect('Level_Up_App:questionaire')
        else:
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
            request.session['currPosition'] = str(form.cleaned_data['currPosition'])
            # if user checks the have career aspiration checkbox
            if request.session['careeraspiration'] == True:
                request.session['careerendpoint'] = str(form.cleaned_data['careerGoal'])
            else:
                #TODO:replace with career end point from questionaire
                request.session['careerendpoint'] = 'Chief Information Officer'
            qform.user = user
            qform.save()
            return redirect('Level_Up_App:results')
        else:
            print("Error: Questionaire form invalid!")
    return render(request, 'Level_Up_App/questionaire.html', context=form_dict)

def result(request):
    currPos = request.session['currPosition']
    careerendpoint = 'CIO' #TODO

    # Filter job recommendations
    skillset = list()
    skillset.append('C++')
    jobs = getJobRecommendation(skillset)

    skills = list()
    skills.append('ARTIFICIAL INTELLIGENCE')
    skills.append('MACHINE LEARNING')
    skills.append('DEEP LEARNING')
    # Filter course recommendation
    courses = filtercourse(skills)

    user = request.session['username']
    result_dict = {'username': user,
                'careerendpoint': careerendpoint,
                'courses': courses,
                'jobs': jobs}
    return render(request, 'Level_Up_App/results.html', result_dict)

def signup(request):
    if request.method == 'POST':
        return redirect('Level_Up_App/signupthanks')
    return render(request, 'Level_Up_App/signup.html')

def signupthanks(request):
    return render(request, 'Level_Up_App/signupthanks.html')

def courserecommendresult(request):
    courses = filtercourse(skills)
    courses_dict = {'courses': courses}
    return render(request, 'Level_Up_App/courserecommend.html', courses_dict)

def jobrecommendresult(request):
    pass

def chatbot(request):
    return render(request, 'Level_Up_App/chatbot.html')
# ************************
# DialogFlow block : START
# ************************

# dialogflow webhook fulfillment
@csrf_exempt
def webhook(request):
    # build a request object
    req = json.loads(request.body)
    # get action from json
    intent_name = req["queryResult"]["intent"]["displayName"]

# **********************
# DialogFlow Variables : DEFINE
# **********************
    resp_text = ""
# **********************
# DialogFlow intents : START
# **********************

    # Persona Curious Explorer
    if intent_name == "A_GetCareerRoadMapInfo":
        setPersona(PersonaType.CURIOUS_EXPLORER.name)
        resp_text = "The Career Road Map shows you a career path to achieve your career aspiration in the shortest time. It is generated based on anonymised data of real career advancement. Would you be interested to discover your career road map?"
    elif intent_name == "A_GetCareerRoadMapInfo - yes":
        resp_text = "Great! First, I need to know what is your current position and how long you have been in it?"
    elif intent_name == "A_GetCareerRoadMapInfo - no":
        resp_text = "Okay what else can I do for you?"
    elif intent_name == "A_GetHighestDemandJob":
        jobtitle = getHighestDemandJob()
        resp_text =  f"Currently the highest demand job is {jobtitle}"
    # Persona Curious Explorer
    elif intent_name == "A_GetServicesInfo":
        setPersona(PersonaType.CURIOUS_EXPLORER.name)
        resp_text = "I can help you develop a personalised career road map and help you look for suitable jobs and training courses. Would you like to give it a go?"
    elif intent_name == "A_GetServicesInfo - yes":
        resp_text = "Great! First, I need to know what is your current position and how long you have been in it?"
    elif intent_name == "A_GetServicesInfo - no":
        resp_text = "Okay what else can I do for you?"
    elif intent_name == "A_LookforCareerPath":
        setPersona(PersonaType.CURIOUS_EXPLORER.name)
        resp_text = "I can help you develop a personalised career road map. First, I need to know what is your current position and how long you have been in it?"
    # Persona Go Getter
    elif intent_name == "A_GetJobCompetency":
        setPersona(PersonaType.GO_GETTER.name)
        jobInterestedIn = req["queryResult"]["parameters"]["job_roles"]
        setJobInterestedIn(jobInterestedIn)
        competency = getJobCompetency(jobInterestedIn)
        # to display skills in competency as strings in reply
        resp_text =  f"{jobInterestedIn} requires the following competencies: {', '.join(str(x) for x in competency)}. Would you be interested to see a road map on how to get there?"
    elif intent_name == "A_GetJobCompetency - yes":
        resp_text = "Great! First, I need to know what is your current position and how long you have been in it?"
    elif intent_name == "A_GetJobCompetency - no":
        resp_text = "Okay what else can I do for you?"
    elif intent_name == "A_GetJobDifference":
        setPersona(PersonaType.GO_GETTER.name)
        jobtitle1 = req["queryResult"]["parameters"]["job_roles1"]
        jobtitle2 = req["queryResult"]["parameters"]["job_roles2"]
        jd1 = getJobDescription(jobtitle1)
        jd2 = getJobDescription(jobtitle2)
        resp_text = f"{jobtitle1} \n {jd1} \n {jobtitle2} \n {jd2} \n Which position are you more interested in?"
    elif intent_name == "A_GetJobDifference - custom":
        jobInterestedIn = req["queryResult"]["parameters"]["job_roles"]
        resp_text = "I see, would you like me to show you a road map on how you can get there?"
    elif intent_name == "A_GetJobDifference - custom - yes":
        resp_text = "Great! First, I need to know what is your current position and how long you have been in it?"
    elif intent_name == "A_GetJobDifference - custom - no":
        resp_text = "Okay what else can I do for you?"
    elif intent_name == "A_GetJobEducation":
        setPersona(PersonaType.GO_GETTER.name)
        jobInterestedIn = req["queryResult"]["parameters"]["job_roles"]
        setJobInterestedIn(jobInterestedIn)
        education = getJobEducationLevel(jobInterestedIn)
        resp_text =  f"{jobInterestedIn} requires {education}. Would you be interested to see a road map on how to get there?"
    elif intent_name == "A_GetJobEducation - yes":
        resp_text = "Great! First, I need to know what is your current position and how long you have been in it?"
    elif intent_name == "A_GetJobEducation - no":
        resp_text = "Okay what else can I do for you?"
    elif intent_name == "A_GetJobPath":
        setPersona(PersonaType.GO_GETTER.name)
        jobInterestedIn = req["queryResult"]["parameters"]["job_roles"]
        setJobInterestedIn(jobInterestedIn)
        resp_text = "I can help you with that! First, I need to know what is your current position and how long you have been in it?"
    elif intent_name == "A_GetJobSalary":
        setPersona(PersonaType.GO_GETTER.name)
        jobInterestedIn = req["queryResult"]["parameters"]["job_roles"]
        setJobInterestedIn(jobInterestedIn)
        salary = getJobSalary(jobInterestedIn)
        resp_text = f"On average, {jobInterestedIn} earns {salary} a month. Would you be interested to see a road map on how to get there?"
    elif intent_name == "A_GetJobSalary - yes":
        resp_text = "Great! First, I need to know what is your current position and how long you have been in it?"
    elif intent_name == "A_GetJobSalary - no":
        resp_text = "Okay what else can I do for you?"
    elif intent_name == "A_GetJobScope":
        setPersona(PersonaType.GO_GETTER.name)
        jobInterestedIn = req["queryResult"]["parameters"]["job_roles"]
        setJobInterestedIn(jobInterestedIn)
        jd = getJobDescription(jobInterestedIn)
        resp_text = f"Below is the job description of a {jobInterestedIn}: \n {jd}. \n Would you be interested to see a road map on how to get there?"
    elif intent_name == "A_GetJobScope - yes":
        resp_text = "Great! First, I need to know what is your current position and how long you have been in it?"
    elif intent_name == "A_GetJobScope - no":
        resp_text = "Okay what else can I do for you?"
    elif intent_name == "A_GetJobYears":
        setPersona(PersonaType.GO_GETTER.name)
        jobInterestedIn = req["queryResult"]["parameters"]["job_roles"]
        setJobInterestedIn(jobInterestedIn)
        years = getJobMinYearsExperience(jobInterestedIn)
        setYearsOfWorkingExperience(years)
        resp_text =  f"{jobInterestedIn} typically requires {years} years of experience. Would you be interested to see a road map on how to get there?"
    elif intent_name == "A_GetJobYears - yes":
        resp_text = "Great! First, I need to know what is your current position and how long you have been in it?"
    elif intent_name == "A_GetJobYears - no":
        resp_text = "Okay what else can I do for you?"
    # Persona Unemployed Job Seeker
    elif intent_name == "A_LookforJob":
        setPersona(PersonaType.UNEMPLOYED_JOB_SEEKER.name)
        resp_text = "I know, its tough finding a job these days. Let me help you find a suitable job! First, I need to know what was your last position and how long you had been in it?"
    # Persona Jaded Employee
    elif intent_name == "A_LookforJobChange":
        setPersona(PersonaType.JADED_EMPLOYEE.name)
        resp_text = "I am sorry to hear that. I think I can help you. First, I need to know what is your current position and how long you have been in it?"
    # PERSONA EAGER LEARNER
    elif intent_name == "A_LookforSelfImprovement":
        setPersona(PersonaType.EAGER_LEARNER.name)
        resp_text = "I am glad you are actively seeking to improve yourself. I can help you with that. First, I need to know what is your current position and how long you have been in it?"
    elif intent_name =="GiveEmailAddress":
        emailAddress = req["queryResult"]["parameters"]["emailAddress"]
    # Elicit Employment Details Intent
    elif intent_name == "D_ElicitEmployDetails":
        currentPosition = req["queryResult"]["parameters"]["job_roles"]
        setCurrentPosition(currentPosition)
        yearsOfWorkingExperience = req["queryResult"]["parameters"]["duration"]
        setYearsOfWorkingExperience(yearsOfWorkingExperience)
        if getPersona() == PersonaType.JADED_EMPLOYEE.name or getPersona() == PersonaType.CURIOUS_EXPLORER.name or getPersona() == PersonaType.GO_GETTER.name:
            #Lead to Career Aspiration Intent
            resp_text = "I have noted on your employment details. If given an opportunity, what do you aspire to be?"
        elif getPersona() == PersonaType.UNEMPLOYED_JOB_SEEKER.name or getPersona() == PersonaType.EAGER_LEARNER.name:
            # Lead to Competencies Intent
            resp_text = "I have noted your employment details."
            competencies = elicit_competence_without_endgoal(currentPosition)
            resp_text = resp_text + f"I think I can value add more in terms of career advice. May I check with you, which of the following competencies do you have? : {', '.join(str(x) for x in competencies)}"
    # Elicit Career Preferences Intent Combined
    elif intent_name == "D_ElicitEmployDetails - no":
        resp_text = "That's alright. Perhaps you can share with me if you enjoy management, technical or people roles and I can advise you a direction."
    # GET CAREER PREFERENCE
    elif intent_name == "K_GetCareerPref":
        #Get Career Preference
        careerPref = req["queryResult"]["parameters"]["career_type"]
        setCareerPref(careerPref)
        if getCareerPref() == CareerType.MANAGEMENT.name:
            resp_text = "I will suggest you gunning for the Senior Director. Sounds good?"
            careerEndGoalPosition = "Senior Director"
            setCareerEndGoalPosition(careerEndGoalPosition)
        elif getCareerPref() == CareerType.SALES.name:
            resp_text = "I will recommend to aim for the Sales Director. Do you think that's great?"
            careerEndGoalPosition = "Sales Director"
            setCareerEndGoalPosition(careerEndGoalPosition)
        elif getCareerPref() == CareerType.TECHNICAL.name:
            resp_text = "I will suggest you to become either a Technical Director or CTO. Yes?"
            careerEndGoalPosition = "Chief Technical Officer"
            setCareerEndGoalPosition(careerEndGoalPosition)
    elif intent_name == "K_GetCareerPref - yes":
        if getPersona() == PersonaType.UNEMPLOYED_JOB_SEEKER.name:
            cost, resp_career_roadmap = getCareerPath(getCurrentPosition(), getCareerEndGoalPosition())
            resp_text = f"This will be your career roadmap: {' to '.join(str(x) for x in resp_career_roadmap)} and it will take you {cost} months." + "You can consider some of these courses to achieve your goal!"
            # ELICIT COURSE RECOMMENDATIONS
            resp = courserecommendation_with_endgoal(getCurrentPosition(), getCareerEndGoalPosition(), getCurrentSkillset())
            resp = cardsWrap(resp, resp_text)
            resp = cardsAppend(resp, "Will you be interested to signup with us to learn more?")

            return JsonResponse(resp, status=200, content_type="application/json", safe=False)
        elif getPersona() == PersonaType.EAGER_LEARNER.name:
            cost, resp_career_roadmap = getCareerPath(getCurrentPosition(), getCareerEndGoalPosition())
            resp_text = f"This will be your career roadmap: {' to '.join(str(x) for x in resp_career_roadmap)} and it will take you {cost} months." + "In line with the roadmap, here are some jobs you might find interesting to consider for your next role."
            # ELICIT JOBS RECOMMENDATIONS
            resp = jobsrecommendation_with_endgoal(getCurrentPosition(), getCareerEndGoalPosition(), getCurrentSkillset())
            resp = cardsWrap(resp, resp_text)
            resp = cardsAppend(resp, "Would you like to be updated for more jobs and courses when they are available?")
            return JsonResponse(resp, status=200, content_type="application/json", safe=False)
        else:
            cost, resp_career_roadmap = getCareerPath(getCurrentPosition(), getCareerEndGoalPosition())
            # elicit competencies based on careerEndGoalPosition
            competencies = elicit_competence_with_endgoal(currentPosition, careerEndGoalPosition)
            resp_text = f"Great to hear that. This will be your career roadmap: {' to '.join(str(x) for x in resp_career_roadmap)} and it will take you {cost} months." + f"Based on the role, do you have the following competencies today? {', '.join(str(x) for x in competencies)}"
    elif intent_name == "K_GetCareerPref - yes - yes":
        resp_text = "Great! Can I have your full name and email address?"
    elif intent_name == "K_GetCareerPref - no":
        competencies = elicit_competence_without_endgoal(currentPosition)

        if getPersona() == PersonaType.UNEMPLOYED_JOB_SEEKER.name:
            resp_text = "Sure, no worries. I hope I have helped you. Maybe you can consider some of these courses to improve your skills?"
            resp = courserecommendation_without_endgoal(getCurrentPosition(), getCurrentSkillset())
            resp = cardsWrap(resp, resp_text)
            resp = cardsAppend(resp, "Will you be interested to signup with us to learn more?")
            return JsonResponse(resp, status=200, content_type="application/json", safe=False)
        elif getPersona() == PersonaType.EAGER_LEARNER.name:
            resp_text = "Sure, no worries. I hope I have helped you. Maybe you can consider some of these jobs next?"
            resp = jobsrecommendation_without_endgoal(getCurrentPosition(), getCurrentSkillset())
            resp = cardsWrap(resp, resp_text)
            resp = cardsAppend(resp, "Would you like to be updated for more jobs and courses when they are available?")
            return JsonResponse(resp, status=200, content_type="application/json", safe=False)
        else:
            resp_text = f"I think I can value add more in terms of career advice. May I check with you, which of the following competencies do you have? : {', '.join(str(x) for x in competencies)}"
    elif intent_name == "K_GetCareerPref - no - yes":
        resp_text = "Great! Can I have your full name and email address?"
    # Get Aspiration Intent Combined
    elif intent_name == "D_GetAspiration":
        #Lead to D_GetAspiration - yes Intent
        careerEndGoalPosition = req["queryResult"]["parameters"]["job_roles"]
        setCareerEndGoalPosition(careerEndGoalPosition)
        resp_text = "This is your career road map."
        cost, resp_career_roadmap = getCareerPath(getCurrentPosition(), getCareerEndGoalPosition())
        resp_text = resp_text + f"Your career roadmap is: {' to '.join(str(x) for x in resp_career_roadmap)} and it will take you {cost} months."
        if getPersona() == PersonaType.JADED_EMPLOYEE.name or getPersona() == PersonaType.CURIOUS_EXPLORER.name or getPersona() == PersonaType.GO_GETTER.name:
            ## ELICIT COMPETENCY WITH ROADMAP FUNCTION
            competencies = elicit_competence_with_endgoal(getCurrentPosition(), getCareerEndGoalPosition())
            print(competencies)
            resp_text = resp_text + f"I think I can value add more in terms of career advice. May I check with you, which of the following competencies do you have? : {', '.join(str(x) for x in competencies)}"
        elif getPersona() == PersonaType.UNEMPLOYED_JOB_SEEKER.name:
            # ELICIT COURSE RECOMMENDATIONS
            resp_text = resp_text + "You can consider some of these courses to achieve your goal!"
            resp = courserecommendation_without_endgoal(getCurrentPosition(), getCurrentSkillset())
            resp = cardsWrap(resp, resp_text)
            resp = cardsAppend(resp, "Will you be interested to signup with us to learn more?")
            return JsonResponse(resp, status=200, content_type="application/json", safe=False)
        else:
            resp_text = resp_text + "In line with the roadmap, here are some jobs you might find interesting to consider for your next role."
            resp = jobsrecommendation_with_endgoal(getCurrentPosition(), getCareerEndGoalPosition(), getCurrentSkillset())
            resp = cardsWrap(resp, resp_text)
            resp = cardsAppend(resp, "Would you like to be updated for more jobs and courses when they are available?")
            return JsonResponse(resp, status=200, content_type="application/json", safe=False)
    elif intent_name == "D_GetAspiration - yes":
        if getPersona() == PersonaType.UNEMPLOYED_JOB_SEEKER.name or getPersona() == PersonaType.EAGER_LEARNER.name:
            resp_text = "Great! Can I have your full name and email address?"
        else:
            #Lead to Competency Intent
            resp_text = "Great to hear that. Based on the following list, please key in your relevant competencies."
            pass
    elif intent_name == "D_GetAspiration - no":
        if getPersona() == PersonaType.EAGER_LEARNER.name or getPersona() == PersonaType.UNEMPLOYED_JOB_SEEKER.name:
            resp_text = "Sure, no worries, we hope to have helped!"
        else:
            resp_text = "That's alright. Perhaps you can share with me if you enjoy management, technical or people roles and I can advise you a direction."
    # ELICIT COMPETENCIES INTENT
    elif intent_name == "Wang_elicit_comp":
        currentSkillSet = req["queryResult"]["parameters"]['skills']
        setCurrentSkillset(currentSkillSet)
        if getPersona() == PersonaType.JADED_EMPLOYEE.name or getPersona() == PersonaType.GO_GETTER.name:
            resp = jobsrecommendation_with_endgoal(getCurrentPosition(), getCareerEndGoalPosition(), getCurrentSkillset())
            resp = cardsWrap(resp, "That's a great set of skills you have, here are some jobs you might find interesting:")
            resp = cardsAppend(resp, "I think I can show you some courses that might help improve you skillsets too. Would you be interested to find out more?")
            return JsonResponse(resp, status=200, content_type="application/json", safe=False)
        elif getPersona() == PersonaType.UNEMPLOYED_JOB_SEEKER.name:
            resp = jobsrecommendation_without_endgoal(getCurrentPosition(), getCurrentSkillset())
            resp = cardsWrap(resp, "That's some awesome skills you have, here are some jobs you might find interesting:")
            resp = cardsAppend(resp, "If given an opportunity, who do you aspire to be?")
            return JsonResponse(resp, status=200, content_type="application/json", safe=False)
        elif getPersona() == PersonaType.CURIOUS_EXPLORER.name:
            resp_text = "That's some awesome skills you have, here are some courses that might be interesting for you."
            resp = courserecommendation_with_endgoal(getCurrentPosition(), getCareerEndGoalPosition(), getCurrentSkillset())
            resp = cardsWrap(resp, resp_text)
            resp = cardsAppend(resp, "I think there are some jobs waiting for talented people like you. Would you be interested to find out more?")
            return JsonResponse(resp, status=200, content_type="application/json", safe=False)
        else:
            resp = courserecommendation_without_endgoal(getCurrentPosition(), getCurrentSkillset())
            resp = cardsWrap(resp, "That's some awesome skills you have, here are some courses you might find interesting:")
            resp = cardsAppend(resp, "Do you have any career aspiration in mind?")
            return JsonResponse(resp, status=200, content_type="application/json", safe=False)
    # FOLLOW UP TO COMPETENCIES INTENT - COURSES RECOMMENDATION
    elif intent_name == "Wang_elicit_comp - yes":
        if getPersona() == PersonaType.JADED_EMPLOYEE.name or getPersona() == PersonaType.GO_GETTER.name:
            resp = courserecommendation_with_endgoal(getCurrentPosition(), getCareerEndGoalPosition(), getCurrentSkillset())
            resp = cardsWrap(resp, "Here are some courses that will help improve your current standing and further your knowledge.")
            resp = cardsAppend(resp, "Do you want to sign up so that we can notify you when we find more suitable jobs or courses for you!")
            return JsonResponse(resp, status=200, content_type="application/json", safe=False)
        elif getPersona() == PersonaType.CURIOUS_EXPLORER.name:
            resp_text = "Here are some jobs you might find interesting:"
            resp = jobsrecommendation_with_endgoal(getCurrentPosition(), getCareerEndGoalPosition(), getCurrentSkillset())
            resp = cardsWrap(resp, resp_text)
            resp = cardsAppend(resp, "Would you be interested to sign up and keep in touch when we get more information?")
            return JsonResponse(resp, status=200, content_type="application/json", safe=False)
        else:
            # applies to UJS & EL
            resp_text = "That's some awesome skills you have, here are some jobs you might find interesting:"
            resp = jobsrecommendation_with_endgoal(getCurrentPosition(), getCareerEndGoalPosition(), getCurrentSkillset())
            resp = cardsWrap(resp, resp_text)
            resp = cardsAppend(resp, "I think I can show you some courses that might help improve you skillsets too. Would you be interested to find out more?")
            return JsonResponse(resp, status=200, content_type="application/json", safe=False)
    elif intent_name == "Wang_elicit_comp - yes - yes":
        resp_text = "Great! Can I have your full name and email address?"
    elif intent_name == "Wang_elicit_comp - no":
        if getPersona() == PersonaType.UNEMPLOYED_JOB_SEEKER.name:
            # GUIDE TO PREFERENCE
            resp_text = "That's alright. Perhaps you can share with me if you enjoy management, technical or people roles and I can advise you a direction."
        elif getPersona() == PersonaType.CURIOUS_EXPLORER.name or getPersona() == PersonaType.GO_GETTER.name or getPersona() == PersonaType.JADED_EMPLOYEE.name:
            resp_text = "Sure, no worries. Can I have your full name and email address if you are interested to get updated?"
        else:
            resp_text = "Great! Can I have your full name and email address?"
    # debug intent
    elif intent_name == "K_Debug":
        persona = getPersona()
        currentPosition = getCurrentPosition()
        careerEndGoalPosition = getCareerEndGoalPosition()
        resp_text = f"Persona is {persona}. "
        resp_text = resp_text + f"Current job is {currentPosition}. "
        resp_text = resp_text + f"Career End Goal Job is {careerEndGoalPosition}. "
    # catch all response
    else:
        resp_text = "Unable to find a matching intent. Try again."
    resp = {"fulfillmentText": resp_text}
    return JsonResponse(resp, status=200, content_type="application/json", safe=False)
# **********************
# DialogFlow intents : END
# **********************

# **********************
# UTIL FUNCTIONS : START
# **********************
def filtercourse(skills):
    # Declare course recommendation rules and build facts
    engine = CourseRecommender()
    engine.reset()
    engine.declare(SkillGapsFact(skills=skills))
    engine.run()
    return recommendedcourses

def processIncomingSkillset(skillset):
    userSkill=list()
    for skill in skillset:
        userSkill.append(skill.upper())
    return userSkill

def aStarsearchwrapper(currPos, endpt):
    cpkg = CareerPathKnowledgeGraph()
    careerkg = cpkg.getCareerKnowledgeMap()
    careerph = cpkg.getCareerPathHeuristic()
    return searchCareerPath(careerkg, careerph, currPos, endpt)

class PersonaType(Enum):
    CURIOUS_EXPLORER = 1
    GO_GETTER = 2
    JADED_EMPLOYEE = 3
    UNEMPLOYED_JOB_SEEKER = 4
    EAGER_LEARNER = 5

class CareerType(Enum):
    MANAGEMENT = 1
    SALES = 2
    TECHNICAL = 3
# **********************
# UTIL FUNCTIONS : END
# **********************
