# we use enumerate function with for loop to track position of our items in iterable


# how we can do this without enumerate funcyion

number=[1,2,3]
pos=0
for i in number :
    print(f"{pos} -----> {i}")
    pos+=1

# with enumerate function

for pos,i in enumerate(number) :
    print(f"{pos} -----> {i}")







name=["harshad","mohit","rohit"]

def indox_no ( l,name) :
    for pos,i in enumerate(l) :
        if i==name :
            return pos
    return -1
        

print(indox_no(name,"rohit"))