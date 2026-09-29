#Q58. Student ID Validation
# student_id=input("Enter Your ID Details:").split("-")
# degree,batch,branch,roll_number=student_id
# print("CSE Student" if branch=="CSE" else "Non-CSE Student")

#Q59. Email Domain Checker
# email=input("Enter Your Email Address:").split("@")
# codomain,domain=email
# print("Gmail User" if domain=="gmail.com" else "Other Email Provider")

#Q60. Username Generator Validation
# full_name=input("Enter The Full Name:")
# first_name,middle_name,last_name=full_name
# print("Valid Username Format" if )

#Q61. Number Digit Analyzer
# integer=int(input("Enter Your Number:"))
# print("One Digit" if 0<integer<10 else "Two Digits" if 9<integer<100 else "Three Digits" if 99<integer<1000 else "Four or More Digits")

#Q62. Shopping Bill Category
# product_price=int(input("Enter Your Product Price:"))
# quantity=int(input("Enter Your Product Quantity:"))
# subtotal=product_price*quantity
# discount
# final=subtotal-discount

#Q63. Electricity Bill Category
# unit=int(input("Enter Your Consumed Units:"))
# rate=int(input("Enter Your Per Unit Rate:"))
# bill=unit*rate
# if unit>300:
#     # if rate==10:
#         print("Bill:",bill)
# elif 100<unit:
#     # if rate==7:
#         print("Bill:",bill)
# else:
#     # if rate==5:
#         print("Bill:",bill)        

#Q64. ATM Menu
# initial_balance=10000
# withdrawal_amount=int(input("Enter Your Withdrwal Amount:"))
# menu=int(input("Enter Input to get Display Menu:"))
# deposit=int(input("Enter Your Deposit Amount:"))
# balance=initial_balance
# match menu:
#     case 1:
#         print("Check Balance",initial_balance)
#     case 2:
#         print()   
# 
# Q65. Restaurant Ordering System
# i

#Q66. Exam Result Analyzer
# sub1_marks=int(input("Enter Your Subject 1 Marks:"))
# sub2_marks=int(input("Enter Your Subject 2 Marks:"))
# sub3_marks=int(input("Enter Your Subject 3 Marks:"))
# attendance=int(input("Enter Your Attendance in %:"))
# total=sub1_marks+sub2_marks+sub3_marks
# average=total//3
# if attendance>=75:
#     if average>=90:
#         print("Outstanding")
#     elif 74<average:
#         print("Very Good")
#     elif 59<average:
#         print("Good")
#     elif 39<average:
#         print("Pass")
#     else:
#         print("Fail")
# else:
    # print("Not Eligible")

#Q67. Cab Fare Calculator
# distance=int(input("Enter Your Distance in Km:"))
# ride_type=input("Enter Your Ride Type:")
# normal_ride=15 
# premium_ride=25
# fare1=distance*normal_ride
# fare2=distance*premium_ride

# match ride_type:
#     case "normal":
#         if distance>=20:
#             print("Fare:",fare1+fare1/10)
#         else:
#             print("Fare",fare1)
            
#     case "premium":
#         if distance>=20:
#             print("Fare:",fare2+fare2/10)
#         else:
#             print("Fare:",fare2)

#Q68. College Admission System
# entrance_score=int(input("Enter Your Entrance Score:"))
# percentage_in_12th=int(input("Enter Your Percentage in 12th:"))
# category=input("Enter Your Category:")
# match category:
#     case "general":
#         if entrance_score>=80 and percentage_in_12th>=75:
#             print("Admission Eligible")
#         else:
#             print("Admission Not Eligible")
#     case "obc":
#         if entrance_score>=70 and percentage_in_12th>=70:
#             print("Admission Eligible") 
#         else:
#             print("Admission Not Eligible") 
#     case "sc":
#         if entrance_score>=60 and percentage_in_12th>=60:
#             print("Admission Eligible")
#         else:
#             print("Admission Not Eligible")
# 
              