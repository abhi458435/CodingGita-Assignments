#Q45. Find the Middle Character
# str1=input("Enter Your word:")
# middle=len(str1)//2
# for i in range(len(str1)+1):
#     if i==middle:
#         print(str1[i])

#Q46. First Half and Second Half
# word=input("Enter Your Word:")
# middle=len(word)//2
# print("First Half:",end="")
# for i in range(middle):
#     print(word[i],end="")
# print()
# print("Last Half:",end="")
# for i in range(middle,len(word)):
#     print(word[i],end="")
# print()

#Q47. Split a String by Length — Odd vs Even
# word=input("Enter Your Word:")
# middle=len(word)//2
# if len(word)%2==0:
#     print("First Half:",end="")
#     for i in range(middle):
#         print(word[i],end="")
#     print()
#     print("Second Half:",end="")
#     for i in range(middle,len(word)):
#         print(word[i],end="")
# else:
#     print("First Half:",end="")
#     for i in range(middle):
#         print(word[i],end="")
#     print()
#     print("Middle Character:",end="")
#     for i in range(middle,middle+1):
#         print(word[i],end="")
#     print()
#     print("Second Half:",end="")
#     for i in range(middle+1,len(word)):
#         print(word[i],end="")
#     print()

#Q48. Compare Two Halves
# string=input("Enter Your String:")
# first_half=""
# second_half=""
# for i in range(1,len(string)+1):
#     if i>len(string)//2:
#         first_half=first_half+[i]+""
#     print(first_half)
# else:
#     second_half=second_half+[i]+""
#     print(second_half)



  #Q49. Mirror the String



# #Q50. Alternate Character Extraction
# str1=input("Enter Your Word:")
# for i in range(0,len(str1),2):
#     print(str1[i],end="")

#Q51. Count Characters at Even and Odd Indexes
# str2=input("Enter Your word:")
# even=0
# odd=0
# for i in range(len(str2)):
#  if i%2==0:
#   even=even+1
#  else:
#   odd=odd+1      
# print("Even Index",even)
# print("Odd Index",odd)
     

#Q52. Swap Adjacent Characters
word=input("Enter Your Word:")
reverse=""
for i in word:
    reverse=reverse+i
    if reverse==word:
        print(reverse)
 