from pyknow import *

class SkillSetFact(Fact):
    """Fact input from derived career map"""
    pass

recommendedjobs = list()

class JobRecommender(KnowledgeEngine):
    @Rule()
    def recommend(self):
        """Recommend jobs"""
        global recommendedjobs
        recommendedjobs.append()
