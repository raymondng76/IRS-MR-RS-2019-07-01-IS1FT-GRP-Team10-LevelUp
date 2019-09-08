
import random

def gaSearchCareerPath(careergraph, yearsExp, currjobtitle, careerendpoint):
    # universalCareerGraph = {'A': ['B',1,'C',2],'B': ['D',3],'C': ['D',3,'E',2],'D': ['G',7],'E': ['F',2],'F': ['G',2]}
    # yearsOfExperience = {'A':2,'B':3,'C':4,'D':5,'E':6,'F':8,'G':10}

    universalCareerGraph = careergraph
    yearsOfExperience = yearsExp
    currentJobTitle = currjobtitle
    careerEndPoint = careerendpoint

    # currentJobTitle = 'A'
    # careerEndPoint = 'G'
    candidateCareerPaths = []
    #currentNode = currentJobTitle

    num_iterations = 50
    GenerationSize = 10
    PathLength = 7
    mutation_prob = 5
    Generation = []
    penalty_cost = 100

    #Randomly Generate Sequences
    for i in range (GenerationSize):
        path = [0,currentJobTitle]
        currentNode = currentJobTitle
        for j in range (PathLength - 1):

            if currentNode in universalCareerGraph.keys():
                CandidateNode = universalCareerGraph[currentNode]
                if len(CandidateNode) < 2:
                    nextNode = CandidateNode[0]
                else:
                    index = random.randint(1,int(len(CandidateNode)/2))*2 - 2
                    nextNode = CandidateNode[index]
                path.append(nextNode)
                if nextNode == careerEndPoint:
                    break
                currentNode = nextNode
            else:
                break
        Generation.append(path)

    #print(Generation)

    for h in range (num_iterations):

        #score the sequences
        for i in range (len(Generation)):
            cost = 0
            for j in range (len(Generation[i])-2):
                list1 = universalCareerGraph[Generation[i][j+1]]
                for k in range (len(list1)):
                    if list1[k] == Generation[i][j+2]:
                        cost = cost + list1[k+1]
                        break
            Generation[i][0] = cost

        #check and store solution and impose penalty cost on non-solution and compute Generation Fitness Score
        GenerationFitnessScore = 0
        for i in range (len(Generation)):
            SolutionFound = False
            for j in range (len(Generation[i])-1):
                if Generation[i][j+1] == careerEndPoint:
                    SolutionFound = True
                    break
            if SolutionFound:
                existingSolution = False
                for j in range (len(candidateCareerPaths)):
                    if candidateCareerPaths[j] == Generation[i]:
                        existingSolution = True
                        break
                if not existingSolution:
                    candidateCareerPaths.append(Generation[i].copy())
            else:
                Generation[i][0] = Generation[i][0] + penalty_cost
            GenerationFitnessScore = GenerationFitnessScore + int(1/Generation[i][0]*1000)

        newGeneration = []
        for i in range(int(GenerationSize/2)):
            LuckyNumber = random.randint(1,GenerationFitnessScore)

            CumulativeNumber = 0
            for j in range(len(Generation)):
                CumulativeNumber = CumulativeNumber + int(1/Generation[j][0]*1000)
                if CumulativeNumber >= LuckyNumber:
                    newGeneration.append(Generation[j].copy())
                    break

        #newGeneration = [[8, 'A', 'C', 'E', 'F', 'G'], [11, 'A', 'B', 'D', 'G'], [11, 'A', 'B', 'D', 'G'], [11, 'A', 'B', 'D', 'G'], [8, 'A', 'C', 'E', 'F', 'G']]
        #print("New",newGeneration)

        CrossOverGen = []
        for i in range (len(newGeneration)):
            CrossOverPoint = random.randint(3,len(newGeneration[i]))
            Cpath = []
            MatchFound = False
            if newGeneration[i][CrossOverPoint-1] in universalCareerGraph.keys() and not newGeneration[i][CrossOverPoint-1]==careerEndPoint:
                for j in range (len(newGeneration)):
                    if not j == i and len(newGeneration[j]) > CrossOverPoint:
                        for k in range (int(len(universalCareerGraph[newGeneration[i][CrossOverPoint-1]])/2)):
                            if newGeneration[j][CrossOverPoint] == universalCareerGraph[newGeneration[i][CrossOverPoint-1]][k*2]:
                                MatchFound = True
                                break
                        if MatchFound:
                            for k in range (CrossOverPoint):
                                Cpath.append(newGeneration[i][k])
                            for k in range (len(newGeneration[j])-CrossOverPoint):
                                Cpath.append(newGeneration[j][CrossOverPoint + k])
                            break
                if MatchFound:
                    CrossOverGen.append(Cpath.copy())
                    #print("Match Found",CrossOverPoint)
                else:
                    CrossOverGen.append(newGeneration[i].copy())
                    #print("No Match Found")
            else:
                CrossOverGen.append(newGeneration[i].copy())
                #print("No more Node")
            CrossOverGen[i][0]=0

        #print("Cross",CrossOverGen)

        MutatedGen = []

        #Perform mutation
        for i in range (len(CrossOverGen)):
            LuckyNumber2 = random.randint(1,10)
            Mpath = []
            if LuckyNumber2 >= mutation_prob:
                MutationPoint = random.randint(3,len(CrossOverGen[i]))
                for j in range (MutationPoint):
                    Mpath.append(CrossOverGen[i][j])
                #add new nodes to the sequence
                currentNode = Mpath[MutationPoint-1]
                for j in range (PathLength-MutationPoint):
                    if currentNode in universalCareerGraph.keys() and not currentNode==careerEndPoint:
                        CandidateNode = universalCareerGraph[currentNode]
                        if len(CandidateNode) < 2:
                            nextNode = CandidateNode[0]
                        else:
                            index = random.randint(1,int(len(CandidateNode)/2))*2 - 2
                            nextNode = CandidateNode[index]
                        Mpath.append(nextNode)
                        if nextNode == careerEndPoint:
                            break
                        currentNode = nextNode
                    else:
                        break
                MutatedGen.append(Mpath.copy())
            else:
                MutatedGen.append(CrossOverGen[i].copy())

        Generation = []

        for i in range(len(newGeneration)):
            Generation.append(newGeneration[i].copy())

        for i in range(len(MutatedGen)):
            Generation.append(MutatedGen[i].copy())

        #print("Mutate",MutatedGen)

    print(candidateCareerPaths)

    lowerestCost = 1000
    for i in range(len(candidateCareerPaths)):
        if candidateCareerPaths[i][0] < lowerestCost:
            lowerestCost = candidateCareerPaths[i][0]
            bestSolutionIndex = i

    print("Shortest Career Path: ", candidateCareerPaths[bestSolutionIndex])
