# Q7. Sum of Numbers in a Range
start=int(input("Enter your starting Number:"))
end=int(input("Enter Your End Number:"))
add=0
for i in range(start,end+1):
    add=add+i
print(add)

# Q8. Count Multiples of 3
N=int(input("Enter Your Number:"))
count=0
for i in range(1,N+1):
    if i%3==0:
        count=count+1
print(count)

# Q9. Sum of Multiples of 4
N=int(input("Enter Your Number:"))
sum=0
for i in range(1,N+1):
    if i%4==0:
        sum=sum+i
print(sum)    

# Q10. Count Numbers with Two Conditions
N=int(input("Enter Your Number:"))
count=0
for i in range(1,N+1):
     if i%3==0 and i%5==0:
         count=count+1
print(count)

# Q11. Sum Numbers Except Multiples of 3
N=int(input("Enter Your Number:"))
sum=0
for i in range(1,N+1):
    if i%3!=0:
        sum=sum+i
print(sum)

# Q12.Count Even and Odd Together
N = int(input("Enter Your Number:"))
even_count = 0
odd_count = 0
for i in range(1, N + 1):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Even={even_count}")
print(f"Odd={odd_count}")

# Q13. Running Sum
N = int(input("Enter Your Number:"))
sum=0
for i in range(1, N + 1):
    sum=sum+i
    print(sum)

# Q14. Running Product
N = int(input("Enter Your Number:"))
multiply=1
for i in range(1, N + 1):
    multiply=multiply*i
    print(multiply)

