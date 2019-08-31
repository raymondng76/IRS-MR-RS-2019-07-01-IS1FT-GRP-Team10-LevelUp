def searchCareerPath(careergraph, careerheuristic, currjobtitle, careerendpoint):

    universalCareerGraph = careergraph
    yearsOfExperience = careerheuristic
    currentJobTitle = currjobtitle
    careerEndPoint = careerendpoint

    candidateCareerPaths = [[0,0,currentJobTitle]]
    currentNode = currentJobTitle
    nextNode = currentJobTitle
    index = 0
    newNodeFound = True

    while currentNode != careerEndPoint and newNodeFound:

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
            cost = yearsOfExperience[careerEndPoint] - yearsOfExperience[WL1[i*2]] #compute heuristic cost

            if i == 0: #append to exiting path
                candidateCareerPaths[index][1]=candidateCareerPaths[index][1]+WL1[i*2+1]
                candidateCareerPaths[index][0]=cost + candidateCareerPaths[index][1]
                candidateCareerPaths[index].append(WL1[i*2])
            else: #append to newly duplicated path(s)
                index2 = len(candidateCareerPaths) - i
                candidateCareerPaths[index2][1]=candidateCareerPaths[index2][1]+WL1[i*2+1]
                candidateCareerPaths[index2][0]=cost + candidateCareerPaths[index2][1]
                candidateCareerPaths[index2].append(WL1[i*2])


        currentCost = 2000
        newNodeFound = False
        for i in range(len(candidateCareerPaths)):
            if currentCost>candidateCareerPaths[i][0] and (candidateCareerPaths[i][len(candidateCareerPaths[i])-1] == careerEndPoint or candidateCareerPaths[i][len(candidateCareerPaths[i])-1] in universalCareerGraph):
                currentCost = candidateCareerPaths[i][0]
                nextNode = candidateCareerPaths[i][len(candidateCareerPaths[i])-1]
                index = i
                newNodeFound = True

        currentNode = nextNode
        #print('*******************************')
        #print('Current Cost:',currentCost)
        #for ccp in candidateCareerPaths:
        #    print(ccp)
        #print('*******************************')

    if newNodeFound:
        print("Shortest Career Path Found is", candidateCareerPaths[index][0], "Months")
    else:
        print("Sorry, path not found")

    careerpath =[]

    for i in range(len(candidateCareerPaths[index])-2):
        print(candidateCareerPaths[index][i+2])
        careerpath.append(candidateCareerPaths[index][i+2])

    return (candidateCareerPaths[index][0], careerpath)
