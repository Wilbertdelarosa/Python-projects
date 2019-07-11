#average falling grades
#Given: A list of grades and a failing grade threshold

#Get data
def getData():
    numGrades = int(input("Enter number of grades: "))
    gradeList = []
    for i in range(numGrades):
        grade = int(input("Enter grade: "))
        gradeList.append(grade)
    
    return gradeList

# Compute avetage of failing Grades
def computeAverageFailing(gradeList, failThreshold):
    totalFailing = 0
    countFailing = 0
    for i in range(len(gradeList)):
        if gradeList[i] < failThreshold:
            totalFailing = totalFailing + gradeList[i]
            countFailing = countFailing + 1
 
    if countFailing > 0:
        averageFailing = totalFailing/countFailing
        return averageFailing
    else:
        return -1
        
# Print result
def printResult(failAverage):
    if failAverage == -1:
        print("congrats No failing grades")
    else:
        print("Average of failing grades", failAverage)
        

#Main funtion
def main():
    gList = getData()
    threshold = int(input("Enter failing grade threshold: "))
    fAvg = computeAverageFailing(gList, threshold)
    printResult(fAvg)
