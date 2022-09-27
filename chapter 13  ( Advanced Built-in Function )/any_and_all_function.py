number1=[2,4,6,8,10]
number2=[1,2,3,4,5,6]

# all function

print(all([True,True,True]))
print(all([True,True,False]))
print("\n")

# any function

print(any([True,False,False]))
print(any([False,False,False]))
print("\n")

# list comprehension with all function



print(all([num%2==0 for num in number1]))
print(all([num%2==0 for num in number2]))
print("\n")

# list comprehension with any function



print(any([num%2==0 for num in number1]))
print(any([num%2==0 for num in number2]))