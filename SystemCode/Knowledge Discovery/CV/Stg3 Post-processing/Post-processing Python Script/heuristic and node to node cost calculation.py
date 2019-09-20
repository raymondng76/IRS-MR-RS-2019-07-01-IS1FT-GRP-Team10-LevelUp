import csv
import itertools
import math

listToDict = {}
jobsPair = []
timePair = []
newjobsPair = []
newtimePair = []
combinePair = []

########for heuristic table
csvtoDict = {}
heuristicDict = {}
listTable = []
combineValue = 0
count = 0

CurrentPairKey = ""
NextPairKey = ""
CurrentPairValue = ""
MainJobTitle = ""
index = 0
counter=0
start = True

########neighbour table
with open('7 Knowledge Discovery after post-processing - Used in Step 8.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
   
    for row in csv_reader:
        jobsPair.append(row['title'])
        timePair.append(row['month'])
    MainJobTitle = jobsPair[0]
    
    #create pair-wise list for newjobsPair, newtimePair and combinePair
    for row in range(len(jobsPair)):
        if start == True:
            index += 1
            if counter == 1:
                CurrentPairKey = CurrentPairKey + "," + jobsPair[len(jobsPair)-index]
                NextPairKey = jobsPair[len(jobsPair)-index]
                combinePair.append(CurrentPairKey + ":" + CurrentPairValue)
                CurrentPairValue = timePair[len(timePair)-index]
                start = False
                counter = 0
                newjobsPair.append(CurrentPairKey)
                newtimePair.append(CurrentPairValue)
            elif counter == 0:
                CurrentPairKey = jobsPair[len(jobsPair)-index]
                CurrentPairValue = timePair[len(timePair)-index]
                newtimePair.append(CurrentPairValue)
                counter += 1
        else:
            index += 1
            CurrentPairKey = NextPairKey + "," + jobsPair[len(jobsPair)-index]
            NextPairKey = jobsPair[len(jobsPair)-index]
            combinePair.append(CurrentPairKey + ":" + CurrentPairValue)
            CurrentPairValue = timePair[len(timePair)-index]
            newjobsPair.append(CurrentPairKey)
            if index != len(jobsPair):
                newtimePair.append(CurrentPairValue)        
    combinePair.sort()
    
    for row in range(len(combinePair)):
        listToDict[row] = combinePair[row]
    
    for row in range(len(listToDict)):
        if listToDict[row][0:len(MainJobTitle)] == MainJobTitle:
            del listToDict[row]
    
    reorderDict = {}
    index=0
    for row in listToDict:
        reorderDict[index] = listToDict[row]
        index +=1
    
    ########adjacent nodes table
    count = 0
    neighbourDict={}
    start = True
    for row in range(len(reorderDict)):
        if start == True:
            searchKey = reorderDict[row][0:reorderDict[row].find(":")]
            searchValue = int(reorderDict[row][reorderDict[row].find(":")+1:])
            start = False
            count += 1
        else:
            nextsearchKey = reorderDict[row][0:reorderDict[row].find(":")]
            nextsearchValue = int(reorderDict[row][reorderDict[row].find(":")+1:])
            
            if nextsearchKey != searchKey:
                average = searchValue / count
                neighbourDict[searchKey] = average
                count = 1
                searchKey = nextsearchKey
                searchValue = nextsearchValue
            else:
                count += 1
                searchValue = searchValue + nextsearchValue
            if row == len(reorderDict)-1:
                average = searchValue / count
                neighbourDict[searchKey] = average
    
    #####generate node to node cost csv
    with open(MainJobTitle + '_neighbour.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Title A', 'Title B','Average'])
        for key, value in neighbourDict.items():
           writer.writerow([key[0:key.find(",")],key[key.find(",")+1:],math.ceil(value)])
    csv_file.close()
    
#########heuristic table
with open('7 Knowledge Discovery after post-processing - Used in Step 8.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    start = True
    count = 0
    for row in enumerate(csv_reader):
        key, value = row
        csvtoDict[key] = value
    
    for row in range(len(csvtoDict)):
        if start == True:
            searchKey = csvtoDict[row]['title']
            
            searchValue = 0
            combineValue = 0
            start = False
        else:
            nextsearchKey = csvtoDict[row]['title']
            nextsearchValue = int(csvtoDict[row]['month'])
            
            if nextsearchKey != searchKey:
                searchValue = searchValue + nextsearchValue
            else:
                listTable.append(searchValue)
                combineValue = combineValue + searchValue
                count += 1
                searchValue = 0
            if row == len(csvtoDict)-1:
                listTable.append(searchValue)
                combineValue = combineValue + searchValue
                count +=1
                searchValue = 0
    averageValue = combineValue / count
    heuristicDict['title','average','min'] = searchKey, averageValue, min(listTable)
    
    #####generate heuristic cost csv
    with open(MainJobTitle + '_heuristic.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Title','Average','Min'])
        writer.writerow([searchKey,math.ceil(averageValue),math.ceil(min(listTable))])
    csv_file.close()