
n=int(input(" enter a number : "))

def cube_dict(n) :
    cube_dict={}
    for i in range(1,n+1) :
        cube_dict[i]=i**3
    return cube_dict

print(cube_dict(n))