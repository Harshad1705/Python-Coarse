

x=5    # global variable

def func() :
    global x
    x=7        # value of x now changes
    y=6        # local variable 
    return x,y

print(x)
print(func())