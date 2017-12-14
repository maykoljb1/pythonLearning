studentsCount = int(input("Enter the number of students: "))
n = 0
studentsGrades = [[]]
while n < studentsCount:    
    studentsGrades.append([]);
    for i in range(3):        
        grade = int(input("Please enter (" + str(i + 1) + ")grade: "))
        studentsGrades[n].append(grade)
    n = n + 1    

n = 0
approvedStudents = 0
while n < studentsCount:        
    gradesSum = 0
    for i in range(3):        
        gradesSum = studentsGrades[n][i] + gradesSum
    avg = gradesSum / 3

    print("Student #" + str(n) + ": Average: " + str(avg)) 
    if(avg  >= 70):
        approvedStudents = approvedStudents + 1
    n = n + 1
    

print("the number of approved students is: " + str(approvedStudents))

    
    
