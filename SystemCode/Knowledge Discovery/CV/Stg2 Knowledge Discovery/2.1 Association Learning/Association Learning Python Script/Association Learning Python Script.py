from efficient_apriori import apriori
import csv
import re

dataset=[]
with open('List of Principal Software Engineer CVs after transpose.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    for row in csv_reader:
      row = [x for x in row if x]
      dataset.append(row)
  
itemsets, rules = apriori(dataset, min_support=0.15, min_confidence=0.5)
rules_rhs = filter(lambda rule: len(rule.lhs) == 1 and len(rule.rhs) == 1 and rule.lift == 1, rules)

with open('Itemsets to be removed.csv', 'w', newline='') as csvFile:
  writer = csv.writer(csvFile)
  
  for rule in rules_rhs:
    strRules = str([rule])
    print(rule)
    strRules = re.split(' -> |{|}|\[|\]',strRules)
    strRules = [x for x in strRules if x]
    writer.writerow(strRules)
  csvFile.close()