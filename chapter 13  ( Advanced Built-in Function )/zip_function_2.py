
l=[(1,2),(3,4),(5,6),(7,8)]

# * operator with zip

l1,l2=list(zip(*l))
print(list(l1))
print(list(l2))

print("\n\n")

new_list=[]
l4=[4,5,6,7]
l5=[8,9,10,11]

for pair in zip(l4,l5) :
    new_list.append(max(pair))
print(new_list)    