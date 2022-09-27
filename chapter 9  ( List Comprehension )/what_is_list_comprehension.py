
# with the help of list comprehension we can create list in one line 

#  create a list of square from 1 to 10

square=[i**2 for i in range(1,11)]
print(square)

# create a list of negative number from 1 to 10

negative=[ -i for i in range(1,11)]
print(negative)

# create a list of first number of another list

name=["harshad","mohit","rohit"]

new_name=[i[0] for i in name]

print(new_name)