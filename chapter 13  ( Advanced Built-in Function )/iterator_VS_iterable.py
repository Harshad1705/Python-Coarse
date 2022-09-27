
number=[1,2,3,4,5]    # list,tuple,string-----> iterables
          
square=map(lambda i:i**2,number)    #  map,filter------->iterator

# for i in number :                   working of for loop
#     print(i)                        number_iter=iter(number)    /// connvert iterable to iterator
                                    #   print(next(square))
# print("\n\n")                         print(next(square))
                                #       print(next(square))
# for i in square :
#     print(i)

print("\n\n")

print(next(square))
print(next(square))
print(next(square))


# print(next(number))   // error