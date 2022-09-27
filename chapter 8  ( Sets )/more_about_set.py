
# in keyword in sets

s={"a","b",'c'}

if "a" in s :
    print("present")
else : 
    print("not present")

# looping in sets

for i in s :
    print(i)


# SET MATH

s1={1,2,3,4}
s2={3,4,5,6}

# union 

union=s1|s2
print(union)

# intersection

intersection=s1&s2
print(intersection)