# My Code 
l=[[1,2,3],[4,5,6],[7,8,9]]

def average(l) :
    l1,l2,l3=list(zip(*l))
    new_list=[]
    i=0
    for i in range(3) :
        new_list.append((l1[i]+l2[i]+l3[i])/3)
    return new_list
print(average(l))

# Harshit code 

def average_finder(*args) :        # *args take input in ----  ( [],[] )
    averages=[]
    for pair in zip(*args) :       # here * unpack the tuple 
        averages.append(sum(pair)/len(pair))
    return averages

print(average_finder([1,2,3],[4,5,6]))

# code in one line 

avg=lambda *args :[ sum(pair)/len(pair) for pair in zip(*args)]

print(avg([1,2,3],[4,5,6],[7,8,9],[10,11,12]))