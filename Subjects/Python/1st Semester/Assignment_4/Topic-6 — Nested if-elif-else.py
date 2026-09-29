# Q44. Greatest of Three Numbers
num_1=int(input("Enter Your First Number:"))
num_2=int(input("Enter Your Second Number:"))
num_3=int(input("Enter Your Third Number:"))
if num_1>=num_2:
    if num_1>num_2:
        print("A is Greatest")
    else:
        print("A and B are Equal and Greatest")
elif num_2>=num_3:
    if num_2>num_3:
        print("B is Greatest")
    else:
        print("B and C are Equal and Greatest")
elif num_3>=num_1:
    if num_3>num_1:
        print("C is Greatest")
    else:
        print("A and C are Equal and Greatest")
else:
    print("All are Equal")

#  Q45. Student Result with Grade
attendance=int(input("Enter Your Attendance in %:"))
marks=int(input("Enter Your Marks:"))
print(("A" if marks>=90 else "B" if 75<=marks else "C" if 60<= marks else "D" if 40<=marks else "F")if attendance>=75 else "Not Eligible")

# Q46. Employee Bonus
salary=int(input("Enter Your Salary Amount:"))
rating=int(input("Enter Ratings:"))
print(("Bonus:20%" if rating==5 else "Bonus:15%" if rating==4 else "Bonus:10%" if rating==3 else "Bonus: 5%") if salary>=30000 else "Not Eligible for Bonus")

# Q47. Bus Ticket Category
age=int(input("Enter Your Age:"))
distance=int(input("Enter Your Distance:"))
print("Senior"if age>=60 else ("Long Distance" if distance>=10 else "Short Distance") if 5<=age else "Free Ticket")

# Q48. Product Purchase Validation
stock=int(input("Enter Your Stock:"))
payment_status=input("Check Payment Status:")
print( ("Order Confirmed" if payment_status=="paid" else "Payment Pending" if payment_status=="pending" else "Invalid Payment Status")if stock>0 else "Out of Stock")

# Q49. Travel Ticket Validation
age=int(input("Enter Your Age:"))
ticket_type=(input("Enter Your Ticket Type:"))
print("Senior Passenger" if age>=60 else ("AC Ticket" if ticket_type=="Ac" else " Sleeper Ticket" if ticket_type=="Sleeper" else " Invalid Ticket Type") if 5<=age else "Free Travel")