
name=["harshad","mohit","rohit"]

def rev(l) :
    rev_name=[]
    for i in l :
        rev_name.append(i[-1::-1])
    return rev_name

print(rev(name))



def rev(l) :
    return [ i[::-1] for i in l ]

print(rev(name))