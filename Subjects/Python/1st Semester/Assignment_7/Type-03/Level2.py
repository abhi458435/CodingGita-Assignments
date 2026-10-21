#Q46. Find the First and Last Digit
# n=704
# last_digit=n%10
# first_digit=n
# while first_digit>10:
#     first_digit=first_digit//10

# print(first_digit)    
# print(last_digit)
    
#Q47. Count Even Digits
# n=583204
# even=0
# while n>0:
#     x=n%10
#     n=n//10
#     if x%2==0:
#         even+=1 
# print(even)

#Q48. Count Odd Digits
# n=583204
# odd=0
# while n>0:
#     x=n%10
#     n=n//10
#     if x%2!=0:
#         odd+=1 
# print(odd)

#Q49. Find the Sum of Even Digits
# n=135792
# even=0
# sum=0
# p=0
# while n>0:
#     x=n%10
#     n=n//10
#     if x%2==0:
#         p=x
#         sum=sum+p
# print(sum)

#Q50. Find the Largest Digit
# n=1947
# max=0
# while n>0:
#     x=n%10
#     n=n//10
#     if x>max:
#      max=x
# print(max)

#Q51. Find the Smallest Digit
# n=147
# min=9
# while n>0:
#     x=n%10
#     n=n//10
#     if min>x:
#         min=x
# print(min)

#Q52. Check Whether a Number Is a Palindrome
# n=1221
# original=n
# reverse=0
# while n>0:
#     x=n%10
#     n=n//10
#     reverse=reverse*10+x
# if reverse==original:
#     print("Palindrome")
# else:
#     print("Not palindrome")
 

#Q53. Count How Many Times a Digit Appears
# n=7007
# d=7
# count=0
# while n>0:
#     x=n%10
#     n=n//10
#     if x==d:
#         count+=1
# print(count)

#Q54. Check Whether All Digits Are the Same
# n=7777
# while n>0:
#     x=n%10
#     n=n//10


#Q55. Compare the Sum of First and Last Digits with the Middle Digits'

# i = 1

# while i <= 3:
#     j = 1

#     while j <= 2:
#         print(j, end=" ")
#         j += 1

#     print()
#     i += 1

