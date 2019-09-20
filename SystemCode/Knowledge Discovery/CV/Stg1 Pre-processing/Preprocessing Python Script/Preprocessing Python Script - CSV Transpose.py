import csv

jobList=[]
mainJobTitle=""
jobGroupList=[]
start=True

with open('List of Principal Software Engineer CVs before transpose.csv', mode='r') as csv_file:
    with open('List of Principal Software Engineer CVs after transpose.csv', 'w', newline='') as csvFile:
        csv_reader = csv.DictReader(csv_file)
        writer = csv.writer(csvFile)
        
        for row in csv_reader:
            jobList.append(row['title'])
            mainJobTitle = jobList[0]
        
        #create group job list
        for index in range(len(jobList)):
            NextKey = jobList[len(jobList)-index-1]
            jobGroupList.append(NextKey)
            
            if NextKey == mainJobTitle:
                writer.writerow(jobGroupList)
                jobGroupList = []
            if index == (len(jobList)):
                writer.writerow(jobGroupList)
                jobGroupList = []
        csvFile.close()
    csv_file.close()