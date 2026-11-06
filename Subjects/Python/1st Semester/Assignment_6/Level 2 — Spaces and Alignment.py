#Q13. Right-Aligned Half Pyramid
# row=5
# col=5
# for i in range(1,row+1):
#     for j in range(col-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end="")
#     print()

# #Q14. Inverted Right-Aligned Half Pyramid
# n=5
# for i in range(n,-1,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end="")
#     print()

#Q15. Star Pyramid
# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end="")
#     print()

# Q16. Inverted Star Pyramid
# n=5
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end="")
#     print()

#Q17. Solid Diamond
# n=20
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end="")
#     print()
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end="")
#     print()

#Q18. Rhombus
# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(2*n-1):
#         print("*",end="")
#     print()

### Q19. Mirrored Number Pattern
# n = 5
# for i in range(1, n + 1):

#     # Left side
#     for j in range(1, i + 1):
#         print(j, end="")

#     # Spaces
#     for k in range(2 * (n - i)):
#         print(" ", end="")

#     # Right side
#     for j in range(i, 0, -1):
#         print(j, end="")

#     print()

print("Hello World")
