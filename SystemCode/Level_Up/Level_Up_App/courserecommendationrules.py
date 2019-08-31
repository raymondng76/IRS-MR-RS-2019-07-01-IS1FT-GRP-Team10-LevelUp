from experta import *
from Level_Up_App.models import Course, Skill


def getCourseSkillRequired(coursecode):
    course = Course.objects.get(coursecode=coursecode)
    skillreq = list()
    for skill in course.skillRequired.all():
        skillreq.append(str(skill))
    return skillreq

def findSkillMatch(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
    return result

class SkillGapsFact(Fact):
    """Fact input from derived career road map"""
    pass

recommendedcourses = list()

class CourseRecommender(KnowledgeEngine):
    @Rule(SkillGapsFact(skills=P(lambda skills: findSkillMatch(skills,getCourseSkillRequired(coursecode='ACA-SF')))))
    def aca_sf(self):
        """NICF-Advanced Cusomter Analytics"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='ACA-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='ACP-SF')))))
    def acp_sf(self):
        """NICF-PMI Agile Certified Practitioner (PMI-ACP) Preparatory Course"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='ACP-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='AIOTS-SF')))))
    def aiots_sf(self):
        """NICF-Architecting IOT Solutions"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='AIOTS-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='AISP-SF')))))
    def aisp_sf(self):
        """NICF-AISP Qualified Information Security Professional Course"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='AISP-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='APAB')))))
    def apab(self):
        """Architecting Platforms as a Business"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='APAB'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='API-SF')))))
    def api_sf(self):
        """NICF-RESTful API Design"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='API-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='ARCHSS-SF')))))
    def archss_sf(self):
        """NICF-Architecting Software Solutions"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='ARCHSS-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='AT-SF')))))
    def at_sf(self):
        """NICF-Agile Testing"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='AT-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='BAAP-SF')))))
    def baap_sf(self):
        """NICF-Business Analysis for Agile Practitioners"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='BAAP-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='BABC')))))
    def babc(self):
        """NICF-Business Agility Bootcamp"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='BABC'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='BEAD-SF')))))
    def bead_sf(self):
        """NICF-Big Data Engineering for Analytics"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='BEAD-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='BLCK-SF')))))
    def blck_sf(self):
        """NICF-Introduction to Blockchain & DLT for Executives"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='BLCK-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='BPR-SF')))))
    def bpr_sf(self):
        """NICF-Business Process Reengineering"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='BPR-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='CAAR-SF')))))
    def caar_sf(self):
        """NICF-Cloud Native Solution Design"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='CAAR-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='CA-SF')))))
    def ca_sf(self):
        """NICF-Customer Analytics"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='CA-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='CBAP')))))
    def cbap(self):
        """Certified Business Analysis Professional (CBAP) Preparatory Course"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='CBAP'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='CCSP-SF')))))
    def ccsp_sf(self):
        """NICF-(ISC)2 CCCP CBK Training Seminar"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='CCSP-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='CEITA-SF')))))
    def ceita_sf(self):
        """NICF-Certified Enterprise Architecture Practioner Course"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='CEITA-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='CFDDA-SF')))))
    def cfdda_sf(self):
        """NICF-Containers for Deploying and Scaling Apps"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='CFDDA-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='CISSP-SF')))))
    def cissp_sf(self):
        """NICF-(ISC)2 CISSP CBK Training Seminar"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='CISSP-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='CITPMP-SF')))))
    def citpmp_sf(self):
        """NICF-PMP for Projects Managers"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='CITPMP-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='CLESSP-SF')))))
    def clessp_sf(self):
        """NICF-Certified LeSS Practitioner - Principles to Practices"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='CLESSP-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='CLIF-SF')))))
    def clif_sf(self):
        """NICF-Lean IT Foundation Certification"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='CLIF-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='CMG')))))
    def cmg(self):
        """NICF-Campaign Analytics"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='CMG'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='CM-SF')))))
    def cm_sf(self):
        """NICF-Communicating and Managing Change"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='CM-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='COBIT-SF')))))
    def cobit_sf(self):
        """NICF-COBIT 5 Foundation"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='COBIT-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='CSADL-SF')))))
    def csadl_sf(self):
        """NICF-Cybersecurity Risk Awareness"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='CSADL-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='CSCRUM-SF')))))
    def cscrum_sf(self):
        """NICF-Certified Scrum Master"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='CSCRUM-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='CSF-SF')))))
    def csf_sf(self):
        """NICF-Client Side Foundation"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='CSF-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='CSIDL-SF')))))
    def csidl_sf(self):
        """NICF-Managing Cybersecurity Risk"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='CSIDL-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='CSIP-SF')))))
    def csip_sf(self):
        """NICF-Cyber Security for ICT Professional"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='CSIP-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='CSPO')))))
    def cspo(self):
        """NICF-Certified Scrum Product Owner"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='CSPO'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='CSSLP-SF')))))
    def csslp_sf(self):
        """NICF-(ISC)2 CSSLP CBK Training Seminar"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='CSSLP-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='DABP')))))
    def dabp(self):
        """NICF-Data Analytics Process and Best Practice"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='DABP'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='DAG-SF')))))
    def dag_sf(self):
        """NICF-Data Governance & Protection"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='DAG-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='DDDM-SF')))))
    def dddm_sf(self):
        """NICF-Data Driven Decision Making"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='DDDM-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='DFEML')))))
    def dfeml(self):
        """NICF-Data and Feature Engineering for Machine Learning"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='DFEML'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='DIEC')))))
    def diec(self):
        """NICF-Designing Intelligent Edge Computing"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='DIEC'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='DMS-SF')))))
    def dms_sf(self):
        """NICF-Designing Cloud-Enabled Mobile Applications"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='DMS-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='DOEA')))))
    def doea(self):
        """NICF-DevOps Engineering and Automation"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='DOEA'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='DOFBO-SF')))))
    def dofbo_sf(self):
        """NICF-DevOps Foundation with BizOps"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='DOFBO-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='DPS-SF')))))
    def dps_sf(self):
        """NICF-Digital Product Strategy"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='DPS-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='DSES-SF')))))
    def dses_sf(self):
        """NICF-Digital & Social Engagement Strategy"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='DSES-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='DSMA-SF')))))
    def dsma_sf(self):
        """NICF-Design Secure Mobile Architecture"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='DSMA-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='DST-SF')))))
    def dst_sf(self):
        """NICF-Data Storytelling"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='DST-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='EAMC-SF')))))
    def eamc_sf(self):
        """NICF-Enterprise Architecture Masterclass"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='EAMC-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='EAPRAC-AOP-SF')))))
    def eaprac_aop_sf(self):
        """NICF-Enterprise Architecture Practicum - AOP"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='EAPRAC-AOP-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='EAPRAC-SF')))))
    def eaprac_sf(self):
        """NICF-Enterprise Architecture Practium"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='EAPRAC-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='EBA-SF')))))
    def eba_sf(self):
        """NICF-Strategic Business Analysis"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='EBA-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='EG')))))
    def eg(self):
        """e-Goverment Leadership"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='EG'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='EPAT-SF')))))
    def epat_sf(self):
        """NICF-Essential Practices for Agile Teams"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='EPAT-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='ESUIOT-SF')))))
    def esuiot_sf(self):
        """NICF-Envisioning Smart Urban IoT Solutions"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='ESUIOT-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='FEAIOT')))))
    def feaiot(self):
        """NICF-Feature Engineering and Analytics using IOT Data"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='FEAIOT'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='FESMDL')))))
    def fesmdl(self):
        """NICF-Feature Extraction and Supervised Modeling with Deep Learning"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='FESMDL'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='HA')))))
    def ha(self):
        """NICF-Health Analytics"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='HA'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='HSS')))))
    def hss(self):
        """NICF-Humanizing Smart Systems"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='HSS'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='IB-SF')))))
    def ib_sf(self):
        """NICF-Innovation Bootcamp"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='IB-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='IOTSEC')))))
    def iotsec(self):
        """NICF-Securing IoT"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='IOTSEC'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='ISSM')))))
    def issm(self):
        """NICF-Intelligent Sensing and Sense Making"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='ISSM'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='ITGL-SF')))))
    def itgl_sf(self):
        """NICF-Enterprise Digital Governance"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='ITGL-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='ITSM-CSI-SF')))))
    def itsm_csi_sf(self):
        """NICF-ITIL Continual Service Improvement Certificate"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='ITSM-CSI-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='ITSM-OSA-SF')))))
    def itsm_osa_sf(self):
        """NICF-ITIL Operational Support and Analysis Certificate"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='ITSM-OSA-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='ITSM-RCV-SF')))))
    def itsm_rcv_sf(self):
        """NICF-ITIL Release, Control and Validation Certificate"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='ITSM-RCV-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='ITSM-SF')))))
    def itsm_sf(self):
        """NICF-ITIL Foundation Certification in IT Service Management"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='ITSM-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='ITSM-SOA-SF')))))
    def itsm_soa_sf(self):
        """NICF-Service Offerings and Agreement Certificate"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='ITSM-SOA-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='MBAP-SF')))))
    def mbap_sf(self):
        """NICF-Managing Business Analytics Projects"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='MBAP-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='MR')))))
    def mr(self):
        """NICF-Machine Reasoning"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='MR'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='MXD-SF')))))
    def mxd_sf(self):
        """NICF-Mobile User Experience Design"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='MXD-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='NMSM')))))
    def nmsm(self):
        """NICF-New Media and Sentiment Mining"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='NMSM'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='OOAD-SF')))))
    def ooad_sf(self):
        """NICF-Object Oriented Analysis & Design"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='OOAD-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='OODP-SF')))))
    def oodp_sf(self):
        """NICF-Object Oriented Design Patterns"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='OODP-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='P3O')))))
    def p3o(self):
        """NICF-Portfolio, Programme and Project Offices (P3O) - Foundation & Practitioner"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='P3O'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='PAF-SF')))))
    def paf_sf(self):
        """NICF-Persistence and Analytics Fundamentals"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='PAF-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='PA-SF')))))
    def pa_sf(self):
        """NICF-Predictive Analytics - Insights of Trends and Irregularities"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='PA-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='PE')))))
    def pe(self):
        """NICF-Platform Engineering"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='PE'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='PLS')))))
    def pls(self):
        """NICF-Platform Security"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='PLS'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='PRINCE2-SF')))))
    def prince2_sf(self):
        """NICF-PRINCE2 (PRoject IN Controlled Environments) - Foundation and Practitioner Certificate"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='PRINCE2-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='PRMLS')))))
    def prmls(self):
        """NICF-Pattern Recognition and Machine Learning Systems"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='PRMLS'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='PSUPR')))))
    def psupr(self):
        """NICF-Problem Solving using Pattern Recognition"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='PSUPR'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='PTO-SF')))))
    def pto_sf(self):
        """NICF-Product Thinking for Organisations"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='PTO-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='PYDOT-SF')))))
    def pydot_sf(self):
        """NICF-Python for Data, Ops and Things"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='PYDOT-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='RBS')))))
    def rbs(self):
        """NICF-Robotic Systems"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='RBS'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='RCS')))))
    def rcs(self):
        """NICF-Recommender Systems"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='RCS'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='RS')))))
    def rs(self):
        """NICF-Reasoning Systems"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='RS'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='SB-SF')))))
    def sb_sf(self):
        """NICF-Statistics Bootcamp"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='SB-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='SDI-SF')))))
    def sdi_sf(self):
        """NICF-Strategic Design & Innovation"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='SDI-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='SFB-SF')))))
    def sfb_sf(self):
        """NICF-Statistics for Business"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='SFB-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='SFF-SF')))))
    def sff_sf(self):
        """NICF-Statistics Futures & Foresight"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='SFF-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='SID-SF')))))
    def sid_sf(self):
        """NICF-Service Design"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='SID-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='SITP-SF')))))
    def sitp_sf(self):
        """NICF-Digital Transformation Planning"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='SITP-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='SMA-SF')))))
    def sma_sf(self):
        """NICF-Social Media Analytics"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='SMA-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='SMDL')))))
    def smdl(self):
        """NICF-Sequence Modeling with Deep Learning"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='SMDL'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='SNMF-SF')))))
    def snmf_sf(self):
        """NICF-Security Notification and Messaging Fundamentals"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='SNMF-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='SPMF-SF')))))
    def spmf_sf(self):
        """NICF-Strategic Product Market Fit"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='SPMF-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='SPMR-SF')))))
    def spmr_sf(self):
        """NICF-Strategic Product Manager"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='SPMR-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='SRSD')))))
    def srsd(self):
        """NICF-Spatial Reasoning from Sensor Data"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='SRSD'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='SSDIOT-SF')))))
    def ssdiot_sf(self):
        """NICF-Developing Smart Urban IoT Solutions"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='SSDIOT-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='SSDLA-SF')))))
    def ssdla_sf(self):
        """NICF-Secure Software Development Lifecycle for Agile"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='SSDLA-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='SSF-SF')))))
    def ssf_sf(self):
        """NICF-Server Side Foundation"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='SSF-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='STRCA-SF')))))
    def strca_sf(self):
        """NICF-Systems Thinking & Root Cause Analysis"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='STRCA-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='SUMML')))))
    def summl(self):
        """NICF-Supervised and Unsupervised Modeling with Machine Learning"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='SUMML'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='SVA-SF')))))
    def sva_sf(self):
        """NICF-Service Analytics"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='SVA-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='TA-SF')))))
    def ta_sf(self):
        """NICF-Text Analytics"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='TA-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='TE-SF')))))
    def te_sf(self):
        """NICF-Technopreneurship"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='TE-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='TPML')))))
    def tpml(self):
        """NICF-Text Processing using Machine Learning"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='TPML'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='UXD-SF')))))
    def uxd_sf(self):
        """NICF-Digital User Experience Design"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='UXD-SF'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='VSE')))))
    def vse(self):
        """NICF-Vision Systems"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='VSE'))
    @Rule(SkillGapsFact(skills=P(lambda skills:findSkillMatch(skills,getCourseSkillRequired(coursecode='WA-SF')))))
    def wa_sf(self):
        """NICF-Web Analytics & SEO"""
        global recommendedcourses
        recommendedcourses.append(Course.objects.get(coursecode='WA-SF'))
