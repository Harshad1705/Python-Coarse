
# generate list with range function

number=list(range(1,11))
print(number)

print("\n\n")

# more about pop method

new_number=number.pop()     #pop also  return value
print(number) 
print(new_number)

print("\n\n")


# index method

# list_number=[1,2,3,4,5,6,7,8,9,10,1,5,6,7,1]
# print(list_number.index("5"))

# pass list to a function

def double_list(l) :
    double=[]
    for i in number :
        double.append(i*2)
    return double

print(double_list(number))