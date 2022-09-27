# generators are iterartor

# iterator,iterable

l=[1,2,3]  # iterable

# for i in l :
#     print(i)

# i=iter(l)
# print(next(i))
# print(next(i))
# print(next(i))

for  i in map(lambda a:a**2 , l) :   # iterator
    print(i)

# memory ------- [............................] , list
# memory -------(1)  , generator

# if we have use sequence -- again and again --- list,tuple,etc
#                         -- only once       --- use generator
 
