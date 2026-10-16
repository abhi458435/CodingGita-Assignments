import math
#Q53. Second Largest Digit
# num=int(input("Enter Your Number:"))
# max=0
# second_largest=max
# for i in range(int(math.log10(num))+1):
#     number=num%10
#     if number>max:
#         second_largest=max
#         max=number
#     elif second_largest<number:
#         second_largest=number
#     num=num//10
# print(second_largest)

#Q54. Longest Consecutive Equal Character Run
# string=input("Enter Your String:")
# current_count=1
# best_count=1
# for i in range(1,len(string)):
#     if string[i]==string[i-1]:
#         current_count+=1
#     else:
#         current_count=1
#     if current_count>best_count:
#         best_count=current_count
# print("Longest Consecutive run:",best_count)

#Most Frequent Character — Controlled Approach
# str4=input("Enter Your String:")
# target_character=input("Enter Your Target Character:")
# count=0
# for i in str4:
#     if i in target_character:
#         count+=1
# print("Count:",count)
# print("Frequenc?y:",count*100/len(str4),"%")  

#Q56. Running Digit Sum Until the End
# num=int(input("Enter Your Number:"))
# sum=0
# for i in range(int(math.log10(num))+1):
#     x=num%10
#     sum=sum+x
#     num=num//10
#     print(sum)

#Q57. Number with Most Even Digits
# num=input("Enter Your Number:")
# even=0
# odd=0
# for i in num:
#     if int(i)%2==0:
#         even=even+1
#     else:
#         odd=odd+1
# if even>odd:
#     print("More Even Digits")
# elif odd>even:
#     print("More Odd Digits") 
# else:
    # print("Equal")   

#Q58. Alternating Digit Sum 
#  # 58

# n = int(input("Enter a number: "))
# result = 0

# for i in range(len(str(n))):
#     digit = n % 10

#     if i % 2 == 0:
#         result = result + digit
#     else:
#         result = result - digit

#     n = n // 10

# # print(result)


#Q59. Output Prediction — Accumulator Trap

# 2
# 6
# 12
# 20
# 30
  
#Q60. Output Prediction — Condition Inside Loop
 
# 5

#Q61. Debug the Accumulator

# # sum = 0
# # for i in range(1, 6):
# #     sum = sum+i
# # print(sum)
