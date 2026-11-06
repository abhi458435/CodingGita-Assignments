#Q1. Solid Square
# r=int(input("Enter Your row Number:"))
# c=int(input("Enter your col number:"))
# for i in range(1,r+1):
#     for j in range(1,c+1):
#         print("*",end="")
#     print()

# #Q2. Solid Rectangle
# rows=3
# col=6
# for i in range(1,rows+1):
#     for j in range(1,col+1):
#         print("*",end=" ")
#     print()

#Q3. Increasing Star Triangle
# row=5
# col=5
# for i in range(1,row+1):
#     for j in range(i):
#         print("*",end="")
#     print()

#Q4. Increasing Number Triangle
# row=5
# for i in range(1,row+1):
#     for j in range(i):
#         print(j+1,end="")
#     print()

#Q5. Repeated Number Triangle
# row=5
# col=5
# for i in range(1,row+1):
#     for j in range(i):
#         print(i,end="")
#     print()

#Q6. Repeated Alphabet Triangle
# row=5
# for i in range(1,row+1):
#     for j in range(i):
#         print(chr(64+i),end="")
#     print()

#Q7. Alphabet Triangle
# row=5
# col=5
# for i in range(1,row+1):
#     for j in range(i):
#         print(chr(65+j),end="")
#     print()

#Q8. Continuous Number Triangle
# row=5
# n=1
# for i in range(1,row+1):
#     for j in range(i):
#         print(n,end=" ")
#         n+=1
#     print()

#Q9. Alternating 0–1 Triangle
# row=5
# for i in range(1,row+1):
#     for j in range(i):
#        print((i+j)%2,end=" ")
#     print()

#Q10. Decreasing Star Triangle
# row=5
# col=5
# for i in range(row,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

#Q11. Decreasing Number Triangle
# row=5
# col=5
# for i in range(row,0,-1):
#     for j in range(i):
#         print(j+1,end="")
#     print()

#Q12. Decreasing Alphabet Triangle
# row=5
# for i in range(row,0,-1):
#     for j in range(i):
#         print(chr(65+j),end="")
#     print()