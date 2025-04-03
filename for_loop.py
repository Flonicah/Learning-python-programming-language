#dealing with the For loop in python

#creating for loop that loops through every item  specifird

for letter in "Girrafe Aademy":
    print(letter)

# getting deep into it on for loop on an array

friends =["Jim", "caro", "floxy"]
print("Using the For Loop on Friends Array")
# creating the for loop to work on the friends array
print()
for friend in friends:
    print()
    print(friend)
#indexing with for loop
    print()
print("Indexting numbers on range of ten")
print()
for index in range(10):
    print(index)
print()
#print("range print between 3 and 10")
for index in range(3,10):
    print(index)

#length of array
    print()
    print("Indexing length of an array")
for index in range(len(friends)):
    print(friends[index])


print()

for index in range(5):
    if index ==0:
        print("first  iteration")
    else:
        print("Not first iteration")
