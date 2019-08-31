from django.db.models import Count
from Level_Up_App.models import CareerSkills, CareerPosition, Skill, Job, GenericInfo, CareerPathMap, ChatbotVar
from Level_Up_App.courserecommendationrules import CourseRecommender, SkillGapsFact, recommendedcourses
from Level_Up_App.jobrecommendationrules import getJobRecommendation
from Level_Up_App.careerknowledgegraph import *
from Level_Up_App.CareerPathASTARSearch import *


def getJobCompetency(jobtitle):
    jobcompetency = list()
    careerpos = CareerPosition.objects.get(name=jobtitle)
    filterCareerPos = CareerSkills.objects.get(careerpos=careerpos)
    skillreq = filterCareerPos.skillRequired.all()
    if len(skillreq) > 20:
        skillreq = skillreq[:20]
    for skill in skillreq:
        jobcompetency.append(str(skill))
    return jobcompetency

def getHighestDemandJob():
    highest = 0
    allcareerpos = CareerPosition.objects.all()
    hdjob = allcareerpos[0].name
    for pos in allcareerpos:
        count = Job.objects.filter(name=pos).count()
        if count > highest:
            highest = count
            hdjob = pos.name
    return hdjob

def getJobEducationLevel(jobtitle):
    return str(queryGenericInfo(jobtitle).eduLvl)

def getJobSalary(jobtitle):
    return str(queryGenericInfo(jobtitle).salaryRange)

def getJobDescription(jobtitle):
    return str(queryGenericInfo(jobtitle).description)

def getJobMinYearsExperience(jobtitle):
    return str(queryGenericInfo(jobtitle).minYears)

def queryGenericInfo(jobtitle):
    careerpos = CareerPosition.objects.get(name=jobtitle)
    return GenericInfo.objects.get(title=careerpos)

def getCareerPath(currentjobtitle, aspiredjobtitle):
    cpkg = CareerPathKnowledgeGraph()
    ckm = cpkg.getCareerKnowledgeMap()
    cph = cpkg.getCareerPathHeuristic()
    return searchCareerPath(ckm, cph, currentjobtitle, aspiredjobtitle)

#****************************************
# Methods for elicit competence : START
#****************************************
def elicit_competence_with_endgoal(currPos, endGoal):
    # Get career path
    cost, careerPath = getCareerPath(currPos, endGoal)
    # Get next pos from career path
    nextpos = careerPath[1]
    # Get list of competencies to ask user
    compList = getListofCompetencetoAskUserWithCRoadMap(currPos, nextpos)
    if len(compList) > 20:
        compList = compList[:20]
    return compList

def elicit_competence_without_endgoal(currPos):
    compList = getListofCompetencetoAskUserWithoutCRoadMap(currPos)
    if len(compList) > 20:
        compList = compList[:20]
    return compList
#****************************************
# Methods for elicit competence : END
#****************************************
#****************************************
# Methods for jobs recomendation : START
#****************************************
def jobsrecommendation_with_endgoal(currPos, endGoal, userCompetence):
    if not userCompetence:
        return list()
    competenceList = elicit_competence_with_endgoal(currPos, endGoal)
    competenceList.append(userCompetence)
    return wrapJobRecommendation(getJobRecommendation(competenceList))

def jobsrecommendation_without_endgoal(currPos, userCompetence):
    if not userCompetence:
        return list()
    competenceList = elicit_competence_without_endgoal(currPos)
    competenceList.append(userCompetence)
    return wrapJobRecommendation(getJobRecommendation(competenceList))
#****************************************
# Methods for jobs recommendation : END
#****************************************
#*****************************************
# Methods for course recomendation : START
#*****************************************
def courserecommendation_with_endgoal(currPos, endGoal, userCompetence):
    origialCompetenceList = elicit_competence_with_endgoal(currPos, endGoal)
    if set(userCompetence) == set(origialCompetenceList):
        return list()
    remainList = [skills for skills in userCompetence if skills not in origialCompetenceList]
    return wrapCourseRecommendation(getCourseRecommendation(remainList))

