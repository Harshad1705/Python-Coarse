

# set is a data type
# unordered collection of unique items

s={1,2,3,2}
print(s)

# print(s[2])       // error

# used to remove duplicate items 

l=[1,2,3,4,5,5,5,5,6,6,6,7,8,8,]
s1=set(l)
print(s1)

# add method 

s.add(9)
s.add(10)
s.add(4)

print(s)

# remove method

s.remove(10)
print(s)

            # s.remove(15)   // error

# discard method

s.discard(15)
print(s)

# clear method 

print(s.clear())


# what we can store in sets

# we cannot store list , tuple , and dictionary in sets 

s2={1,1.0,2.0,"harshad"}
print(s2)