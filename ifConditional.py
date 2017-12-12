print("*******************************************************");
print("**********************If Conditional*******************");
print("*******************************************************");
num1=int(input("Enter the first value: "))
num2=int(input("Enter the second value: "))
print("The biggest value is")
if num1 > num2:
    print(num1)
else:
    print(num2)

print("*******************************************************");
print("**********************Grades Average*******************");
print("*******************************************************");
grade1 = int(input("Enter first grade"));
grade2 = int(input("Enter second grade"));
grade3 = int(input("Enter third grade"));
avg = (grade1 + grade2 + grade3) / 3;
if avg >= 7:
    print("Aproved");
else:
    if avg >= 6:        
        if avg <= 5 and grade3 <= 6:
            print("Expelled")
        else:
            print("Disapprove")
    else:
        print("Regular")

        
