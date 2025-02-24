#dealing with the input function to make the program interactive to the users


print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")


#anything = input("Enter a number: ")
#something = anything ** 2.0
#print(anything, "to the power of 2 is", something)

#dealing with input to be able to get numbers from the user validly

anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)
#calculating the length of the hypoternuse
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)
# the other way too

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)

# working on the string operators + and *

fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")
