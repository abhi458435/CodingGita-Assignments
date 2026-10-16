# Q37. Print Characters with Index
str1=input("Enter Your Word:")
for i in range(0,len(str1)):
       print(i,str1[i])

# Q38. Count Characters Without len()
str2=input("Enter Your Word:")
count=0
for i in str2:
    count=count+1
print(count)

# Q39. Count Vowels and Consonants
str3=input("Enter Your Number:")
vowels=0
consonants=0
for k in str3:
 if k in "aeiouAEIOU":
  vowels=vowels+1
 else:
   consonants=consonants+1
print("Vowels:",vowels)
print("Consonants:",consonants)

# Q40. Character Frequency
string=input("Enter Your String:")
chracter=input("Enter Your Specific Character:")
count=0
for p in string:
   if p in chracter:
      count=count+1
print(count)

# Q41. First Occurrence Position
string = input("Enter Your String: ")
character = input("Enter Your Specific Character: ")
count = 0
found = False
for p in string:
    if p == character:
        print(count)
        found = True
        break
    count = count + 1

if found == False:
    print("Not Found")

#Q42. Count Uppercase and Lowercase
word=input("Enter Your Number:")
upper=0
lower=0
for p in word:
    if p.isupper():
        upper=upper+1
    elif p.islower():
        lower=lower+1
print("Uppercase=",upper)
print("Lowercase",lower)


#Q43. Character Code Analyzer
str1=input("Enter Your Word:")
for i in str1:
    print(i,ord(i))


# Q44. String Without Vowels
str2=input("Enter Your Word:")
for i in str2:
    if i not in "aeiou":
        print(i,end="")
