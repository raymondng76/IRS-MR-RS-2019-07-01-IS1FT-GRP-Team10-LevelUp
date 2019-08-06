
universalCareerGraph = {'A': ['B',0,'C',2],'B': ['D',3],'C': ['D',3,'E',2],'D': ['G',7],'E': ['F',2],'F': ['G',2]}
yearsOfExperience = {'A':2,'B':3,'C':4,'D':5,'E':6,'F':8,'G':10}

currentJobTitle = 'A'
careerEndPoint = 'G'
candidateCareerPaths = [[0,0,currentJobTitle]]
currentNode = currentJobTitle
nextNode = currentJobTitle
index = 0

while currentNode != careerEndPoint:

    WL1 = universalCareerGraph[currentNode]
    count = int(len(WL1)/2)

    #Create Branches if necessary
    if count > 1:
        for i in range(len(candidateCareerPaths)):
            if candidateCareerPaths[i][len(candidateCareerPaths[i])-1] == currentNode:
                for j in range(count-1):
                    candidateCareerPaths.append(candidateCareerPaths[i].copy())
                break

    for i in range(count):
        cost = yearsOfExperience[careerEndPoint] - yearsOfExperience[WL1[i*2]]
        for j in range(len(candidateCareerPaths)):
            if candidateCareerPaths[j][len(candidateCareerPaths[j])-1] == currentNode:
                candidateCareerPaths[j][1]=candidateCareerPaths[j][1]+WL1[i*2+1]
                candidateCareerPaths[j][0]=cost + candidateCareerPaths[j][1]
                candidateCareerPaths[j].append(WL1[i*2])
                break

    currentCost = 100
    for i in range(len(candidateCareerPaths)):
        if currentCost>candidateCareerPaths[i][0]:
            currentCost = candidateCareerPaths[i][0]
            nextNode = candidateCareerPaths[i][len(candidateCareerPaths[i])-1]
            index = i

    currentNode = nextNode

print("Shortest Career Path Found is", candidateCareerPaths[index][0], "Years")
for i in range(len(candidateCareerPaths[index])-2):
    print(candidateCareerPaths[index][i+2])



