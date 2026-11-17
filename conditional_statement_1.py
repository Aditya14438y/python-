# Check whether a number is positive, negative, or zero.

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
# Check whether a number is even or odd.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

    num = int(input("Enter a number: "))


# Find the greater of two numbers.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("First number is greater")
elif num2 > num1:
    print("Second number is greater")
else:
    print("Both numbers are equal")
# Find the greatest of three numbers.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2 and num1 > num3:
    print("First number is greatest")
elif num2 > num1 and num2 > num3:
    print("Second number is greatest")
elif num3 > num1 and num3 > num2:
    print("Third number is greatest")
else:
    print("Two or more numbers are equal or tied for greatest")

# Check whether a person is eligible to vote (age 18 or above).
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# Check whether a student has passed or failed (pass marks: 35).

marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")
    
# Check whether a character is a vowel or consonant.

char = input("Enter a character: ")

if len(char) != 1 or not char.isalpha():
    print("Please enter a single alphabet")
elif char.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")
# Check whether a year is a leap year.

year = int(input("Enter a year: "))

if year <= 0:
    print("Invalid year")
elif year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")
# Check whether a number is divisible by both 5 and 11.

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")
# Check whether a person is eligible for a driving license (minimum age: 18).

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age >= 18:
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")