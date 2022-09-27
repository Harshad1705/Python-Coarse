
names=["harshad","mohit"]

def fun(l,**kwargs) :
    if kwargs.get("reverse_str")==True :
        return [i[::-1].title() for i in names]
    else :
        return [i.title() for i in names]

print(fun(names,reverse_str=True ))