def courserecommendation_without_endgoal(currPos, userCompetence):
    origialCompetenceList = elicit_competence_without_endgoal(currPos)
    if set(userCompetence) == set(origialCompetenceList):
        return list()
    remainList = [skills for skills in userCompetence if skills not in origialCompetenceList]
    return wrapCourseRecommendation(getCourseRecommendation(remainList))

def getCourseRecommendation(skillgap):
    engine = CourseRecommender()
    engine.reset()
    engine.declare(SkillGapsFact(skills=skillgap))
    engine.run()
    return recommendedcourses
#*****************************************
# Methods for course recomendation : END
#*****************************************
def getListofCompetencetoAskUserWithoutCRoadMap(currPos): # Input is a string
    currSkillList = getCareerSkillList(currPos)
    nextSkillList = getCombinedSkillReqFromNextPos(currPos)
    return [skills for skills in nextSkillList if skills not in currSkillList] # This is a list of skills to ask user

def getListofCompetencetoAskUserWithCRoadMap(currPos, nextPos): # Both input are strings
    currSkillList = getCareerSkillList(currPos)
    nextposSkillList = getCareerSkillList(nextPos)
    return [skills for skills in nextposSkillList if skills not in currSkillList] # This is a list of skills to ask user

def getCareerSkillList(pos): # Input is a string
    careerpos = CareerPosition.objects.get(name=pos)
    careerSkills = CareerSkills.objects.get(careerpos=careerpos)
    skillList = list()
    for skill in careerSkills.skillRequired.all():
        skillList.append(skill)
    return skillList # This is a list of all the skills required for this position

def getCombinedSkillReqFromNextPos(currPos): #Input is a string
    # Get combined list of next pos
    nextposlist = getCombinedListofNextPos(currPos)
    nextposskilllist = list()
    for pos in nextposlist:
        careerSkills = CareerSkills.objects.get(careerpos=pos)
        for cs in careerSkills.skillRequired.all():
            nextposskilllist.append(cs)
    return nextposskilllist # This is a list of skills

def getCombinedListofNextPos(currPos): # Input is string
    # Get career path map
    careerPathMap = getCareerPathMap(currPos)
    nextposlist = list()
    for cp in careerPathMap:
        nextposlist.append(cp.nextpos)
    return nextposlist # This is a list of all next positions available

def getCareerPathMap(currPos): # Input is string
    # Get current pos object
    currCareerPos = CareerPosition.objects.get(name=currPos)
    # Get career path map object filter by career pos object
    careerPath = CareerPathMap.objects.filter(initialpos=currCareerPos)
    return careerPath # This is a queryset of careerpath
#*****************************************
# Methods for chat bot variable : START
#*****************************************
def getPersona():
    cbv = getChatbotVar()
    return cbv.get_persona()
def setPersona(persona):
    cbv = getChatbotVar()
    cbv.set_persona(persona)
    cbv.save()

def getCurrentPosition():
    cbv = getChatbotVar()
    return cbv.get_currentPosition()
def setCurrentPosition(currentPosition):
    cbv = getChatbotVar()
    cbv.set_currentPosition(currentPosition)
    cbv.save()

def getYearsOfWorkingExperience():
    cbv = getChatbotVar()
    return cbv.get_yearsOfWorkingExperience()
def setYearsOfWorkingExperience(yearsOfWorkingExperience):
    cbv = getChatbotVar()
    cbv.set_yearsOfWorkingExperience(yearsOfWorkingExperience)
    cbv.save()

def getCompanyName():
    cbv = getChatbotVar()
    return cbv.get_companyName()
def setCompanyName(companyName):
    cbv = getChatbotVar()
    cbv.set_companyName(companyName)
    cbv.save()

def getEmailAddress():
    cbv = getChatbotVar()
    return cbv.get_emailAddress()
def setEmailAddress(emailAddress):
    cbv = getChatbotVar()
    cbv.set_emailAddress(emailAddress)
    cbv.save()

def getJobInterestedIn():
    cbv = getChatbotVar()
    return cbv.get_jobInterestedIn()
def setJobInterestedIn(jobInterestedIn):
    cbv = getChatbotVar()
    cbv.set_jobInterestedIn(jobInterestedIn)
    cbv.save()

def getCareerEndGoalPosition():
    cbv = getChatbotVar()
    return cbv.get_careerEndGoalPosition()
