
# fromkeys method         // used to create dictionary 
                         # // used to assign same values for many key

d={
    'name':'unknown','age' : 'unknown',
}
print(d)

d1=dict.fromkeys(['name','age'],"unknown")
print(d1)

d2=dict.fromkeys(("name","age"),"unknown")
print(d2)

d3=dict.fromkeys(('abc'),"unknown")
print(d3)

d4=dict.fromkeys(range(1,11),"numbers")
print(d4)

d5=dict.fromkeys(["name","age"],["unknown","unknown"])
print(d5)

# get method                // used to access keys

d6={"name":"harshad","age":18}

print(d6["name"])          # harshad
# print(d6["height"])        # error

print(d6.get("name"))      # harshad
print(d6.get("height"))    # none

if d.get("name") :
    print("present")
else :
    print("not present")


if d.get("height") :            # if none ---> false   and   else ---> true
    print("present")
else :
    print("not present")


# clear method         # used to delete data of dictionary

d.clear()
print(d)

# copy method             // used to create copy of dictionary 

d7=d6.copy()
print(d7)