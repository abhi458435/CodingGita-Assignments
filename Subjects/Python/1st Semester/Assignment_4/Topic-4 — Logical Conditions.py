# # Q29. College Admission Eligibility
# marks=int(input("Enter Your Marks:"))
# attendance=int(input("Enter Your Marks:"))
# if marks>=60:
#     if attendance>=75:
#         print("Eligible")
#     else:
#         print("Not Eligible")
# else:
#     print("Not Eligible")

# # Q30. Scholarship Eligibility
marks=int(input("Enter Your Marks: "))
family_income=int(input("Enter Your Family Income:"))
if marks>=85 or family_income<=300000:
        print("Scholarship Available")
else:
        print("No Scholarship")


# # Q31. Weekend Check
# weekday=input("Take a Day Name:")
# match weekday:
#     case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
#         print("Weekday")
#     case "Saturday"| "Sunday":
#         print("Weekend")   
#     case _:
#         print("Invalid Day Name")

# # Q32. Online Exam Access
# username=input("Enter your username:")
# password=input("Enter your valid password:")
# if username=="student":
#     if password=="python123":
#         print("Access Granted")
#     else:
#         print("Access Denied")
# else:
#     print("Access Denied")

# # Q33. Delivery Availability
# delivery_available=input("Enter Your Current City:")
# match delivery_available:
#     case "Ahmedabad"|"Gandhinagar":
#         print("Delivery Available")
#     case _:
#         print("Delivery Unavailable") 

# # Q34. Number Range Check
# number=int(input("Enter Your Number:")) 
# print("Inside Range" if 10<= number<=50 else "Outside Range")  

# # Q35. Secure Transaction
# amount=int(input("Enter Your Amount:"))
# otp=(input("Enter The OTP:"))
# print(("Transaction Approved" if otp=="1234" else "Transaction Declined")if amount<=50000 else "Transaction Declined")