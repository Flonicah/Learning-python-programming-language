#continuation of video learning python lesson
# getting access to more function by importing them


# importing math
from math import * # allow to do more with math funtion and more
my_num = -5
print(floor(3.7))# gets the lower number 
print()
print(ceil(3.7))#gets the highest number of it

print()
print(sqrt(36))# the square roo

#check more on math functions in python


#getting inputs from a user into the program

print("Getting input fron the user")
print()

name = input("What is your Name; ")
print()
print("Hello " + name + "!")
print()
age = input("How old are you? ")
print()
print("Wow! " + name ,", so you are " + age + " years.")


#Building a basic Calculator
print("BUILDING A BASIC CALCULATOR")
print()
# getting numbers
num1 = input("Enter the first number; ")
num2 = input("Enter the second number; ")
result = num1 + num2
print(result) # it only concanate the without doing any basic math operations but takes in the input as strings

print()
print("dealing with numbers input to do the math opreations /function tasks")

#getting number with special py functions
#literals int and floats
# the int use first
num3 = input("Enter the  number; ")
num4 = input("Enter the another number; ")
results = int(num3) + int(num4)
print(results)

# using the float function now
num5 = input("Enter the first number; ")
num6 = input("Enter the second number; ")
resulted = float(num5)+ float(num6)
print(resulted)
