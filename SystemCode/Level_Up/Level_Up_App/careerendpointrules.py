from pyknow import *

class QuestionaireFact(Fact):
    """Fact input from the questionaire"""
    pass

careerendpoint = ''

class CareerEndPointRecommender(KnowledgeEngine):
    @Rule()
    def recommend(self):
        """Recommend Career End Point"""
        global careerendpoint
        careerendpoint = ''
