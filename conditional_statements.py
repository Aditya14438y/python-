# CONDITIONAL STATEMENTS:
# Check whether a number is positive, negative, or zero.

num=int(input("enter your favourite number   :"))
if num>0:
    print(" number is positive  ")
elif num<0:
    print(" number is negative")
else:
    print("number is zero ")

# Determine if a number is even or odd.

num=int(input(" enter a number   :"))
if num%2==0:
    print(" number is even  ")
else:
    print(" num is odd  ")
# Check if a person is eligible to vote (age ≥ 18).

age= int(input(" enter your age  :"))
if age>=18:
    print(" your eligible for vote  ")
else:
    print(" your not eligible for vote ")
# Find the largest of two numbers.

num1=int(input(" enter your number  :"))
num2=int(input(" enter your number  :"))
if num1>num2:
    print(" num1 is greater  ")
elif num1==num2:
    print("both are equal")
else:
    print("num2 is greater ")
# Find the largest of three numbers.

num1=int(input(" enter your number  :"))
num2=int(input(" enter your number  :"))
num3=int(input(" enter your number  :"))
if num1==num2==num3:
    print(" all are equal")
elif num1>=num2 and num1>=num3:
    print("num1 is greater")
elif num2>=num3 and num2>=num1:
    print(" num2 is greater")
else:
    print(" num3 is greater")
# Check whether a year is a leap year.

year=int(input(" enter a year  :"))
if year%4==0 and year%100!=0:
    print(year," is a  leap year")
elif year%400==0:
    print(year,"is a leap year")
else:
    print(" it is not a leap year  ")
# Determine if a character is a vowel or consonant.

char = input("Enter a character: ")

if len(char) != 1:
    print("Please enter only one character")

elif not char.isalpha():
    print("Please enter an alphabet")

elif char.lower() in "aeiou":
    print("It is a vowel")

else:
    print("It is a consonant")
# Check whether a number is divisible by 5 and 11.
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")

marks = int(input("Enter your marks: "))
# Assign grades based on marks (A, B, C, D, Fail).
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Fail")
# Check if a number is a multiple of both 3 and 7.

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 7 == 0:
    print("Multiple of both 3 and 7")
else:
    print("Not a multiple of both 3 and 7")
# Determine whether a given number is a two-digit number.

num = int(input("Enter your number: "))

if (num >= 10 and num <= 99) or (num >= -99 and num <= -10):
    print("It is a two-digit number")
else:
    print("It is not a two-digit number")
# Check if a character is an alphabet, digit, or special character.

char = input("Enter a character: ")

if len(char) != 1:
    print("Please enter only one character")
elif char.isalpha():
    print("It is an alphabet")
elif char.isdigit():
    print("It is a digit")
else:
    print("It is a special character")
# Create a simple calculator using if-elif (add, subtract, multiply, divide).

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", num1 / num2)
else:
    print("Invalid operator")
# Check whether a triangle is valid based on its angles.

angle1 = int(input("Enter first angle: "))
angle2 = int(input("Enter second angle: "))
angle3 = int(input("Enter third angle: "))

total = angle1 + angle2 + angle3

if angle1 > 0 and angle2 > 0 and angle3 > 0 and total == 180:
    print("Valid triangle")
else:
    print("Invalid triangle")
# Determine the type of triangle (equilateral, isosceles, scalene).
side1 = int(input("Enter first side: "))
side2 = int(input("Enter second side: "))
side3 = int(input("Enter third side: "))

if side1 <= 0 or side2 <= 0 or side3 <= 0:
    print("Invalid side lengths")
elif side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
    print("Invalid triangle")
elif side1 == side2 == side3:
    print("Equilateral triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

num = int(input("Enter a number: "))
# Find whether a number is greater than 100, equal to 100, or less than 100.

if num > 100:
    print("Number is greater than 100")
elif num == 100:
    print("Number is equal to 100")
else:
    print("Number is less than 100")

# Check if a given temperature is cold, warm, or hot.

temperature = float(input("Enter temperature: "))

if temperature < 25:
    print("Cold")
elif temperature <= 34:
    print("Warm")
else:
    print("Hot")
# Determine whether a person is a child, teenager, adult, or senior based on age.

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 40:
    print("Adult")
else:
    print("Senior")
# Check whether a number lies between 1 and 50.

num = int(input("Enter a number: "))

if num >= 1 and num <= 50:
    print("Number lies between 1 and 50")
else:
    print("Number does not lie between 1 and 50")
# Verify if a given password is valid (length condition).

password_length=input(" enter password   :")
if len(password_length)==4:
    print("the password is valid  :")
else:
    print(" try again")
# Check if a year is a century year.
                                                                                                                                                                                 
year=int(input("enter a year  :"))
if year%100==0:
    print("it is a century year ")
else:
    print(" it is not century year ")
# determine whether a number is divisible by 2, 3, or both.

num=int(input(" enter your number  :"))
if num%2==0 and num%3==0:
    print(" it is divisible by both 2 and 3 ")
elif num%2==0:
    print(" it is divisible by 2 ")
elif num%3==0:
    print(" it is divisible by 3")

else:
    print(" it is not divisible 2, 3 and both")
# Find the smallest of three numbers.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 == num2 == num3:
    print("All numbers are equal")

elif num1 <= num2 and num1 <= num3:
    print("num1 is smallest")

elif num2 <= num1 and num2 <= num3:
    print("num2 is smallest")

else:
    print("num3 is smallest")

# Check whether a number is a perfect square (basic logic).

num=int(input("enter your number  :"))
square=num**0.5
if square.is_integer():
    print("it is  perfect square ")
else:
    print("it is not a perfect square")
# Determine the profit or loss based on cost price and selling price.

cost_price=int(input(" enter cost price   :"))
selling_price=int(input(" enter selling_price   :"))
if cost_price<selling_price:
    print(" profit")
elif cost_price==selling_price:
    print("no profit no loss")
else:
    print("loss")
# Check if a student passes or fails (minimum marks condition).

marks=int(input(" enter your marks  :"))
if marks>=45:
    print("pass")
else:
    print("fail")
# Determine whether a given day number (1–7) is a weekday or weekend.

day_number = int(input("Enter day number (1-7): "))

if day_number >= 1 and day_number <= 5:
    print("Weekday")

elif day_number == 6 or day_number == 7:
    print("Weekend")

else:
    print("Invalid day number")
# Check if a number is positive and even.

num=int(input("enter your number  :"))
if num>0 and num%2==0:
    print(" it is positive and even number")
elif num>0 and num%2!=0:
    print("it is positive and odd number ")
elif num<0:
    print(" it is negative number")
else:
    print("it  either positive nor negative ")
# Classify BMI into underweight, normal, overweight, obese.

weight=int(input("enter your weight  :"))
height=float(input(" enter your height    :"))
total=height*height
bmivalue=weight/total
print("your bmi:",round(bmivalue,2))
if bmivalue<18.5:
    print(" under weight")
elif bmivalue<25:
    print("normal weight")
elif bmivalue<30:
    print("over weight")
else:
    print("obese")
# Determine electricity bill category based on units consumed.

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in metres: "))

if weight <= 0 or height <= 0:
    print("Invalid weight or height")

else:
    bmi = weight / (height ** 2)

    print("Your BMI:", round(bmi, 2))

    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal weight")
    elif bmi < 30:
        print("Overweight")
    else:
        print("Obese")