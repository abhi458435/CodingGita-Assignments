#Q60. Student Result Information
info=input("Enter Your Information: name,total,average-").split(",")
name,total,average=info
m1=70
m2=80
m3=90
total=m1+m2+m3
average=total/3
print("Name:",name)
print("Total:",total)
print("Average:",average)

# Q61. Student ID Analyzer
id=input("Write about college:").split("-")
degree,batch,branch,roll_number=id
x=int(roll_number)
print("Degree:",degree)
print("Batch:",batch)
print("Branch:",branch)
print("Roll Number:",x)
print(degree[0:4])

# Q62. Username Generator
username=input("Enter Your Full Name:").split()
first_name,middle_name,last_name=username
print(f"{first_name[0:].lower()}.{last_name[0:].lower()}")

# Q63. Sentence Information
sentence=input("Enter Your Sentence:").split()
first,second,third,fourth=sentence
print(f"First word:{first[0:]}")
print(f"Last word:{fourth[0:]}")

# Q64. Email Analyzer + Membership
email=input("Enter Your Email Address:").split("@")
username,domain=email
print("@" is not domain)
print("Username:",username)
print("Domain:",domain)

# Q65. Character Analyzer
character=(input("Enter Your Character:"))
x=character
y=ord(x)
z=y-1
k=chr(z)
l=chr(z+2)



print("Character:",x)
print("Code:",y)
print("Previous:",k)
print("Next:",l)

# Q66. Product Bill
product_name=input("Enter Your Product Name:")
price=int(input("Enter Your Product Price:"))
quantity=int(input("Enter Your Product Quantity:"))
discount_percentage=int(input("Enter Your Discount Percentage:"))
subtotal=price*quantity
discount=subtotal*(discount_percentage/100)
final_amount=subtotal-discount
print("Product:",product_name)
print("Price:",round(price,2))
print("Quantity:",quantity)
print("Subtotal:",round(subtotal,2))
print("Discount:",round(discount,2))
print("Final Total:",round(final_amount,2))

# Q67. Date Analyzer
date=(input("Enter Date:")).split("-")
day,month,year=date
print("Day:",day)
print("Month:",month)
print("Year:",year[0:])

# Q68. String Transformation Challenge
sentence=input("Enter Your Sentence:").split()
first_word,second_word=sentence
print("First Word:",first_word[0:])
print("Second Word:",second_word[0:])
print("First Word Reversed:",first_word[::-1])
print("Second Word Reversed:",second_word[::-1])

# Q69. Final Challenge — Student Code Formatter
details=input("Enter The All Details:").split("-")
degree,batch,branch,roll=details
print("Degree:",degree[0:])
print("Batch:",batch[0:])
print("Branch:",branch)
print("Roll:",roll)
print(f"Code:{degree}/{branch}/{roll}")

# Q70. Final String + Input/Output Challenge
full_name = input("Enter Your Full Name: ")

names = full_name.split()

first_name = names[0]
last_name = names[-1]

first_name_upper = first_name[:3].upper()
last_name_lower = last_name[1:].lower()

reversed_name = full_name[::-1]

print(f"Original: {full_name}")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"First Name (Upper Part): {first_name_upper}")
print(f"Last Name (Lower Part): {last_name_lower}")
print(f"Full Name Reversed: {reversed_name}")



