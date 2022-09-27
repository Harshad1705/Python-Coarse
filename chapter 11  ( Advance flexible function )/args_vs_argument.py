
def sum(*args) :
    total=1
    for i in args :
        total+=i
    return total

num1=[2,3,4]
num2=(4,5,6)

# print(sum(num1))  // error

print(sum(*num1))

print(sum(*num2))   # * unpacked the values inside list and tuples