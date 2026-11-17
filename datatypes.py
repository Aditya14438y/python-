# task 1 Store and Display

name=input("enter your name :")
print(name,type(name))
age=int(input("enter your age :"))
print(age,type(age))
height=float(input("enter your height:"))
print(height,type(height))
student=input(" you are a student:").lower()=="true"
print(student,type(student))

# Task 2: Type Identification
a=100
print(type(a))
b=99.99
print(type(b))
c="Python"
print(type(c))
d=True
print(type(d))

# Take two integer variables and perform:
a=int(input("enter first number :"))
b=int(input(" enter second number :"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

# Task 4: Float Calculations
l=float(input("enter first value :"))
w=float(input("enter second value :"))
area=l*w
print(area)
perimeter=2*(l+w)
print(perimeter)

# Task 5: String Information
name="aditya kulkarni"
print(len(name))
print(name[0])
print(name[-1])
print(name.upper())

# Task 6: Boolean Check
a=is_logged_in=False
print(is_logged_in)
is_logged_in=True
print(is_logged_in)

# Task 7: Type Conversion
a=59
print(float(a))
print(type(float(a)))
b=89.0
print(int(b))
print(type(int(b)))
c="500"
print(int(c))
print(type(int(c)))
d=69
print(str(d))
print(type(str(d)))

# Task 8: User Information
name=input("enter your name :")
age=int(input("enter your age :"))
print("hello",name,"you are",age,"years old")
print(type(name))
print(type(age))