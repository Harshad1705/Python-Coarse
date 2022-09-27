
# by map function

number=[1,2,3]

def square(a) :
    return a**2

squares=list(map(square,number))
print(squares)

# by lambda function

square2=list(map(lambda i:i**2,number))
print(squares)

# by list comprehension

square3=[i**2 for i in number]
print(square3)

# without all these 

new_num=[]
for i in number :
    new_num.append(square(i))
print(new_num)

# Map function is an iterable

names=["harshad","mohit","rohit"]
length=map(len,names)
for i in length:
    print(i)