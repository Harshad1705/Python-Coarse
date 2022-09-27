
def greater(a,b) :
    if a>b :
        return a
    return b

def greatest(a,b,c) :
    bigger=greater(a,b)
    return greater(bigger,c)   # return greate(greater(a,b),c)


print(greatest(10,20,30))

# kiss-- keep it simple stupid 