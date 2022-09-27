# you will have to complete understanding of function
# first class function / closures
# then finally we will learn about decorators

def square (a) :
    return a**2

print(square(7))

s=square
print(s(5))

print("\n\n")

print(s.__name__)
print(square.__name__)
print(s)
print(square)