
def num(n):
    for i in range(1,n+1) :
        if i%2==0 :
            yield(i)

n=num(15)

for i in n :
    print(i)