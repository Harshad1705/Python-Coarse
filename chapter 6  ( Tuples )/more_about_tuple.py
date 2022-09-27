
mixed=(1,2,3,4,5)

# looping in tuple

for i in mixed :
    print(i)                   # we can use while loop too

# tuple with one element

num=(1)                     # not a tuple 
word=('word1')                # not a tuple 

print(type(num))
print(type(word))

num1=(1,)                     #  a tuple 
word1=('word1',)                #  a tuple 

print(type(num1))
print(type(word1))

# tuple without parenthesis

name="harshad","mohit","harsh","lucky"
print(type(name))

# tuple unpacking

name="harshad","mohit","harsh","lucky"
name1,name2,name3,name4=name
print(name1)
print(name2)
print(name3)
print(name4)

# list inside tuple

fruits=["mango","banana",["pear","grapes"]]

fruits[2].pop()                  # all methods of list are used in list inside tuple
print(fruits)

# other some function used in tuples 

# min(),max(),sum 