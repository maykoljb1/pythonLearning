print("***************************************************************************")
print("                           Is it Christmas?                                ")  
print("***************************************************************************")

print("Please enter the day")
day = int(input());

print("Please enter the month")
month = int(input())

print("Please enter the year")
year = int(input())

if day == 24 and month == 12:
    print("is Christmas!!!!")
else:
    print("it is not Christmas :(")

print("***************************************************************************")
print("                           Are this values 10                              ")  
print("***************************************************************************")

print("Please enter the 1st number")
firstNumber = int(input());

print("Please enter the 2nd number")
secondNumber = int(input())

print("Please enter the 3th number")
thirdNumber = int(input())

if thirdNumber < 10 and secondNumber < 10 and firstNumber < 10:
    print("all numbers are less than 10")
else:    
    if thirdNumber < 10 or secondNumber < 10 or firstNumber < 10:
        print("at leaset 1 number is less than 10")
    else:
        print("none of the numbers were less than 10")

    
        
