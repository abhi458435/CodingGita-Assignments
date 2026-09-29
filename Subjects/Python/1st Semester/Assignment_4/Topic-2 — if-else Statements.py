# Q9. Even or Odd
integer=int(input("Enter Your Integers:"))
print("Even" if integer%2==0 else "Odd")
# Q10. Pass or Fail
marks=int(input("Enter Your Marks:"))
print("Pass" if marks>=40 else "Fail")
# Q11. Adult or Minor
age=int(input("Age:"))
print("Adult" if age>=18 else "Minor")
# Q12. Number Sign
number=int(input('Enter Your Number:'))
print("Positve" if number>0 else "Non-Positive")

# Q13. Divisible by 3
integer=int(input("Enter Your Number:"))
print("Divisible by 3" if integer%3==0 else "Not Divisible by 3")

# Q.14.  Login Password
correct_password = input("Enter Your Password:")
print("Login Successful" if correct_password=="python123" else "Invalid Password")

# Q15. Username Check
username=input("Enter Your Username:")
print("Welcome Admin" if username=="admin" else "Invalid Username")
# Q16. Greater Between Two Numbers
int1=int(input("Enter Your Integer 1:"))
int2=int(input("Enter Your Integer 2:"))
print(int1 if int1>int2 else int2 if int2>int1 else "Both are Equal")

# Q17. Hot or Comfortable
temperature=int(input("Enter Your Curernt Temperature:"))
print("Hot" if temperature>30 else "Comfortable")

# Q18. Shopping Discount Eligibility
amount=int(input("Enter Your Amount:"))
print("Discount Available" if amount>=5000 else "No Discount")

