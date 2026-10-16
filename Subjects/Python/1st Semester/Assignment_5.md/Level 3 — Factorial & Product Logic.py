#Q15. Factorial of a Number
# product=1
# N=int(input("Enter Your Number:"))
# for i in range(1,N+1):
#     product=product*i
# print(product)    
    
# Q16. Factorial of a Number
# product=1
# N=int(input("Enter Your Number:"))
# for i in range(1,N+1):
#     product=product*i
#     print(f"{i}!={product}")

#*Q17. Product of Even Numbers6
# N=int(input("Enter Your Number:"))
# product=1
# for i in range(2,N+1,2):
#      product=product*i
# print(product)    

# Q18. Product of Odd Numbers
# product=1
# N=int(input("Enter Your Number:"))
# for i in range(1,N+1,2):
#     product=product*i
# print(product)

# Q19. Double Factorial — Even Numbers
# N=int(input("Enter The Number:"))
# product=1
# for i in range(N,0,-2):
#     product=product*i
# print(product)

#Q20. Sum of Squares
# N=int(input("Enter The Number:"))
# sum=0
# for i in range(1,N+1):
#     sum=sum+i**2
# print(sum)

#Q21. Sum of Cubes
# N=int(input("Enter The Number:"))
# sum=0
# for i in range(1,N+1):
#     sum=sum+i**3
# print(sum)

#Q22. Factorial-Based Sum
N=int(input("Enter The Number:"))
sum=0
product=1
for i in range(N,0,-1):
    sum=sum+i*product
print(sum)
