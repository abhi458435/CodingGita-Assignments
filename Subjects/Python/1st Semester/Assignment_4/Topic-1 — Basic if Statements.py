# Q1. Positive Number
integer=int(input("Enter Your Integr:"))
print("Positive Number" if integer>0 else "No output")

#Q2.Voting Eligibility Check
age=int(input("Enter your Age:"))
print("Eligible to Vote" if age>=18 else "No output")

#Q3. Temperature Warning
temp=int(input("Temperature:"))
print("High Temperature" if temp>40 else "No output")

# Q4. Divisible by 5
integer=int(input("Integer:"))
print("Divisible by 5" if integer%5==0 else "No output")
# Q5. Free Delivery
amount=int(input("Enter Your Delivery Amount:"))
print("Free Delivery" if amount>=1000 else "No Output")
# Q6. Character Check
character=input("Character:")
print("You entered A" if character=="A" else "No output")

# Q7.Password Length Check
password=input("Enter Your Password:")
print("Strong Length" if len(password)>=8 else "No Output")
# Q8. Number of Digits
integer=int(input("Enter your number:"))
print("Three Digit Number" if 99<integer<1000 else "No output")