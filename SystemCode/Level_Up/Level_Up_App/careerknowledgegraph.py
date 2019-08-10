from Level_Up_App.models import CareerPathHeuristic, CareerPathMap, CareerPosition

class CareerPathKnowlegeGraph:
    __instance = None
    @staticmethod
    def getInstance():
        """Static accessor for the knowledge graph"""
        if CareerPathKnowlegeGraph.__instance == None:
            CareerPathKnowlegeGraph()
        return CareerPathKnowlegeGraph.__instance

    def getCareerKnowledgeMap(self):
        """Career KnowledegeMap"""
        return self.__universalcareergraph

    def getCareerPathHeuristic(self):
        """Career Path Heuristic"""
        return self.__careerpathheuristic

    def __init__(self):
        """Virtual private constructor"""
        if CareerPathKnowlegeGraph.__instance != None:
            raise Exception("Class is a singleton")
        else:
            CareerPathKnowlegeGraph.__instance = self
            careerknowledgegraph = {}
            careerpathheuristic = {}
            careerposarr = CareerPosition.objects.all()
            # Loop thru all career position and create both career path and career heuristic graph
            for cp in careerposarr:
                cpqueryset = CareerPathMap.objects.filter(initialpos__name=cp)
                chqueryset = CareerPathHeuristic.objects.filter(careerpos__name=cp)
                for qs in cpqueryset:
                    careerknowledgegraph[str(qs.initialpos)] = [str(qs.nextpos), qs.yearsreq]
                for qh in chqueryset:
                    careerpathheuristic[str(qh.careerpos)] = qh.heuristiccost
            self.__universalcareergraph = careerknowledgegraph
            self.__careerpathheuristic = careerpathheuristic
