# Q19. Grade Calculator
marks=int(input("Enter Your Marks:"))
print("A" if marks>=90 else "B" if marks>=80 else "C" if marks>=70 else "D" if marks>=60 else "F")

# Q20. Temperature Category
temperature=int(input("Enter Your Temperature:"))
print("Very Hot" if temperature>=40 else "Hot" if temperature>=30 else "Warm" if temperature>=20 else "Cold")

# Q21. Traffic Signal
color=input("Enter Your Color Name :")
print("Stop" if color=="red" else "Wait" if color=="yellow" else "Go" if color=="green" else "Invalid Signal")

# Q22. Electricity Usage Category
units=int(input("Enter Your Unit:"))
print("Low Usage" if 0<=units<101 else "Medium Usage" if 101<=units<301 else "High Usage" if 300<units<501 else "Very High Usage")

# Q23. Movie Ticket Category
age=int(input("Enter Your Age:"))
print("Free Ticket" if 0<age<5 else "Child Ticket" if age<13 else "Regular Ticket" if age<60 else "Senior Ticket")

# Q24. BMI Category
bmi=float(input("Enter Your BMI:"))
print("Underweight" if bmi<18.5 else "Normal" if bmi<25 else "Overweight" if bmi<30 else "Obese")

# Q25. Month Days






# Q26. Simple Calculator
num_1=int(input("Enter First Number:"))
num_2=int(input("Enter Two Number:"))
operator=input("Enter Your Operator(+,-,*,/,%):")
print(num_1+num_2 if operator=="+" else num_1-num_2 if operator=="-" else num_1*num_2 if operator=="*" else num_1/num_2 if operator=="/" else "Invalid Operator")

# Q27. Day Number
number=int(input("Enter Your Day Number:"))
match number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday") 
    case 7:
        print("Sunday")  
    case _:
        print("Invalid Day") 

# Q28. Performance Level
score=int(input("Enter Your Score:")) 
print("Excellent" if score>=90 else "Very Good" if score>74 else "Good" if score>59 else "Average" if score>39 else "Needs Improvent") 

