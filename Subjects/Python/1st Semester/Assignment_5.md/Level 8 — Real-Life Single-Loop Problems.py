
# 62
n=int(input("enter your no.:"))
total=0
highest=0
lowest=9
for i in range(n):
    expense=int(input("Enter your expenses:"))
    total=total+expense
    if i==0:
        highest=expense
        lowest=expense
    else:
        if expense>highest:
            highest=expense
            
        if expense<lowest:
            lowest=expense
            
print("Total expense:", total)
print("Highest expense:",highest)
print("Lowest expense:",lowest)
        
        
63
n=int(input("enter your no.:"))
total=0
for i in range(n):
    marks=int(input("Enter your marks:"))
    total=total+marks
    if i==0:
        highest=marks
        lowest=marks
    else:
        if marks>highest:
            highest=marks
            
        if marks<lowest:
            lowest=marks
print("total",total)
average=total/n
print("average:",average)
print("highest:",highest)
print("Lowest:",lowest)   

64

n=int(input("enter no.:"))
present=0
absent=0
for i in range(n):
    att=input("Enter A or P:")
    if att=="P":
        present=present+1
    else:
        absent=absent+1
        
print(present)
print(absent)
print("Present:",present)
print("Absent:",absent)
print("Attandance:",(present/(present+absent)*100))       
        

65

n=int(input("enter no.:"))
total=0
count=0
for i in range(n):
    units=int(input("enter units:"))
    total=total+units
    if units>10:
        count=count+1
print("TOtal units:",total)
print("Days before 10:",count)


66

n=int(input("enter no.:"))
total=0
count=0
for i in range(n):
    prices=int(input("enter units:"))
    total=total+prices
    if prices>1000:
        count=count+1
print("TOtal Bill:",total)
print("prices above 1000:",count)

67

n=int(input("enter no.:"))
success=0
failed=0
count=0
for i in range(n):
    attempts=input("enter attempts:")
    if attempts=="success":
        success=success+1
    else:
        failed=failed+1
print("Successful:",success)
print("Failed:",failed)
print("Success Rate:",success/(success+failed)*100)
    
