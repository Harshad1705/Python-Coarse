
# Map function

l=[1,2,3,4]

def square(a) :
    return a**2

print(list(map(square,l)))

# Create our function like map function

def my_map ( func, l) :
    new_list=[]
    for i in l :
        new_list.append(func(i))
    return new_list

print(my_map(square,l))

# By list comprehension

def my_map2 ( func, l) :
    return [func(i) for i in l]

print(my_map2(square,l))