# Arithmetic Operators

l=int(input("enter length  :"))
w=int(input("enter width    :"))
area=l*w
perimeter=2*(l+w)
print(area)
print(perimeter)

num1=int(input("enter first number   :"))
num2=int(input("enter second number   :"))
print("quotient",num1//num2)
print("remainder",num1%num2)

num1=int(input("enter first number   :"))
print("square",num1**2)
print("cube",num1**3)

# Assignment Operators
a=int(input("enter a number  :"))
a+=10
print(a)
a-=5
print(a)
a*=2
print(a)
a/=3
print(a)

a=30
b=50
a,b=b,a
print("a",a)
print("b",b)

# Comparison Operators
a=int(input("enter a number  :"))
b=int(input("enter a number  :"))
if a>=b:
    print(" number is greater ")
elif a<=b:
    print(" number is lesser ")
else :
    print("number is equal ")

marks=int(input("enter your marks  :"))
if marks>=35:
    print(" congratulation you have  passed the exam ")
else:
    print(" fail")
    
# Logical Operators

age=int(input("enter your age  :"))
proof=input(" do You have valid_id_proof?   :")
if age>=18 and proof=="yes":
    print("eligible for vote")
elif age>=18 and proof=="no":
    print("not eligible for vote")
else:
    print(" better for next time ")

num=int(input("enter a number  :"))
if num>=1 and num<=100:
    print(" it lies between 1 and 100")
else:
    print(" it does not lies between 1 and 100") 

year=int(input("enter a number   :"))
if year%4==0 and year%100!=0:
    print(" it is a leap year   :")
elif year%400==0:
    print(" it is a leap year ")
else:
    print(" it is not a leap year")
num1= int(input("enter first number  :"))
num2= int(input("enter second number  :"))
print(num1&num2)
print(num1|num2)
print(num1^num2)
print(~num1)

# Bitwise Operators

num=int(input("enter your number  :"))
position=int(input("enter your position  :"))
leftshift=num<<position
print(leftshift)

num1=int(input(" enter your number  :"))
position=int(input(" enter your second number  :"))
rightshift=num1>>position
print(rightshift)