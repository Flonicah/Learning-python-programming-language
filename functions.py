#using functions in python
# collection of code that performs a task which i called to get to work#creating a function
# key word  def

def say_hi():
    print("hello User")

#calling the function to execute it
print("Top")
print()
say_hi()
print()
print("Bottom")
print()
print("Passing on the parameters to the defined function")
print()


# passing in parameters to the functions in this case name and age can use one parameter too


def floxy(name, age):
    print("Hello" + name + " , you are " + age)
    

floxy("Flonicah","24")
print()
floxy("Lughano", "25")

