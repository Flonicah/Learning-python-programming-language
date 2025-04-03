#try except block for catching errors in python
print()
print("Using the try except to catch errors")
try:
    #value = 10/0
    number = int(input("Enter the number: "))
    print(number)

#except ZeroDivisionError:
except ZeroDivisionError as err: 
    print()
    print(err)


# accepting specific errors by creating a new specific except function

except ValueError:
     print("Invalid input")

