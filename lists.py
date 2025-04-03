#dealing with the lists in python
#working with lists in python dealing with large amount of data

print()

# creating a list
friends = ["kelvin ", "karen "," james","caro", "john", "john"]

#accessing individual elements inside the list, using the index

print()
print(friends)
print()

print(friends[0])# access element based on the index

 #indexing using negatives it starts indexing from the back of the list
print()

print(friends[-1])

#selecting a part of the list

print()
print(friends[1:])
              
#modify element
friends[1] = "mike"
print()
print(friends[1:])

print()
#add, del , copy and more operations /functions in python

lucky_numbers =[2,3,4,5,6,7,8,9,0,1]
#the extend function takes a list and append function it to another list
friends.extend(lucky_numbers)
print("the extend function results")
print()
print(friends)

print()
#now using the append function on the list

friends.append("creed")# add an iterm at the end of the list

print(friends)

print()

# adding an iterm at the middle or any position of the list function
# use the insert function
friends.insert(1,"kelly")
print(friends)
print()
#removing the iterm in the list using the remove function
friends.remove("caro")
print()
print(friends)

friends.pop()#this pops an element in the list off 
print()
print(friends)
#friends.clear()#this clears the list

#print()
#print(friends)

#checking if am item is in the list

print()
print(friends.index("mike"))

# using the count function on the list to know how many elements are in the list
#counts the number of similar items in the list

print()
print(friends.count("john"))


# sorting the list of items in a list using the sort function can also work on strings into alpjhabetical order

lucky_numbers.sort()
print()
print(lucky_numbers)
#reverse  the list

lucky_numbers.reverse()
print(lucky_numbers)

# the other function used on the list is the copy function

friends2 = friends.copy()
print("COPY FUNCTION")
print()
print(friends2)
