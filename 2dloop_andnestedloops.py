#working with the 2d lists and the nested loops


#2d lists

number_grid = [
[1,2,3],
[4,5,6],
[7,8,9],
[0]
]

# accessing lists from the grid list and the specific element in the specified list
print()

print(number_grid[0][0])

print()
print(number_grid[2][1])
print()

# dealing with the nested loop where a loop is in another loop


for row in number_grid:
    for col in row:
        print(col)


