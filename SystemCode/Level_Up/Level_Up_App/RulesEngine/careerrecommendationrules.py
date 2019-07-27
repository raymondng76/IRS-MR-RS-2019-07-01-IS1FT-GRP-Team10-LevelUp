from pyknow import *
from Level_Up_App.models import Course, Skill

class SkillGapsFact(Fact):
    """Fact input from derived career road map"""
    pass

recommendedcourses = list()

class CourseRecommender(KnowledgeEngine):
    @Rule()
    def aca_sf(self):
        """NICF-Advanced Cusomter Analytics"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def acp_sf(self):
        """NICF-PMI Agile Certified Practitioner (PMI-ACP) Preparatory Course"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def aiots_sf(self):
        """NICF-Architecting IOT Solutions"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def aisp_sf(self):
        """NICF-AISP Qualified Information Security Professional Course"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def apab(self):
        """Architecting Platforms as a Business"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def api_sf(self):
        """NICF-RESTful API Design"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def archss_sf(self):
        """NICF-Architecting Software Solutions"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def at_sf(self):
        """NICF-Agile Testing"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def baap_sf(self):
        """NICF-Business Analysis for Agile Practitioners"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def babc(self):
        """NICF-Business Agility Bootcamp"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def bead_sf(self):
        """NICF-Big Data Engineering for Analytics"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def blck_sf(self):
        """NICF-Introduction to Blockchain & DLT for Executives"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def bpr_sf(self):
        """NICF-Business Process Reengineering"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def caar_sf(self):
        """NICF-Cloud Native Solution Design"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def ca_sf(self):
        """NICF-Customer Analytics"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def cbap(self):
        """Certified Business Analysis Professional (CBAP) Preparatory Course"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def ccsp_sf(self):
        """NICF-(ISC)2 CCCP CBK Training Seminar"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def ceita_sf(self):
        """NICF-Certified Enterprise Architecture Practioner Course"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def cfdda_sf(self):
        """NICF-Containers for Deploying and Scaling Apps"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def cissp_sf(self):
        """NICF-(ISC)2 CISSP CBK Training Seminar"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def citpmp_sf(self):
        """NICF-PMP for Projects Managers"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def clessp_sf(self):
        """NICF-Certified LeSS Practitioner - Principles to Practices"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def clif_sf(self):
        """NICF-Lean IT Foundation Certification"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def cmg(self):
        """NICF-Campaign Analytics"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def cm_sf(self):
        """NICF-Communicating and Managing Change"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def cobit_sf(self):
        """NICF-COBIT 5 Foundation"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def csadl_sf(self):
        """NICF-Cybersecurity Risk Awareness"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def cscrum_sf(self):
        """NICF-Certified Scrum Master"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def csf_sf(self):
        """NICF-Client Side Foundation"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def csidl_sf(self):
        """NICF-Managing Cybersecurity Risk"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def csip_sf(self):
        """NICF-Cyber Security for ICT Professional"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def cspo(self):
        """NICF-Certified Scrum Product Owner"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def csslp_sf(self):
        """NICF-(ISC)2 CSSLP CBK Training Seminar"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def dabp(self):
        """NICF-Data Analytics Process and Best Practice"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def dag_sf(self):
        """NICF-Data Governance & Protection"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def dddm_sf(self):
        """NICF-Data Driven Decision Making"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def dfeml(self):
        """NICF-Data and Feature Engineering for Machine Learning"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def diec(self):
        """NICF-Designing Intelligent Edge Computing"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def dms_sf(self):
        """NICF-Designing Cloud-Enabled Mobile Applications"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def doea(self):
        """NICF-DevOps Engineering and Automation"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def dofbo_sf(self):
        """NICF-DevOps Foundation with BizOps"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def dps_sf(self):
        """NICF-Digital Product Strategy"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def dses_sf(self):
        """NICF-Digital & Social Engagement Strategy"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def dsma_sf(self):
        """NICF-Design Secure Mobile Architecture"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def dst_sf(self):
        """NICF-Data Storytelling"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def eamc_sf(self):
        """NICF-Enterprise Architecture Masterclass"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def eaprac_aop_sf(self):
        """NICF-Enterprise Architecture Practicum - AOP"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def eaprac_sf(self):
        """NICF-Enterprise Architecture Practium"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def eba_sf(self):
        """NICF-Strategic Business Analysis"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def eg(self):
        """e-Goverment Leadership"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def epat_sf(self):
        """NICF-Essential Practices for Agile Teams"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def esuiot_sf(self):
        """NICF-Envisioning Smart Urban IoT Solutions"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def feaiot(self):
        """NICF-Feature Engineering and Analytics using IOT Data"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def fesmdl(self):
        """NICF-Feature Extraction and Supervised Modeling with Deep Learning"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def ha(self):
        """NICF-Health Analytics"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def hss(self):
        """NICF-Humanizing Smart Systems"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def ib_sf(self):
        """NICF-Innovation Bootcamp"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def iotsec(self):
        """NICF-Securing IoT"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def issm(self):
        """NICF-Intelligent Sensing and Sense Making"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def itgl_sf(self):
        """NICF-Enterprise Digital Governance"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def itsm_csi_sf(self):
        """NICF-ITIL Continual Service Improvement Certificate"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def itsm_osa_sf(self):
        """NICF-ITIL Operational Support and Analysis Certificate"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def itsm_rcv_sf(self):
        """NICF-ITIL Release, Control and Validation Certificate"""
        global recommendedcourses
        recommendedcourses.append()
    @Rule()
    def itsm_sf(self):
        """NICF-ITIL Foundation Certification in IT Service Management"""
        global recommendedcourses
        recommendedcourses.append()
