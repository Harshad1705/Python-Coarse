import time

t1=time.time()
l=[i**2 for i in range(10000000)]
t2=time.time()
g=[i**2 for i in range(10000000)]
t3=time.time()

# print(t2-t1)
print(t3-t2)