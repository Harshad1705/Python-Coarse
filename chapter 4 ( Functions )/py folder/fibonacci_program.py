
def fibonacci(n) :
    a=0
    b=1
    if n==1 :
        print(a)
    elif n==2 :
        print(a,b)
    else :
        print(a,b,end=" ")
        i=0
        for i in range(n-2) :
            c=a+b
            a=b
            b=c
            print(b,end=" ")

num=int(input("enter a number : "))

fibonacci(num)