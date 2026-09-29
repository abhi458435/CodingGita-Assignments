# Q36. Login with Role
username=input("Enter Your Username:")
pasword=input("Enter Your Password:")
print(("Login Successful" if pasword=="admin123" else "Wrong Password")if username=="admin" else "Invalid Username")

# Q37. Driving License Eligibility
age=int(input("Enter Your Age:"))
test_status=input("Enter Pass or Fail:")
print(("License Approved" if test_status=="Pass" else "Test Not Passed")if age>=18 else "Age Not Eligible")

# Q38. ATM Withdrawal
account=int(input("Enter Your Account Balance:"))
withdrawal=int(input("Enter Your Withdrawal Amount:"))
if account>=withdrawal:
    if withdrawal%100==0:
        print("Withdrawal Successful")
    else:
        print("Enter Amount in Multiples of 100")
else:
    print("Insufficient Balance")

# Q39. Exam Result with Attendance
marks=int(input("Enter Your Marks:"))
attendance=int(input("Enter Your Attendance:"))
print(("Pass" if marks>=40 else "Fail")if attendance>=75 else "Not Eligible Due to Attendance")

# Q40. Bank Account Verification
type=input("Enter Your Account Type:")
balance=int(input("Enter Your Balance:"))
print(("Minimum Balance Maintained" if balance>=1000 else "Minimum Balance Not Maintained")if type=="Savings" else "Unsupported Account")

# Q41. Online Shopping Eligibility
order_amount=int(input("Enter Your Order Amount:"))
payment_method=input("Card,UPI:")
print(("Card Payment Accepted" if payment_method=="card" else "UPI Payment Accepted" if payment_method=="upi" else "Unsupported Payment Method")if order_amount>=500 else "Minimum Order Amount Not Reached")

# Q42. Hostel Room Allocation
year=int(input("Enter The Year :"))
attendance=int(input("Enter Your Attendance in Percentage:"))
if 1<year<5:
    if attendance>=75:
        print("Room Eligible")
    else:
        print("Attendance Too Low")
else:
    print("Not Eligible by Year")

# Q43. Internet Plan Upgrade
plan=input("Enter The Plan Type:")
uses=int(input("Enter The Uses:"))
print(("Recommend Upgrade" if uses>100 else "Basic Plan Is Sufficient")if plan=="basic" else "Already on Higher Plan")


