# 68

n = int(input("Enter a positive integer: "))

digits = 0
total = 0
even = 0
odd = 0

for i in range(1000):  # loop will stop when n becomes 0
    if n == 0:
        break

    digit = n % 10
    digits = digits + 1
    total = total + digit

    if digits == 1:
        largest = digit
        smallest = digit
    else:
        if digit > largest:
            largest = digit

        if digit < smallest:
            smallest = digit

    if digit % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

    n = n // 10

print("Digits:", digits)
print("Sum:", total)
print("Largest:", largest)
print("Smallest:", smallest)
print("Even Digits:", even)
print("Odd Digits:", odd)



# 69

s = input("Enter a string: ")

total = 0
vowels = 0
consonants = 0
uppercase = 0
lowercase = 0
even_index = 0

for i in range(len(s)):
    ch = s[i]
    total = total + 1

    if i % 2 == 0:
        even_index = even_index + 1

    if ch != " ":
        if ch.lower() in "aeiou":
            vowels = vowels + 1
        else:
            consonants = consonants + 1

        if ch.isupper():
            uppercase = uppercase + 1
        elif ch.islower():
            lowercase = lowercase + 1

print("Total Characters:", total)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Even Index Characters:", even_index)