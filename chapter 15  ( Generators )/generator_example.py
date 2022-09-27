# Generator function

def num(n) :
    for i in range(1,n+1):
        yield(i)

numbers=num(10)

for i in numbers :
    print(i)

for i in numbers :
    print(i)


# generator advantage :

# 1. memory efficiently used
# 2. increase performance