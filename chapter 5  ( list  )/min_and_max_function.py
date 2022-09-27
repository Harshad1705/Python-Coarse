
numbers=[6,60,2,5]

# min function

print(min(numbers))


# max function

print(max(numbers))


print("\n\n")

# function find greatest difference

def greatest_difference(l) :
    return max(l)-min(l)

print(greatest_difference(numbers))