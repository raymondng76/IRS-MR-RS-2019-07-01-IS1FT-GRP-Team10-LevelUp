from Level_Up_App.models import Job, Skill, CareerPosition, CareerSkills

def getJobRecommendation(skillset):
    return getMatchJob(skillset)

def getMatchJob(skills):
    joblist = list()
    jobs = Job.objects.all()
    for job in jobs:
        skillreq = job.skillRequired.all()
        if matchSkills(skillreq, skills):
            joblist.append(job)
    return joblist

def getMatchJobWithPosition(skills, careerPos):
    joblist = []
    jobs = Job.objects.all()
    careerPos = CareerPosition.objects.get(name=careerPos)
    for job in jobs:
        skillreq = job.skillRequired.all()
        if matchSkills(skillreq, skills):
            if job.name == careerPos:
                joblist.append(job)
    return joblist

def matchSkills(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if str(x) == str(y):
                result = True
                return result
    return result
