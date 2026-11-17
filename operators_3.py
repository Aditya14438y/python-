# 1.Take two numbers as input and perform:
# Addition
# Subtraction
# Multiplication
# Division
# Modulus

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

# 2.Find whether a given number is even or odd using the modulus (%) operator.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

num = int(input("Enter a number: "))
# 3.Calculate the square and cube of a number using the exponent (**) operator.

print("Square:", num ** 2)
print("Cube:", num ** 3)

# 4.Swap two numbers without using a third variable.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After swapping:")
print("a:", a)
print("b:", b)

# 5.Find the quotient and remainder when one number is divided by another.


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Quotient:", a // b)
print("Remainder:", a % b)
