
number=list(range(1,11))

# create a list of even number

even=[]
for i in number :
    if i%2==0 :
        even.append(i)

print(even)

even_num=[ i for i in number if i%2==0]
print(even_num)

even_num1=[ i for i in range(1,16) if i%2==0]
print(even_num1)
