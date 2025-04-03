#building a better calculator with python
num1 = float(input ("Enter the first number: "))
op = input ("Enter the operator: ")
num2 = float(input ("Enter the second number: "))


if op == "+": # addition operator
    print(num1 + num2)
    
elif op == "-":# minus operator
    print(num1 - num2)
    
elif op == "/":#division operator
    print(num1 / num2)
    
elif op == "*":#multiplication operator
    print(num1 * num2)
    
elif op == "%":# remender operator
    print(num1 % num2)
else:
    print("Invalid operator ")


#look for more on this too
