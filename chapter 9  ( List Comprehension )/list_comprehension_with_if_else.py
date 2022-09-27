

num=list(range(1,11))

new_num=[]
for i in num :
    if i%2==0 :
        new_num.append(i*2)
    else :
        new_num.append(-i)
print(new_num)


new_list=[ i*2 if i%2==0 else -i for i in num]
print(new_list)