def setCareerEndGoalPosition(careerEndGoalPosition):
    cbv = getChatbotVar()
    cbv.set_careerEndGoalPosition(careerEndGoalPosition)
    cbv.save()

def getCurrentSkillset():
    cbv = getChatbotVar()
    return cbv.get_currentSkillset()
def setCurrentSkillset(currentSkillset):
    cbv = getChatbotVar()
    cbv.set_currentSkillset(currentSkillset)
    cbv.save()

def getCareerPref():
    cbv = getChatbotVar()
    return cbv.get_careerPref()
def setCareerPref(careerPref):
    cbv = getChatbotVar()
    cbv.set_careerPref(careerPref.upper())
    cbv.save()

def getCourseSkillRecommendation():
    cbv = getChatbotVar()
    return cbv.get_courseSkillRecommend()
def setCourseSkillRecommendation(courseSkillRecommend):
    cbv = getChatbotVar()
    cbv.set_courseSkillRecommend(courseSkillRecommend)
    cbv.save()

def getJobSkillRecommendation():
    cbv = getChatbotVar()
    return cbv.get_jobSkillRecommend()
def setJobSklllRecommendation(jobSkillRecommend):
    cbv = getChatbotVar()
    cbv.set_jobSkillRecommend(jobSkillRecommend)
    cbv.save()

def getChatbotVar():
    return ChatbotVar.objects.get(pk=1)
#*****************************************
# Methods for chat bot variable : END
#*****************************************

#*********************************************
# Methods for Facebook button wrapper : START
#*********************************************
def wrapCourseRecommendation(courseList):
    clist = courseList
    if len(courseList) > 10:
        clist = courseList[:10]
    resp = {}
    resp['fulfillmentText'] = "Error showing course recommendation!"
    resp['fulfillmentMessages'] = []
    for course in clist:
        resp['fulfillmentMessages'].append(
        buildCard(
            title=course.title,
            subtitle=course.coursecode,
            imageUrl="https://assistant.google.com/static/images/molecule/Molecule-Formation-stop.png",
            cardText="Course Link",
            cardUrl=course.URL
        ))
    return resp

def wrapJobRecommendation(jobList):
    jlist = jobList
    if len(jobList) > 10:
        jlist = jobList[:10]
    resp = {}
    resp['fulfillmentText'] = "Error showing job recommendation!"
    resp['fulfillmentMessages'] = []
    for job in jlist:
        resp['fulfillmentMessages'].append(
        buildCard(
            title=job.title,
            subtitle=job.company,
            imageUrl="https://assistant.google.com/static/images/molecule/Molecule-Formation-stop.png",
            cardText="Job Link",
            cardUrl=job.URL
        ))
    return resp

def buildCard(title, subtitle, imageUrl, cardText, cardUrl):
    card = {
        "card": {
            "title": title,
            "subtitle": subtitle,
            "imageUri": imageUrl,
            "buttons":[
                {
                    "text": cardText,
                    "postback": cardUrl
                }
            ]
        }
    }
    return card
#*********************************************
# Methods for Facebook button wrapper : END
#*********************************************

#*********************************************
# Methods for Facebook Cards Text : START
#*********************************************

def signUp():
    resp = {}
    resp['fulfillmentText'] = "Error showing signup button!"
    resp['fulfillmentMessages'] = [
        {
            "card": {
            "title": "Level Up",
            "subtitle": "Your Personal Career Coach",
            "imageUri": "https://assistant.google.com/static/images/molecule/Molecule-Formation-stop.png",
            "buttons":[
                    {
                    "text": "Sign Up Here!",
                    "postback": "https://www.google.com/"
                    }
                ]
            }
        }
    ]
    return resp

def cardsAppend(cardsRec, appendText):
    respText = cardsRec
    cardsRec['fulfillmentMessages'].append({
        "text":{
            "text": [appendText]
            }
        },)
    return respText

def cardsWrap(cardsRec, insertText):
    respText = cardsRec
    cardsRec['fulfillmentMessages'].insert(0,{
        "text":{
            "text": [insertText]
            }
        },)
    return respText

#*********************************************
# Methods for Facebook Cards Text : END
#*********************************************
