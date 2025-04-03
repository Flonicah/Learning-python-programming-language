#if statements
# if statements
print("Dealing with the if statement in python")
print()

is_female = True


if is_female:
    print("You are a female")

else:
    print("You are not a female")



# another one

is_tall = False


#using the or key word


if is_female or is_tall:
        print("You are a female or tall")

else:
    print()
    print("You are neither a female nor tall")

# using the and operateor in the if statement

if is_female and is_tall:
    print()
    print ("wow you are a tall female")
elif is_female and not(is_tall):
    print()
    print("You are a short female")

elif not(is_female)  and is_tall:
    print()
    print("You are not a female but you are tall")
else:
    print()
    print(" you are  not female and  not tall")

# using comparison in the if statements

#if statements comparisons


def max_num( num1,num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print()
print("The results of the if comparison statement")
print()
print(max_num(3000,44,55))
    
# you cam compare all data types , strings and more,
#we can use the == for equal, != for not equal , <,  > >=, <= and more
