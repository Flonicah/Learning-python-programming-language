# drawing a rectangle program
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")


#ones own trying code to draw am object
print("7" + 5 *"^" + "7")
print(("|" + " " * 4 + "|\n"), end="")
print(("|" + " " * 3 + "|\n"), end="")
print(("|" + " " * 2 + "|\n"), end="")
print(("|" + " " * 1 + "|\n"), end="")


#working on the lab exercise give by cisco networking acadamy

# input a float value for variable a here
a =float(input("Enter the number of ur choice: "))
# input a float value for variable b here
b=float(input("Enter the second number of ur choice here too: "))
# all operators
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print()
print("\nThat's all, folks!")



x = float(input("Enter value for x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)
