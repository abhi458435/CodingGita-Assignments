import math
#Q23. Count Digits Using a Loop
# num=int(input("Enter Your Number:"))
# count=0
# for i in range(int(math.log10(num))+1):
#     count=count+1
# print(count)

# Q24. Sum of Digits
# num=int((input("Enter Your Number:")))
# sum=0
# for i in range(int(math.log10(num))+1):
#     digit=num%10
#     sum=sum+digit
#     num=num//10
    
# print(sum)

#Q25. Product of Digits
# integer = int(input("Enter Your Integer:"))
# product = 1
# if integer == 0:
#     product = 0
# else:
#     for i in range(int(math.log10(integer)) + 1):
#         digit = integer % 10
#         product = product * digit
#         integer = integer // 10
# print(product)

# Q26. Count Even Digits
# num=int(input('Enter your number:'))
# count=0
# for i in range(int(math.log10(num))+1):
#     count=count+1
# print(count)

# Q27. Sum of Even Digits
# num=int((input("Enter Your Number:")))
# sum=0
# for i in range(int(math.log10(num))+1):
#     digit=num%10
#     if digit%2==0:
#      sum=sum+digit
#     num=num//10
# print(sum)

#Q28.Largest Digit Without max()
# num=int(input("Enter Your Number:"))
# max=0
# for i in range(int(math.log10(num))+1):
#     number=num%10
#     if number>max:
#         max=number
#     num=num//10
# print(max)

#Q29. Smallest Digit Without min()
# num=int(input("Enter Your Number:"))
# min=9
# for i in range(int(math.log10(num))+1):
#     number=num%10
#     if number<min:
#         min=number
#     num=num//10
# print(min)

#Q30. Reverse a Number
# num=input("Enter Your Number:")
# reverse=""
# for i in range(len(num)-1,-1,-1):
#     reverse=reverse+num[i]
# print(reverse)

 #Way-02
# num=int(input("Enter Your Number:"))
# reverse=0
# for i in range(int(math.log10(num))+1):
#     reverse=(reverse*10)+num%10
#     num=num//10
# print(reverse) 
   
#Q31. Reverse a Number
# str1=input("Enter Your Number:")
# new_str=""
# for i in range(len(str1)-1,-1,-1):
#     new_str=new_str+str1[i]
# if new_str==str1:
#     print("Palindrone Number")
# else:
#     print("Non-Palindrone Number")
   
#Q32. Count a Specific Digit
# num = int(input("Enter Your Number: "))
# target_Digit = int(input("Enter Your Target Number: "))
# count = 0
# for i in range(int(math.log10(num)) + 1):
#     if num % 10 == target_Digit:
#         count += 1
#     num = num // 10  

# print("Count of target digit:", count)

#Q33. First Digit Using Repeated Division
# num=int(input('Enter the number:'))
# first_digit= 0
# for j in range(int(math.log10(num))+1):
#     first_digit=num%10
#     num=num//10
# print(first_digit)

#Q34.Difference Between Largest and Smallest Digit
# num=int(input('Enter the number:'))
# max= 0
# min=9
# for j in range(int(math.log10(num))+1):
#     x=num%10
#     if x>max:
#         max=x
#     if x<min:
#         min=x
#     num//=10
# print("min",min)
# print("max",max)
# print("Difference:",max-min)

#Q35. Digit Position Value
# num=int(input("Enter Your Number:"))
# store=0
# for i in range(int(math.log10(num))+1):
#     x=num%10
#     num=num//10
#     store=x
#     print(store,i+1)

#Q36. Armstrong Number — 3 Digit
# num=int(input("enter no.="))
# y=abs(num)
# sum=0
# for i in range(int(math.log10(y))+1):
#     digit=num%10
#     sum=sum+digit**3
#     num=num//10
# print(sum)
# if sum==y:
#     print("Armstrong no.")
# else:
#     print("NON-armstrong")


