
def cube(num,*args) :
    l=[]
    for i in args :
        l.append(i**num)
    return l

num1=[1,2,3]
print(cube(3,*num1))